# SENATOR MEDIA WORKS: Master Architecture v0.2 (disetujui Nanda 25 Nov 2026, F0 berjalan)

Infrastruktur produksi media digital dan content creator di dalam AI Senator.
Status: **DISETUJUI**. F0 sudah dibangun (registry, CLI `senator`, 3 agent). Prinsip pemilik: BUILD TO PRODUCE, PRODUCE TO MONETIZE.

- Pemilik / Executive Producer: Nanda (Orca)
- Arsitek & orkestrator: Claude
- Tanggal: 25 Nov 2026
- Repo induk (HQ): `orca-gtb/ai-senator-workspace`
- Lingkup: **CONTENT CREATION & SOCIAL MEDIA INDUSTRY saja.** Trading, investasi, dan operasional bisnis umum di luar lingkup.

---

## 0. Ringkasan satu paragraf

Senator Media Works (SMW) adalah "pabrik media" berbasis repo: satu **HQ** (repo ini) memegang rencana, standar, registry, agent, dan dashboard; tiap brand media adalah **Studio** (repo produksi sendiri, misalnya `ww-template` untuk World History dan `sang-kronika-studio`) yang tersambung ke HQ lewat antarmuka standar. Produksi berjalan di satu jalur dengan **7 gerbang mutu** (QG0–QG6). Empat pendekatan negara dipakai sebagai **lensa desain** yang masing-masing memiliki satu lapisan sistem: AS memegang cerita, kemasan, dan uang; Jerman memegang standar dan mutu; Soviet memegang perencanaan dan alokasi sumber daya; Tiongkok memegang distribusi, kecepatan iterasi, dan commerce.

---

## 1. Kondisi nyata yang jadi batas desain

| Fakta | Angka / status | Akibat ke desain |
|---|---|---|
| Tenaga manusia | 1 orang (Nanda) | Semua divisi diisi agent; manusia hanya di 2 gerbang wajib (QG0 greenlight, QG5 publish) |
| Target terdekat | YPP World History, akhir Des 2026 (±36 hari lagi) | Fase 1 harus langsung melayani produksi WH, bukan proyek infrastruktur yang berdiri sendiri |
| Basis channel (17 Nov) | 75 subs, ±97,5 jam tonton 12 bln | Analytics dan audience development masuk sejak Fase 2 |
| Kredit suara | 308 tersisa dari 17.169 (25 Nov); reset ±22 Des | Kredit diperlakukan sebagai anggaran terpusat (lensa Soviet), dengan alokasi per brand |
| Mesin produksi yang sudah terbukti | Remotion (peta, Diorama 2.5D), mixer ffmpeg, timeline builder, skill hook/storytelling | Dijadikan "engine" bersama, bukan ditulis ulang |
| Risiko ritme kerja | Rentan burnout kalau target kaku | Perencanaan memakai kapasitas harian bergulir, bukan kuota dan deadline keras |

**Teguran jujur sebelum mulai:** membangun infrastruktur bisa berubah jadi cara halus menunda upload. Aturan yang aku pasang di desain ini: **tidak ada fase infrastruktur yang menghentikan jadwal upload World History.** Part 2 v3 sudah siap upload sekarang, sebelum infrastruktur ini selesai.

---

## 2. Empat lensa negara: apa yang diambil, apa yang ditolak

| Lensa | Prinsip yang diambil | Wujud konkret di SMW | Yang sengaja **ditolak** |
|---|---|---|---|
| **AS** (Hollywood, creator economy) | Pipeline development → pre-pro → produksi → post → distribusi; *greenlight*; showrunner; *packaging first* (judul dan thumbnail sebelum produksi); berpikir seri/franchise; monetisasi berlapis | Gerbang QG0 Greenlight dengan scorecard; agent Showrunner; brief kemasan wajib sebelum naskah; seri (misalnya Bagration 4 part) dikelola sebagai satu IP | Anggaran besar dan kru panjang; clickbait yang tidak sesuai isi (merusak AVD dan kepercayaan) |
| **Jerman** (Industrie 4.0, DIN, Qualitätssicherung) | Standar tertulis per format; toleransi terukur; QA bergerbang; modul yang bisa dipakai ulang; analisis akar masalah | Dokumen *Format-Norm* (misalnya `WH-LF-01`); checklist gerbang dengan angka (LUFS −16 ± 1, VO di atas latar ≥ 12 dB, 100% klaim berstatus); laporan insiden format 8D; engine bersama (mapkit, Diorama, mixer) | Birokrasi dokumen yang tidak dipakai; standar yang tidak bisa diukur mesin |
| **Soviet** (Gosplan, pembagian kerja, standardisasi massal) | Perencanaan terpusat; pembagian tugas yang jelas; komponen standar yang bisa ditukar; alokasi sumber daya dari satu pusat | *Planning Office*: satu slate untuk semua brand; anggaran kredit ElevenLabs/render dialokasikan per brand; template dan library aset standar; jalur turunan Shorts semi-massal | **Kuota berbasis jumlah** (memicu konten massal bertemplat, melanggar kebijakan *inauthentic content* YouTube, dan menurunkan mutu); rencana kaku jangka panjang; target yang tidak boleh diubah meski data berubah |
| **Tiongkok** (Douyin/TikTok, MCN, social commerce, livestream) | Model MCN (satu pusat mengelola banyak akun/brand); radar tren cepat; iterasi pendek berbasis data; *content + commerce* dalam satu siklus; matriks akun per niche | Intelligence Bureau dengan radar tren harian; eksperimen A/B satu variabel; divisi Commerce untuk affiliate (TikTok Shop, Shopee) dan produk; tiap brand punya identitas sendiri | Akun duplikat/spam yang mengunggah konten sama di banyak akun (dilarang platform); livestream sebelum ada wajah/host dan stok produk (ditunda ke Fase 4) |

Aturan integrasi: **setiap lensa memiliki satu lapisan, dan tiap lapisan diawasi lensa lain.** Contoh: rencana dari Planning Office (Soviet) wajib lolos standar mutu (Jerman); kecepatan iterasi tren (Tiongkok) tetap lewat greenlight dan kemasan (AS).

---

## 3. Master architecture: 6 lapisan

```
L0  GOVERNANCE        Senate Office: Nanda (Executive Producer) · kebijakan · gerbang manusia (QG0, QG5)
L1  CONTROL PLANE     Showrunner (orkestrator) · Planning Office (slate, kapasitas, anggaran) · Registry
L2  PRODUCTION PLANE  11 departemen di satu jalur bergerbang QG0–QG6
L3  PLATFORM SERVICES Engines (mapkit, Diorama, mixer, timeline) · Tool adapters (ElevenLabs, vidIQ, Zernio, Canva,
                      Google Drive/Sheets/Calendar, Remotion, ffmpeg, Playwright, web research) · Skill library
L4  DATA & KNOWLEDGE  Registry JSON · Asset store (master di Drive, manifest di git) · Knowledge base · Source ledger ·
                      Metrics warehouse (snapshot JSON/CSV)
L5  OBSERVABILITY     Dashboard · laporan terjadwal · alarm (kredit hampir habis, gerbang gagal, video turun performa)
```

### Topologi repo: HQ + Studio

| Repo | Peran | Isi |
|---|---|---|
| `ai-senator-workspace` | **HQ** (control plane) | standar, SOP, agent, registry semua brand, data metrik, dashboard, CLI `senator` |
| `ww-template` | **Studio** World History | engine Remotion, proyek video, VO, mixer |
| `sang-kronika-studio` | **Studio** Sang Kronika | sama, dengan identitas brand sendiri |
| (nanti) `orca-etsy`, studio baru | **Studio** tambahan | dipasang dengan template studio yang sama |

Tiap studio wajib punya `studio.json` (identitas brand, format, standar yang dipakai) dan struktur folder proyek standar. Dengan begitu HQ bisa membaca semua studio dengan cara yang sama (lensa Soviet: komponen yang bisa ditukar).

---

## 4. Struktur organisasi

```
SENATE OFFICE ─ Nanda (Executive Producer, keputusan akhir QG0 & QG5)
│
└─ SHOWRUNNER (Claude, orkestrator lintas departemen)
   ├─ D1  Intelligence Bureau ............ riset tren, kata kunci, sumber sejarah
   ├─ D2  Development & Story ............ cerita, naskah, hook, kemasan
   ├─ D3  Planning Office ................ slate, kapasitas, anggaran kredit
   ├─ D4  Voice & Audio .................. VO, sound design, mix
   ├─ D5  Visual & Motion ................ peta, animasi, aset visual, brief thumbnail
   ├─ D6  Assembly & Render .............. timeline, render, versi
   ├─ D7  Quality Assurance .............. gerbang mutu, kepatuhan kebijakan, 8D
   ├─ D8  Distribution & Growth .......... metadata, jadwal, turunan Shorts/Reels/TikTok, komunitas
   ├─ D9  Analytics & Performance ........ metrik, eksperimen, laporan
   ├─ D10 Monetization & BizDev .......... YPP, affiliate, sponsor, produk, commerce
   └─ D11 Archive & Knowledge ............ registry aset, knowledge base, lessons learned
```

### Peta departemen dan agent (18 agent: Showrunner + 17)

| Dept | Agent | Lensa | Tanggung jawab | Output utama | Tool |
|---|---|---|---|---|---|
| L1 | **Showrunner** | AS | memecah perintah jadi tugas, memanggil agent, menjaga gerbang | status proyek | semua |
| D1 | **Trend Scout** | CN | radar tren, outlier, kata kunci per brand | `intel/trends-YYYY-WW.md` | vidIQ, WebSearch |
| D1 | **Research Analyst** | DE | riset sumber, kronologi, angka | dossier riset | WebSearch/WebFetch, (Firecrawl) |
| D1 | **Fact Auditor** | DE | status tiap klaim V/K/D/? di source ledger | `sources.json` | ledger |
| D2 | **Story Architect** | AS | tesis, struktur, hook, retensi | outline + hook | skill hook/storytelling |
| D2 | **Scriptwriter** | AS | naskah VO, teks layar | `script.md`, `vo.json` | skill copywriting, anti-ai-writing |
| D2 | **Packaging Lead** | AS | judul, brief thumbnail, konsep sebelum produksi | `package.md` | vidIQ score title |
| D3 | **Production Planner** | SU | slate lintas brand, kapasitas harian, anggaran kredit/render | `plan/slate.json`, `plan/budget.json` | Calendar, registry |
| D4 | **Voice Director** | DE | generate VO, cek teks produksi bocor, 1 take | `vo/*.mp3` + manifest | ElevenLabs |
| D4 | **Sound Engineer** | DE | SFX, musik, mix, loudness | `audio.wav` + laporan QC | ffmpeg, mixer |
| D5 | **Cartographer & Motion Designer** | DE/AS | peta, Diorama 2.5D, motion | komposisi Remotion | Remotion, skill motion-design |
| D5 | **Visual Asset Producer** | AS | brief gambar (Angie/Dio), thumbnail brief, Canva | aset + lisensi | Canva, Unsplash |
| D6 | **Assembly Editor** | SU | timeline, render, versi | `out/*.mp4` | Remotion, ffmpeg |
| D7 | **QA Inspector** | DE | gerbang QG1–QG4, kebijakan (inauthentic, AI disclosure, hak cipta) | laporan gerbang, 8D | script QC |
| D8 | **Distribution Manager** | CN | metadata, jadwal, turunan Shorts/Reels/TikTok, draf balasan komentar (tidak dikirim tanpa izin) | paket publish | Zernio, vidIQ |
| D9 | **Performance Analyst** | DE/CN | snapshot metrik 48 jam / 7 / 28 hari, eksperimen satu variabel | `metrics/*.json`, laporan | vidIQ, Studio |
| D10 | **Revenue Strategist** | AS/CN | jalur uang per brand, affiliate, sponsor, commerce | `biz/*.md` | – |
| D11 | **Archivist** | SU/DE | registry aset, KB, lessons learned | `kb/`, `registry/assets.json` | Drive, git |

Catatan: Showrunner dan 17 agent lain diimplementasikan sebagai subagent Claude Code (`.claude/agents/*.md`) dengan tool dibatasi sesuai tugas. Tidak semua dibangun sekaligus (lihat bagian 10).

---

## 5. Production pipeline dan gerbang mutu

| Tahap | Departemen | Masuk | Keluar | Gerbang | Kriteria lolos (contoh WH long-form) | Penyetuju |
|---|---|---|---|---|---|---|
| S0 Intake | D1, D3 | ide, tren, seri | kartu proyek | **QG0 Greenlight** | skor ≥ 7/10 (dampak audiens, kecocokan brand, potensi search, biaya kredit); slot kapasitas ada | **Nanda** |
| S1 Riset | D1 | kartu | dossier + source ledger | **QG1 Fakta** | 100% klaim punya status; klaim inti V/K; angka sensitif diberi kata "estimated/one account" | QA Inspector |
| S2 Cerita | D2 | dossier | outline, hook, naskah | **QG2 Naskah** | hook 0–5 dtk lolos skill hook; ada tesis sendiri; tidak ada kalimat produksi di teks VO; durasi target dihitung (WH ≥ 8:00) | QA Inspector |
| S3 Kemasan | D2 | naskah | judul + brief thumbnail | (bagian QG2) | judul ≤ 70 kar., kata kunci di 40 kar. pertama, sesuai isi | Packaging Lead |
| S4 Suara | D4 | `vo.json` | VO mp3 | **QG3 Audio** | kredit cukup sebelum generate; transkrip VO = naskah; tidak ada kalimat liar | QA Inspector |
| S5 Visual | D5 | naskah, timeline | adegan Remotion, aset | – | aturan brand (tanpa simbol terlarang, label ilustrasi) | – |
| S6 Rakit | D6, D4 | semua aset | master mp4 | **QG4 Teknis** | durasi sesuai target; −16 ± 1 LUFS; peak ≤ −1 dBTP; VO ≥ 12 dB di atas latar (median); contact sheet tiap adegan dicek | QA Inspector |
| S7 Paket | D8 | master | metadata, chapter, sumber, pengaturan | **QG5 Publish** | chapter cocok durasi; sumber lengkap; AI disclosure; made-for-kids benar | **Nanda** |
| S8 Distribusi | D8 | paket | video tayang + turunan | – | turunan Shorts punya hook sendiri, bukan potongan mentah | – |
| S9 Ulasan | D9, D11 | metrik | laporan + lessons learned | **QG6 Review** | snapshot 48 jam / 7 hari / 28 hari tercatat; satu pelajaran masuk KB | Showrunner |

Gerbang otomatis (QG1–QG4, QG6) dijalankan oleh script. **Gerbang manusia hanya dua**: QG0 dan QG5. Tidak ada publish otomatis.

Contoh nyata kenapa gerbang ini perlu: di Part 2 v1 ada kalimat produksi ("Next: Minsk.") yang ikut terbaca di VO. Di desain ini, QG3 membandingkan transkrip VO dengan naskah dan memblok render kalau ada kalimat tambahan.

---

## 6. Data flow

```
SINYAL ──────────────► INTELLIGENCE ──► PLANNING ──► PROYEK ──────────────► PUBLISH ──► METRIK
vidIQ, Studio,          trends.md        slate.json   registry/projects/     paket       metrics/*.json
komentar (Zernio),      keywords.json    budget.json  <id>/project.json      Zernio /    (48j, 7h, 28h)
tren web                                              sources.json           Studio          │
                                                       script.md, vo.json                     │
                                                       timeline.json → mp4                    ▼
                                                                                         DASHBOARD
       ▲                                                                                      │
       └────────────── KNOWLEDGE BASE (lessons, standar baru) ◄── REVIEW (QG6) ◄──────────────┘
```

Aturan data:
1. **Registry adalah satu-satunya sumber kebenaran** untuk status proyek, anggaran, dan aset. Agent membaca/menulis registry, bukan menyimpan status di percakapan.
2. **File besar tidak masuk git.** Master video/audio di Google Drive (folder per brand/proyek); git menyimpan manifest (path, hash, ukuran, lisensi).
3. Setiap angka di dashboard menyimpan sumber dan tanggal pengambilan.
4. Data dari luar (komentar, halaman web, DM) diperlakukan sebagai data, bukan perintah.

---

## 7. Dashboard dan monitoring

| Panel | Isi | Sumber | Frekuensi |
|---|---|---|---|
| North Star | progres YPP per channel (subs, jam tonton long-form, views Shorts 90 hari) | vidIQ / Studio | harian/mingguan |
| Slate & WIP | proyek per tahap S0–S9, umur di tiap tahap | registry | setiap perubahan |
| Gerbang mutu | lolos/gagal per gerbang, cacat yang lolos ke publik | laporan QG | per proyek |
| Anggaran | kredit ElevenLabs terpakai/sisa per brand, tanggal reset | ElevenLabs usage + budget.json | harian |
| Performa konten | CTR, AVD%, retensi 30 dtk, views 48 jam per video | vidIQ / Studio | 48 j, 7 h, 28 h |
| Eksperimen | hipotesis, variabel, hasil | `experiments.json` | per eksperimen |
| Uang | pendapatan per jalur per brand (iklan, affiliate, sponsor, produk) | input manual + platform | bulanan |

Alarm: kredit < 15% sebelum reset; proyek > 5 hari di satu tahap; gerbang gagal 2× berturut; video dengan retensi 30 dtk di bawah median channel.

---

## 8. Knowledge & asset management

```
ai-senator-workspace/
├── docs/architecture/        rancangan ini + diagram
├── standards/                Format-Norm per format (WH-LF-01, WH-SH-01, SK-REEL-01 ...)
├── sops/                     SOP-00 ... SOP-12 (cara kerja tiap tahap)
├── registry/                 properties.json, projects/, assets.json, budget.json (+ JSON Schema)
├── intel/                    tren dan kata kunci mingguan
├── metrics/                  snapshot per video dan per channel
├── kb/                       lessons learned, style bible per brand, glossary
├── tools/senator/            CLI: project new, gate check, budget, dash build
├── dashboards/               sumber dashboard
└── .claude/agents|skills|hooks
```

SOP yang direncanakan: SOP-00 Greenlight · SOP-01 Riset & source ledger · SOP-02 Hook & naskah · SOP-03 Kemasan · SOP-04 Produksi VO · SOP-05 Peta & motion · SOP-06 Rakit & render · SOP-07 Mix & loudness · SOP-08 QA & 8D · SOP-09 Publish & metadata · SOP-10 Turunan short-form · SOP-11 Review & lessons learned · SOP-12 Anggaran kredit.

---

## 9. Peta tool per divisi

| Divisi | Tool | Status sekarang |
|---|---|---|
| Intelligence | vidIQ MCP, WebSearch/WebFetch | tersambung |
| Intelligence | Firecrawl | butuh API key |
| Story | skill wtf-hook-akademi, viral-hooks, art-of-storytelling, storytelling, dumbify, copywriting, anti-ai-writing | terpasang di `ww-template`, akan dipusatkan di HQ |
| Voice | ElevenLabs MCP | tersambung; kredit 308 tersisa; rencana naik ke Creator |
| Visual | Remotion + mapkit + Diorama, Canva, Unsplash; Angie/Dio (manusia-dalam-loop untuk gambar AI dan thumbnail) | tersedia |
| Assembly | Remotion render, ffmpeg | tersedia di container |
| QA | script QC (loudness, VO/latar, contact sheet), Playwright | sebagian ada di `ww-template`, akan dijadikan modul |
| Distribution | Zernio MCP | **perlu login ulang** (sesi ini minta autentikasi) |
| Analytics | vidIQ, YouTube Studio (manual) | tersambung |
| Planning | Google Calendar, Sheets, Drive | tersambung |

**ElevenLabs Creator Plan:** layak dibeli setelah Fase 1 jalan, karena kredit adalah hambatan produksi yang terbukti (Part 2 Tier B gagal karena kredit). Detail kuota dan harga dicek di halaman harga ElevenLabs saat membeli; anggaran per brand diatur di `budget.json` (SOP-12) supaya World History tetap prioritas.

---

## 10. Rencana implementasi bertahap

| Fase | Isi | Uji modul (definition of done) | Tidak menghentikan |
|---|---|---|---|
| **F0 Fondasi** | struktur folder HQ, JSON Schema registry, `studio.json` untuk WH & SK, CLI `senator` (project new, validate), CLAUDE.md HQ | `senator validate` lolos di 2 studio; satu proyek nyata (Bagration Part 3) terdaftar | upload Part 2 |
| **F1 Jalur produksi WH** | Format-Norm WH-LF-01, SOP-00..09, agent D1/D2/D4/D7, gate checker QG1–QG4 | Bagration Part 3 lewat semua gerbang dengan laporan otomatis | jadwal WH |
| **F2 Distribusi & analytics** | Distribution Manager, Performance Analyst, snapshot metrik, dashboard v1, laporan mingguan terjadwal | dashboard menampilkan data nyata dengan sumber dan tanggal | – |
| **F3 Multi-brand (MCN)** | Sang Kronika masuk standar, Planning Office lintas brand, anggaran kredit per brand, jalur turunan short-form | 2 brand di satu slate tanpa bentrok kredit | – |
| **F4 Commerce** | Revenue Strategist, affiliate/social commerce, produk digital, eksplorasi livestream | satu jalur commerce menghasilkan transaksi tercatat | – |

---

## 11. Keputusan yang perlu disetujui Nanda

1. **Nama sistem:** "Senator Media Works" (SMW), atau nama lain.
2. **Topologi HQ + Studio:** HQ di repo ini, studio tetap di repo masing-masing.
3. **Dua gerbang manusia saja (QG0 dan QG5)**, sisanya otomatis.
4. **Master file besar di Google Drive**, git hanya manifest.
5. **Urutan fase F0 → F4**, dengan F0+F1 dikerjakan memakai Bagration Part 3 sebagai proyek uji nyata.
6. **Penolakan eksplisit:** tanpa kuota berbasis jumlah, tanpa akun duplikat, tanpa publish otomatis.
