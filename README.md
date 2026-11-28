# ai-senator-workspace

Markas sesi cloud Claude Code untuk tim AI Senator.

## Isi
- `CLAUDE.md` — konteks tetap: profil, roadmap, dan aturan kerja AI Senator.
- `.mcp.json` — Playwright MCP (browser otomatis). Pakai Chromium bawaan container cloud
  di `/opt/pw-browsers/chromium`, mode headless.

- `infra/odysseus` — submodule: Odysseus (AI workspace self-hosted, AGPL-3.0), dipin ke `main`. Belum dijalankan; panduan dan catatan keamanan di `infra/ODYSSEUS.md`.

## Cara pakai
Mulai sesi baru di claude.ai/code dan pilih repo ini. Playwright MCP langsung aktif.
