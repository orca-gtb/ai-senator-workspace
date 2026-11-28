# Odysseus (infrastruktur AI workspace self-hosted)

Sumber: https://github.com/odysseus-dev/odysseus · lisensi **AGPL-3.0** · terpasang sebagai **git submodule** di `infra/odysseus`, dipin ke cabang `main` pada commit `9d0d372` (HARNESS_VERSION 0.20.19, dipasang 28 Nov 2026).

## Apa ini
Workspace AI yang dijalankan sendiri (self-hosted): chat dan agen dengan model lokal atau API, riset mendalam, perbandingan model, dokumen, email (IMAP/SMTP), catatan, tugas, kalender (CalDAV), dan "Cookbook" untuk memilih dan menjalankan model lokal sesuai perangkat keras. Berjalan lewat Docker Compose (Odysseus, ChromaDB, SearXNG, ntfy) dan membuka antarmuka web di `http://localhost:7011`.

## Status: terpasang di repo, BELUM dijalankan
- Yang dilakukan: kode ditaut sebagai submodule dan dipin ke satu commit. Tidak ada yang diunduh ke repo ini selain tautan.
- Yang belum: tidak dijalankan, tidak diuji, tidak ada kunci API atau data yang dimasukkan. Container cloud sesi Claude tidak cocok untuk ini (Docker tidak tersedia untuk layanan menetap, dan sesi bersifat sementara); alat ini baru berguna saat Nanda punya laptop atau server sendiri.
- Belum dinilai: apakah Odysseus benar-benar menggantikan atau melengkapi alur kerja AI Senator (ChatGPT, Gemini, Grok, Perplexity, DeepSeek, Claude). Itu perlu dicoba di laptop.

## Saat laptop sudah ada
```bash
git clone --recurse-submodules <url repo ai-senator-workspace>
# atau, bila sudah di-clone tanpa submodule:
git submodule update --init --depth 1 infra/odysseus
cd infra/odysseus
cp .env.example .env          # isi pengaturan; JANGAN di-commit
docker compose up -d --build  # butuh Docker; GPU opsional (docker-compose.gpu-nvidia.yml / gpu-amd.yml)
docker compose logs odysseus  # kata sandi admin pertama tercetak di sini
```
Buka `http://localhost:7011`. Model lokal butuh RAM/VRAM sesuai ukuran model; Cookbook memberi rekomendasi menurut perangkat keras. Di Mac Apple Silicon, Docker tidak bisa memakai GPU Metal (lihat `infra/odysseus/website/setup.md`).

## Keamanan (dari SECURITY.md milik Odysseus; baca sebelum dijalankan)
1. Biarkan `AUTH_ENABLED=true` dan `LOCALHOST_BYPASS=false` bila bisa diakses lewat jaringan.
2. Port bawaan hanya mendengarkan `127.0.0.1`. Jangan buka ke internet tanpa HTTPS dan lapisan akses (Tailscale, VPN, Cloudflare Access).
3. Layanan internal (ChromaDB, SearXNG, ntfy, Ollama) jangan dibuka ke luar.
4. Fitur shell, Python, baca/tulis berkas, email, MCP, dan token adalah fungsi admin yang berhak tinggi. Jangan beri akses ke akun lain.
5. Kunci API, `.env`, `data/`, dan basis data **tidak boleh masuk Git**. Repo ini sudah mengabaikan `infra/odysseus/.env` dan `infra/odysseus/data/` sebagai pengaman tambahan.
6. Hubungan dengan data trading: jangan menghubungkan akun broker, kunci bursa, atau email penting sebelum Nanda memahami fitur yang dipakai. Mulai dengan data tidak sensitif.

## Lisensi AGPL-3.0: yang perlu diingat (bukan nasihat hukum)
- Dipakai sendiri di laptop: bebas.
- Kode Odysseus tidak disalin ke repo ini, hanya ditaut, jadi repo ini tidak otomatis ikut berlisensi AGPL.
- Bila nanti Odysseus dimodifikasi dan dijalankan sebagai layanan yang diakses orang lain lewat jaringan, AGPL mewajibkan menawarkan kode sumber hasil modifikasi itu ke pengguna layanan. Tinjau ulang sebelum melakukannya.
- Fitur opsional "INSTALL_OPTIONAL" memuat PyMuPDF (AGPL juga).

## Merawat
```bash
git submodule update --remote infra/odysseus   # tarik main terbaru, lalu periksa perubahan
git add infra/odysseus && git commit -m "Perbarui pin Odysseus"
```
Cabang bawaan Odysseus (`dev`) mendapat perubahan lebih dulu dan lebih berisiko; pin di repo ini memakai `main`. Perbarui pin secara sengaja, bukan otomatis.

## Pertanyaan terbuka untuk Nanda
- Apa yang paling ingin dipakai dari Odysseus: pusat chat banyak model, riset mendalam, email/kalender terintegrasi, atau menjalankan model lokal?
- Apakah laptopnya nanti punya GPU? Itu menentukan model lokal apa yang masuk akal.
