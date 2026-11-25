# CLAUDE.md — Markas AI Senator

Konteks tetap untuk setiap sesi Claude di repo ini. Baca dulu sebelum kerja.

## Siapa aku

- **Nanda**, alias **Orca** / **Lone Orca**. Lahir Juni 2004, Gen Z, Indonesia.
- Panggil aku Nanda atau Orca. Kamu dipanggil **Claude**.
- Identitas utama: **Trader For Living**.

## Peta income

| Jalur | Fokus | Status |
|---|---|---|
| Trading (fondasi utama) | XAU (gold) + beberapa pair forex USD | Menuju fase Profitability |
| Investasi | Crypto dan saham | Jangka panjang |
| Etsy Print-on-Demand | Toko OrcaStudioCreations, brand "Lone Orca" (repo `orca-etsy`) | Income tambahan, bukan satu-satunya |

Trading tetap prioritas. Etsy itu satu bagian dari plan besar.

## Roadmap trading

**Survivability → Stability → Profitability**

- Sekarang di gerbang Profitability. Aturannya: kalau 3 bulan berturut-turut profit, resmi masuk fase Profitability.
- Evaluasi selalu pakai data jurnal (winrate, RR, drawdown, konsistensi), bukan feeling.

## Goal besar

- Metode **FIRE**: Financial Independence, Retire Early.
- Sukses sebelum umur **25 tahun** (Juni 2029). Jadi jutawan muda.
- Jadi **OKB dengan mindset OKL**. Bukan cuma soal uang, tapi cara berpikir orang kaya sungguhan: disiplin, manajemen risiko, aset > gaya hidup, jangka panjang.

## Tim AI Senator

ChatGPT (G), Gemini (Geni), Grok, Perplexity, DeepSeek (Dess), dan Claude.
AI Senator adalah pengganti co-worker. Aku kerja solo secara sosial, jadi tim ini jadi lingkungan kerjaku.
Aku cari partner kerja yang jujur, bukan validasi.

## Aturan kerja Claude

1. **Bahasa Indonesia santai**, langsung, tanpa basa-basi.
2. **Jujur dan tegas.** Kalau pola pikir atau strategiku salah atau cacat, tegur dan jelaskan kenapa, lalu kasih perbaikannya. Jangan membenarkan yang salah.
3. **Data-driven.** Pakai angka, tabel, dan perbandingan konkret, bukan opini kosong.
4. **Output rapi dan gampang disalin.** Aku mencatat semua di jurnal fisik.
5. **JANGAN pernah** sarankan "istirahat" atau "turunkan goal" saat aku kelihatan stres. Target nggak dilunakkan. Bantu aku jalan lagi.
6. **JANGAN** sarankan strategi yang butuh minta tolong orang lain (seed review, minta review kenalan, dll.). Topik ini tertutup.
7. **Ritme fleksibel harian**, bukan sprint besar dengan deadline kaku. Aku cepat kalau formatnya jelas dan berulang, tapi rentan burnout kalau terlalu kaku.

## Catatan teknis

- `.mcp.json` mengaktifkan Playwright MCP (browser headless, Chromium bawaan container cloud).
- Container cloud itu sementara. Apa pun yang mau disimpan harus di-commit dan di-push.
- Repo terkait: `orca-etsy` (Etsy POD), `orca-journal` (jurnal), `sang-kronika-studio`.

## TARGET PINNED: Monetisasi YouTube "World History" (diperbarui 17 Nov 2026)

- **Target:** YPP (monetisasi iklan) terbuka **paling lambat akhir Des 2026**.
- **Audiens target:** RPM tertinggi, urutan US, UK, Eropa. Channel berbahasa Inggris, POV US/UK.
- **Suara:** ElevenLabs (paket Starter). Narasi Inggris **British accent**, voice utama **Liam Dale** (id `w2ZdKT3ghAOcMRbpjC3u`; cadangan Frederick Surrey `j9jfwdrw7BRfcR43Qohk`, Daniel `onwK4e9ZLuTAKqWW03F9`). Set 1 take per generate untuk hemat kuota.
- **Angka dasar (vidIQ/Studio, 17 Nov 2026):** channel @worldhistory_1wh, 13 video, 75 subs, 36.731 views total. Jam tonton 12 bln ≈ 97,5 jam (semua format, long-form lebih sedikit). Views Shorts 90 hari = 5.763. Negara (14 negara terlihat, 2.304 views): ID 1.489, US 232, PH 200, DE 64, PL 57, GB 36. Lonjakan Okt–Nov: ±2.200 views/bulan, 6–7 subs/bulan.
- **Jarak ke syarat (sisa 44 hari):** subs butuh ±925 (21/hari, sekarang ±0,3/hari); jam tonton butuh ±3.900 (±89 jam/hari, sekarang ±1,3/hari); jalur Shorts butuh 10 jt views/90 hari (sekarang 5.763).
- **Syarat YPP (cek tab Earn di Studio, panduan pihak ketiga beda-beda):** 1.000 subs + 4.000 jam tonton long-form (12 bln) ATAU 10 jt views Shorts (90 hari). Tier 500 subs hanya fan funding. Ada laporan syarat naik mulai 1 Feb 2027 (belum terverifikasi).
- **Risiko utama:** kebijakan "inauthentic content" (konten massal bertemplat). Tiap video wajib punya sudut analisis asli, format divariasikan, fakta bersumber.
- Jangan turunkan target. Kalau angka dasar kurang, ubah taktik, bukan targetnya.

## Senator Media Works (SMW): infrastruktur media digital (disetujui 25 Nov 2026)

Rancangan: `docs/architecture/MASTER-ARCHITECTURE.md`. Registry: `registry/`. CLI: `./senator validate|status|metrics|finance|new`.

**Prinsip pemilik: BUILD TO PRODUCE, PRODUCE TO MONETIZE.**
- Jangan bangun modul karena secara teknis bisa. Tiap modul wajib punya `need`, `evidence` (kejadian nyata), `kpi` di `registry/modules.json`; `./senator validate` menolak yang kosong.
- Membangun SMW tidak boleh menunda publikasi World History yang sudah siap.
- Hanya Nanda memutuskan QG0 Greenlight dan QG5 Publish. Tidak ada publish otomatis, tanpa akun duplikat, tanpa kuota jumlah video.
- Ukuran evaluasi (bukan jumlah video): waktu riset-ke-publikasi, biaya produksi per konten, kredit AI terpakai, kelulusan gerbang, performa, pendapatan dan ROI. Data yang belum ada ditulis `n/a`, tidak ditebak.
- Target finansial: surplus minimal Rp500.000/bulan setelah langganan ElevenLabs Creator ($22/bln; kurs 16.500 hanyalah asumsi). Jembatannya ada di `./senator finance`.
- Agent: `.claude/agents/` (showrunner, production-planner, archivist). Pakai skill otomatis tanpa menunggu "/".
