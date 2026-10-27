// Builds precomposed Hangul syllable glyphs from the Korean disc's own conjoining-jamo
// glyphs (U+1100.. initial, U+1161.. medial, U+11A8.. final). The PS2 game composes
// syllables from these at draw time. The port draws one glyph per code point, so we
// append ready-made syllable cells to each level's font atlas and glyph table.
#pragma once
#include <algorithm>
#include <cstdint>
#include <set>
#include <vector>

namespace krfont {

struct Glyph { std::uint16_t ch, x, y, width; };

inline std::set<std::uint32_t>& Used() { thread_local std::set<std::uint32_t> s; return s; }
inline void Reset() { Used().clear(); }
inline void NoteCodePoint(std::uint32_t cp) { if (cp >= 0xAC00u && cp <= 0xD7A3u) Used().insert(cp); }

constexpr unsigned kCell = 41;       // jamo cell height and advance in the Korean font
constexpr unsigned kPitch = 42;      // atlas grid pitch (one pixel gap)
constexpr unsigned kMaxHeight = 8192;

inline const Glyph* Find(const std::vector<Glyph>& g, std::uint16_t ch) {
    for (const auto& e : g) if (e.ch == ch) return &e;
    return nullptr;
}

// Composites the three jamo cells of `syllable` into dst at (dx, dy) using "over".
inline void Compose(const std::vector<std::uint8_t>& src, unsigned sw, unsigned sh,
                    std::vector<std::uint8_t>& dst, unsigned dw, unsigned dx, unsigned dy,
                    const Glyph* parts[3]) {
    for (int p = 0; p < 3; ++p) {
        if (!parts[p]) continue;
        for (unsigned y = 0; y < kCell; ++y) for (unsigned x = 0; x < kCell; ++x) {
            const unsigned sx = parts[p]->x + x, sy = parts[p]->y + y;
            if (sx >= sw || sy >= sh) continue;
            const std::uint8_t* s = &src[(std::size_t(sy) * sw + sx) * 4];
            std::uint8_t* d = &dst[(std::size_t(dy + y) * dw + dx + x) * 4];
            const unsigned sa = s[3], da = d[3];
            if (!sa) continue;
            const unsigned oa = sa + da * (255 - sa) / 255;
            for (int c = 0; c < 3; ++c)
                d[c] = std::uint8_t(oa ? (s[c] * sa + d[c] * da * (255 - sa) / 255) / oa : 0);
            d[3] = std::uint8_t(oa);
        }
    }
}

// Appends syllable glyphs. Returns false (leaving everything untouched) when this font has
// no jamo or the level uses no Hangul.
inline bool Augment(std::vector<std::uint8_t>& rgba, std::uint32_t& w, std::uint32_t& h,
                    std::vector<Glyph>& glyphs) {
    if (Used().empty() || !Find(glyphs, 0x1100) || !Find(glyphs, 0x1161) || !Find(glyphs, 0x11A8)) return false;
    const unsigned cols = (w - 1) / kPitch;
    if (!cols) return false;
    std::vector<std::uint32_t> list(Used().begin(), Used().end());
    unsigned rows = (unsigned(list.size()) + cols - 1) / cols;
    while (rows && h + 1 + rows * kPitch > kMaxHeight) { --rows; }
    list.resize(std::size_t(rows) * cols < list.size() ? std::size_t(rows) * cols : list.size());
    const std::uint32_t nh = h + 1 + rows * kPitch;
    std::vector<std::uint8_t> out(std::size_t(w) * nh * 4, 0);
    std::copy(rgba.begin(), rgba.end(), out.begin());
    std::vector<Glyph> added;
    for (std::size_t i = 0; i < list.size(); ++i) {
        const std::uint32_t idx = list[i] - 0xAC00u;
        const unsigned l = idx / 588, v = (idx % 588) / 28, t = idx % 28;
        const Glyph* parts[3] = { Find(glyphs, std::uint16_t(0x1100 + l)), Find(glyphs, std::uint16_t(0x1161 + v)),
                                  t ? Find(glyphs, std::uint16_t(0x11A7 + t)) : nullptr };
        const unsigned gx = 1 + unsigned(i % cols) * kPitch, gy = h + 1 + unsigned(i / cols) * kPitch;
        Compose(rgba, w, h, out, w, gx, gy, parts);
        added.push_back({std::uint16_t(list[i]), std::uint16_t(gx), std::uint16_t(gy), std::uint16_t(kCell)});
    }
    glyphs.insert(glyphs.end(), added.begin(), added.end());
    std::sort(glyphs.begin(), glyphs.end(), [](const Glyph& a, const Glyph& b) { return a.ch < b.ch; });
    rgba = std::move(out);
    h = nh;
    return true;
}

}  // namespace krfont
