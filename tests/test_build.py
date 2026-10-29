import json
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build  # noqa: E402
import port_register  # noqa: E402


def jpeg(w, h):
    """SOI + SOF0 만 있는 최소 JPEG 헤더 (크기 검사용)."""
    sof = b"\xff\xc0" + (17).to_bytes(2, "big") + b"\x08" + h.to_bytes(2, "big") + w.to_bytes(2, "big") + b"\x03" + b"\x01\x11\x00\x02\x11\x01\x03\x11\x01"
    return b"\xff\xd8" + sof + b"\xff\xd9"


class FakeRoot(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old = build.ROOT_DIR
        build.ROOT_DIR = self.tmp.name
        self.dir = os.path.join(self.tmp.name, "ports", "demo")
        os.makedirs(os.path.join(self.dir, "in"))
        json.dump([{"id": "demo", "required_assets": "데모 데이터", "upstream": "https://example.com/demo"}],
                  open(os.path.join(self.tmp.name, "ports.json"), "w"))
        build.PORTS_JSON = os.path.join(self.tmp.name, "ports.json")
        json.dump({"id": "demo", "nro": {"src": "in/demo.nro", "out": "demo.nro"}},
                  open(os.path.join(self.dir, "port.json"), "w"))

    def tearDown(self):
        build.ROOT_DIR = self.old
        self.tmp.cleanup()


class SlotsTest(FakeRoot):
    def test_slots_are_derived_from_port_and_catalog_when_no_slots_file(self):
        slots = build.load_slots("demo")
        self.assertEqual([s["path"] for s in slots], ["in/demo.nro", "in/data"])
        self.assertIn("https://example.com/demo", slots[0]["get"])
        self.assertEqual(slots[1]["what"], "데모 데이터")

    def test_empty_required_slots_fail_the_check(self):
        self.assertFalse(build.check_slots("demo", quiet_ok=True))

    def test_filled_nro_and_data_pass_and_icon_stays_optional(self):
        open(os.path.join(self.dir, "in", "demo.nro"), "wb").write(b"x")
        os.makedirs(os.path.join(self.dir, "in", "data"))
        open(os.path.join(self.dir, "in", "data", "a.bin"), "wb").write(b"x")
        self.assertTrue(build.check_slots("demo", quiet_ok=True))

    def test_empty_data_dir_does_not_count_as_filled(self):
        open(os.path.join(self.dir, "in", "demo.nro"), "wb").write(b"x")
        os.makedirs(os.path.join(self.dir, "in", "data"))
        self.assertFalse(build.check_slots("demo", quiet_ok=True))

    def test_rom_argument_satisfies_the_data_slot(self):
        open(os.path.join(self.dir, "in", "demo.nro"), "wb").write(b"x")
        self.assertTrue(build.check_slots("demo", quiet_ok=True, rom="/some/folder"))

    def test_variant_only_slot_is_ignored_for_the_other_variant(self):
        json.dump([{"path": "in/a", "what": "a"}, {"path": "in/ko", "what": "ko", "variant": "ko"}],
                  open(os.path.join(self.dir, "slots.json"), "w"))
        open(os.path.join(self.dir, "in", "a"), "wb").write(b"x")
        self.assertFalse(build.check_slots("demo", "ko", quiet_ok=True))
        self.assertTrue(build.check_slots("demo", "original", quiet_ok=True))


class ReleaseTest(FakeRoot):
    def test_nro_is_taken_from_a_zip_member_and_checked_against_sha256(self):
        import hashlib, io, zipfile
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as z:
            z.writestr("pkg/demo.nro", b"NRODATA")
        blob = buf.getvalue()
        src = os.path.join(self.tmp.name, "rel.zip")
        open(src, "wb").write(blob)
        os.environ["NS_PORTS_CACHE"] = os.path.join(self.tmp.name, "cache")
        prof = {"_base": self.dir, "nro": {"src": "in/demo.nro"},
                "release": {"repo": "x/y", "tag": "t", "asset": "rel.zip", "member": "pkg/demo.nro",
                            "sha256": hashlib.sha256(blob).hexdigest()}}
        orig = port_register.fetch_url
        port_register.fetch_url = lambda e: blob
        try:
            port_register.ensure_nro(prof)
        finally:
            port_register.fetch_url = orig
        self.assertEqual(open(os.path.join(self.dir, "in", "demo.nro"), "rb").read(), b"NRODATA")

    def test_existing_nro_is_not_replaced(self):
        path = os.path.join(self.dir, "in", "demo.nro")
        open(path, "wb").write(b"MINE")
        prof = {"_base": self.dir, "nro": {"src": "in/demo.nro"}, "release": {"repo": "x/y", "tag": "t", "asset": "a"}}
        port_register.ensure_nro(prof)
        self.assertEqual(open(path, "rb").read(), b"MINE")

    def test_release_makes_the_nro_slot_optional(self):
        json.dump({"id": "demo", "nro": {"src": "in/demo.nro"}, "release": {"repo": "x/y", "tag": "t1", "asset": "a"}},
                  open(os.path.join(self.dir, "port.json"), "w"))
        self.assertTrue(build.load_slots("demo")[0]["optional"])


class IconTest(unittest.TestCase):
    def write(self, data):
        f = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        f.write(data)
        f.close()
        self.addCleanup(os.unlink, f.name)
        return f.name

    def test_256_square_jpeg_is_accepted(self):
        path = self.write(jpeg(256, 256))
        self.assertEqual(port_register.check_icon(path), path)

    def test_wrong_size_is_rejected_with_the_size_in_the_message(self):
        with self.assertRaises(SystemExit) as e:
            port_register.check_icon(self.write(jpeg(512, 512)))
        self.assertIn("512x512", str(e.exception))

    def test_non_jpeg_is_rejected(self):
        with self.assertRaises(SystemExit) as e:
            port_register.check_icon(self.write(b"\x89PNG\r\n"))
        self.assertIn("JPEG", str(e.exception))


if __name__ == "__main__":
    unittest.main()
