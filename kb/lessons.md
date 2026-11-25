# Lessons learned (satu entri per insiden: tanggal, kejadian, penyebab, aturan baru)

## 2026-11-24 · Kalimat produksi ikut terbaca di VO (WH Bagration Part 2 v1)
- Kejadian: "Next: Minsk." dan "Bobruisk. June, nineteen forty-four." terbaca sebagai narasi.
- Penyebab: teks kartu/produksi masuk ke naskah yang dikirim ke ElevenLabs; tidak ada pencocokan transkrip dengan naskah.
- Aturan baru: gerbang QG3 membandingkan transkrip VO dengan naskah (modul `gate-qg3-vo-check`, F1).

## 2026-11-25 · Kredit suara habis sebelum Tier B Part 2 (WH)
- Kejadian: sisa 308 dari 17.169; Tier B (891 karakter) batal; ±900 kredit terpakai di luar Part 2 tanpa tercatat.
- Penyebab: kredit tidak punya anggaran per brand dan tidak dicek sebelum produksi.
- Aturan baru: `registry/budget.json` + `./senator status` tampil sisa kredit; Planner menghitung kebutuhan sebelum menyetujui generate.

## 2026-11-24 · Still AI diam dibuka sebagai opening membuat penonton skip (WH Part 2)
- Aturan baru: opening = 2 detik gelap lalu peta; gambar AI tidak di awal; adegan pakai animasi vektor (Diorama) bukan still.
