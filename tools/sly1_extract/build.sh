#!/bin/sh
# Builds a Linux host binary from ProjectCane 0.5.0's Switch extractor sources,
# with the Korean (SCKA-200.04) changes from kr_patch_sources.py.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
SRC=${CANE_SRC:?set CANE_SRC to a ProjectCane 0.5.0 checkout}
OUT=$HERE/build
GEN=$OUT/gen
rm -rf "$GEN" "$OUT/obj"; mkdir -p "$GEN/platform" "$OUT/obj"
ln -s "$SRC/File Extractor GUI" "$GEN/File Extractor GUI"
ln -s "$SRC/platform/switch" "$GEN/platform/switch"
python3 "$HERE/kr_patch_sources.py" "$SRC" "$GEN"
cp "$SRC/platform/installer/iso_extractor.h" "$GEN/platform/installer/"
CXX="g++ -std=c++20 -O2 -pthread -I$SRC/Libraries/include"
BRX="$SRC/File Extractor GUI/NativeTools/BrxRebuilder"
PAL="$SRC/File Extractor GUI/NativeTools/PalExtractor"
pids=""; objs=""
cc() { o="$OUT/obj/$1.o"; shift; objs="$objs $o"; $CXX "$@" -o "$o" & pids="$pids $!"; }
for s in AssetWalker GeometryWalker ObjectWalker OptionWalker SpliceWalker TriangleList; do
  cc brx_$s -DCBinaryInputStream=CaneBrxInputStream -c "$BRX/$s.cpp"
done
for s in BrxWalker BinaryInputStream; do
  cc brx_$s -DCBinaryInputStream=CaneBrxInputStream -iquote "$BRX" -c "$GEN/brx/$s.cpp"
done
for s in AssetWalker BrxWalker GeometryWalker ObjectWalker OptionWalker SpliceWalker; do
  cc pal_$s -c "$PAL/$s.cpp"
done
cc pal_BinaryInputStream -iquote "$PAL" -c "$GEN/pal/BinaryInputStream.cpp"
cc pal_PalIsoExtractor -iquote "$PAL" -c "$GEN/pal/PalIsoExtractor.cpp"
cc iso_extractor -DCBinaryInputStream=CaneBrxInputStream -c "$GEN/platform/installer/iso_extractor.cpp"
cc main -I"$GEN/platform/installer" -c "$HERE/main.cpp"
fail=0; for p in $pids; do wait "$p" || fail=1; done
[ "$fail" = 0 ] || { echo "compile failed"; exit 1; }
$CXX $objs -lz -o "$OUT/cane-extract"
echo "built $OUT/cane-extract"
