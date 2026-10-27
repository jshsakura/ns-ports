#!/usr/bin/env python3
"""Generate Korean (SCKA-200.04) variants of ProjectCane 0.5.0's extractor sources.

The Korean executable is not the USA layout. Its tables sit at different addresses,
its levels use the Japanese/PAL "two UTF-16 localization tables" BRX form, and its
cutscene table matches PAL. So the Korean disc goes through the localized path
(the same one the Japanese disc uses), with one language slot instead of two.
On the content side it is labelled NTSC-J with a single "Japanese" slot, because
ProjectCane 0.5.0 has no Korean region and NTSC-J is the PAL-branch content type
that matches these levels.

usage: kr_patch_sources.py <ProjectCane src> <output dir>
Every replacement must match exactly once, so an upstream change fails loudly.
"""
import os
import sys

# Read from the Korean executable (SCKA_200.04) by kr-probe scripts.
KR_LEVEL_TABLE_VA = 0x00249C70     # 46 records x 44 bytes, one descriptor each
KR_CUTSCENE_TABLE_VA = 0x0024A570  # 16 descriptors + 1 special at table - 0x20
KR_LEVEL_IDENTITIES = [
    27, 28, 29, 30, 31, 32, 37, 34, 33, 36, 35, 38, 39, 40, 41, 45,
    46, 42, 43, 44, 47, 48, 49, 51, 50, 54, 52, 53, 55, 56, 57, 58,
    61, 59, 62, 64, 60, 63, 65, 66, 67, 68, 69, 70, 71, 72,
]
# Sound bank descriptor table at 0x002470C0, USA name order.
KR_SOUND_BANKS = [
    ("Common.bnk", 0xAA0A0), ("Intro.bnk", 0xBF5EA), ("Snow.bnk", 0xAB70D),
    ("Underwater.bnk", 0xAC1AF), ("Muggshot.bnk", 0xB0C2A), ("Voodoo.bnk", 0xB214C),
    ("Clockwerk.bnk", 0xA8F58),
]
PAL_CUTSCENE_IDENTITIES = "0x11, 0x16, 0x18, 0x13, 0x0D, 0x0A, 0x10, 0x0E, 0x12, 0x17, 0x07, 0x02, 0x19, 0x0F, 0x0C, 0x09, 0x08"


def replace_once(text, old, new, what):
    count = text.count(old)
    if count != 1:
        sys.exit("patch '%s': expected 1 match, found %d" % (what, count))
    return text.replace(old, new)


def patch_pal_iso_extractor(text):
    text = replace_once(text,
        'if (entry.name == "SCUS_971.98") region = DiscRegion::NtscU;',
        'if (entry.name == "SCUS_971.98") region = DiscRegion::NtscU;\n'
        '        else if (entry.name == "SCKA_200.04") region = DiscRegion::Japanese;',
        "DetectRegion")
    text = replace_once(text,
        'file.name.starts_with("SCPS_") || file.name.starts_with("SCPS-");',
        'file.name.starts_with("SCPS_") || file.name.starts_with("SCPS-") ||\n'
        '               file.name.starts_with("SCKA_");',
        "FindGameElf")
    banks = ",\n".join('    {"%s", 0x%06X}' % b for b in KR_SOUND_BANKS)
    korean = '''
namespace {
constexpr std::array<SoundBankLocation, 7> kKoreanSoundBanks = {{
%s
}};

void ExtractKoreanRegion(const IsoReader& iso, const IsoFile& elf,
    const std::filesystem::path& outputDirectory) {
    constexpr std::size_t kKoreanRecordSize = 44;
    const auto table = VaToIsoOffset(iso, elf, 0x%08X);
    if (table + kLevelCount * kKoreanRecordSize > iso.size())
        throw std::runtime_error("Korean level table lies outside the executable");
    iso.SetTotal(7 + 17 + kLevelCount);
    ExtractSoundBanks(iso, outputDirectory / "Worlds" / "Sound Banks", kKoreanSoundBanks, "Korean");
    static constexpr std::array<std::string_view, 1> languages = {"Japanese"};
    ExtractCutscenes(iso, elf, outputDirectory / "Cutscenes", 0x%08X, languages, "Korean", 1);
    const auto worldsDirectory = outputDirectory / "Worlds";
    for (std::size_t i = 0; i < kLevelCount; ++i) {
        iso.Report("Extracting worlds", std::string(kLevelNames[i]));
        const auto record = table + i * kKoreanRecordSize;
        const auto sector = U32(iso, record) ^ U32(iso, record + 20);
        const auto compressedSize = U32(iso, record + 4) ^ U32(iso, record + 28);
        const auto source = static_cast<std::size_t>(sector) * kSectorSize;
        if (compressedSize == 0 || compressedSize > kMaximumCompressedSize ||
            source > iso.size() || compressedSize > iso.size() - source)
            throw std::runtime_error("Invalid Korean descriptor at table index " + std::to_string(i));
        const auto decoded = Decompress(iso.Read(source, compressedSize), iso);
        const auto levelDirectory = LevelDirectory(worldsDirectory, i) / "Japanese";
        std::filesystem::create_directories(levelDirectory);
        const auto path = levelDirectory / (std::string(kLevelNames[i]) + ".brx");
        std::ofstream output(path, std::ios::binary);
        if (!output || !output.write(reinterpret_cast<const char*>(decoded.data()),
            static_cast<std::streamsize>(decoded.size())))
            throw std::runtime_error("Could not write " + path.string());
        output.close();
        BrxWalker walker(StringEncoding::Auto, BrxRegion::Japanese, !iso.HasCallback());
        walker.WalkFile(path);
        ExtractAudio(iso, levelDirectory / "Dialogs", walker.AudioDescriptors());
        ExtractAudio(iso, levelDirectory / "Commentary", walker.CommentaryDescriptors());
        ExtractMusic(iso, worldsDirectory / "Music", walker.MusicDescriptors());
        iso.Advance();
    }
}
}

DiscRegion PalIsoExtractor::DetectRegion''' % (banks, KR_LEVEL_TABLE_VA, KR_CUTSCENE_TABLE_VA)
    text = replace_once(text, "\nDiscRegion PalIsoExtractor::DetectRegion", korean, "Korean extractor")
    text = replace_once(text,
        '    const auto& elf = FindGameElf(rootFiles);\n\n    if (!IsJapaneseElf(elf)) {',
        '    const auto& elf = FindGameElf(rootFiles);\n'
        '    if (elf.name.starts_with("SCKA_")) {\n'
        '        ExtractKoreanRegion(iso, elf, outputDirectory);\n'
        '        return;\n'
        '    }\n\n    if (!IsJapaneseElf(elf)) {',
        "ExtractDetectedRegion")
    return text


def patch_brx_walker(text):
    ids = ", ".join(str(v) for v in KR_LEVEL_IDENTITIES)
    for name in ("japaneseLevelIdentities", "englishLevelIdentities"):
        start = text.index("constexpr std::array<std::uint32_t, 46> %s = {" % name)
        end = text.index("};", start)
        text = text[:start] + "constexpr std::array<std::uint32_t, 46> %s = {\n        %s\n    " % (name, ids) + text[end:]
    start = text.index("constexpr std::array<std::uint32_t, 18> japaneseIdentities = {")
    end = text.index("};", start)
    text = text[:start] + ("constexpr std::array<std::uint32_t, 18> japaneseIdentities = {\n        %s, 0xFFFFFFFF\n    "
                           % PAL_CUTSCENE_IDENTITIES) + text[end:]
    return text


def patch_binary_input_stream(text):
    # Korean BRX strings are UTF-16 Hangul. The upstream auto-detector only counts
    # UTF-16 code units whose high byte is zero, so Hangul text was read as a narrow
    # string of half its length and the walk derailed. Narrow BRX strings are ASCII,
    # so their byte pairs never land in the Hangul syllable block.
    return replace_once(text,
        "if ((c & 0xff00u) == 0 && (c & 0xffu) >= 0x20) ++zeroHigh;",
        "if (((c & 0xff00u) == 0 && (c & 0xffu) >= 0x20) || (c >= 0xAC00u && c <= 0xD7A3u)) ++zeroHigh;",
        "LooksLikeUtf16 Hangul")


def patch_iso_extractor(text):
    text = replace_once(text,
        'const std::vector<std::string> languages = japanese ? std::vector<std::string>{"Japanese", "English"} :',
        'const std::vector<std::string> languages = japanese ? std::vector<std::string>{"Japanese"} :',
        "Korean single slot")
    text = replace_once(text,
        '{"schemaVersion", 1}, {"game", japanese ? "Kaitou Sly Cooper" :',
        '{"schemaVersion", 1}, {"game", japanese ? "Sly Cooper (Korea)" :',
        "manifest game")
    text = replace_once(text, '{"serial", japanese ? "SCPS-150.36" :', '{"serial", japanese ? "SCKA-200.04" :', "manifest serial")
    text = replace_once(text,
        'if (japanese) manifest["voiceLanguages"] = {"Japanese", "English"};',
        'if (japanese) manifest["voiceLanguages"] = {"Japanese"};',
        "manifest voices")
    return text


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, out = sys.argv[1:]
    jobs = [
        ("File Extractor GUI/NativeTools/PalExtractor/PalIsoExtractor.cpp", "pal/PalIsoExtractor.cpp", patch_pal_iso_extractor),
        ("File Extractor GUI/NativeTools/BrxRebuilder/BrxWalker.cpp", "brx/BrxWalker.cpp", patch_brx_walker),
        ("File Extractor GUI/NativeTools/BrxRebuilder/BinaryInputStream.cpp", "brx/BinaryInputStream.cpp", patch_binary_input_stream),
        ("File Extractor GUI/NativeTools/PalExtractor/BinaryInputStream.cpp", "pal/BinaryInputStream.cpp", patch_binary_input_stream),
        ("platform/installer/iso_extractor.cpp", "platform/installer/iso_extractor.cpp", patch_iso_extractor),
    ]
    for rel, dst, fn in jobs:
        text = open(os.path.join(src, rel), encoding="utf-8").read()
        path = os.path.join(out, dst)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(fn(text))


if __name__ == "__main__":
    main()
