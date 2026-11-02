import subprocess
import os

svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1140" width="1600" height="1140" style="background:#ffffff; font-family:'Segoe UI', Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f3f5" stroke-width="0.8"/>
    </pattern>
    <marker id="openArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5" fill="none" stroke="#000000" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <rect width="1600" height="1140" fill="url(#grid)" />
  <rect x="15" y="15" width="1570" height="1110" fill="none" stroke="#d0d5dd" stroke-width="1.2" />

  <g text-anchor="middle">
    <text x="800" y="48" font-family="'Times New Roman', Georgia, serif" font-size="23" font-weight="bold" letter-spacing="1.5" fill="#111827">USE CASE DIAGRAM</text>
    <text x="800" y="72" font-family="'Times New Roman', Georgia, serif" font-size="13.5" font-style="italic" fill="#4b5563">Sistem Pendukung Keputusan Penilaian Kinerja Karyawan Metode MOORA - PT ISS Indonesia Site Prodia</text>
  </g>

  <!-- System Boundary Box (7 Use Cases) -->
  <rect x="330" y="95" width="1210" height="990" rx="8" fill="#ffffff" stroke="#111827" stroke-width="2" />
  <line x1="330" y1="135" x2="1540" y2="135" stroke="#111827" stroke-width="1.5" />
  <text x="935" y="121" text-anchor="middle" font-size="15" font-weight="bold" fill="#111827" letter-spacing="0.5">Sistem Aplikasi SPK MOORA ISS Prodia</text>

  <!-- ==================== ACTORS (LEFT SIDE) ==================== -->
  
  <!-- ACTOR 1: SUPER ADMIN (Agung Permadi) at cy=310 -->
  <g id="actor-admin">
    <circle cx="160" cy="260" r="22" fill="#ffffff" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="282" x2="160" y2="335" stroke="#111827" stroke-width="2.2" />
    <line x1="120" y1="303" x2="200" y2="303" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="335" x2="130" y2="385" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="335" x2="190" y2="385" stroke="#111827" stroke-width="2.2" />
    <text x="160" y="409" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#111827">Super Admin</text>
    <text x="160" y="427" text-anchor="middle" font-size="12" font-weight="500" fill="#4b5563">(Agung Permadi - HRD)</text>
  </g>

  <!-- ACTOR 2: SITE SUPERVISOR (Septo Aribowo) at cy=590 -->
  <g id="actor-spv">
    <circle cx="160" cy="540" r="22" fill="#ffffff" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="562" x2="160" y2="615" stroke="#111827" stroke-width="2.2" />
    <line x1="120" y1="583" x2="200" y2="583" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="615" x2="130" y2="665" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="615" x2="190" y2="665" stroke="#111827" stroke-width="2.2" />
    <text x="160" y="689" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#111827">Site Supervisor</text>
    <text x="160" y="707" text-anchor="middle" font-size="12" font-weight="500" fill="#4b5563">(Septo Aribowo - ISS)</text>
  </g>

  <!-- ACTOR 3: BRANCH MANAGER (Siska Darmayanti) at cy=870 -->
  <g id="actor-manager">
    <circle cx="160" cy="820" r="22" fill="#ffffff" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="842" x2="160" y2="895" stroke="#111827" stroke-width="2.2" />
    <line x1="120" y1="863" x2="200" y2="863" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="895" x2="130" y2="945" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="895" x2="190" y2="945" stroke="#111827" stroke-width="2.2" />
    <text x="160" y="969" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#111827">Branch Manager</text>
    <text x="160" y="987" text-anchor="middle" font-size="12" font-weight="500" fill="#4b5563">(Siska Darmayanti - Prodia)</text>
  </g>

  <!-- ==================== ASSOCIATIONS ==================== -->
  <g stroke="#111827" stroke-width="1.8">
    <!-- Super Admin connects to UC 1 (Login), UC 2 (Karyawan), UC 3 (Kriteria), UC 6 (Dashboard) -->
    <line x1="200" y1="303" x2="415" y2="180" />
    <line x1="200" y1="303" x2="415" y2="295" />
    <line x1="200" y1="303" x2="415" y2="410" />
    <line x1="200" y1="303" x2="415" y2="755" />

    <!-- Site Supervisor connects to UC 1 (Login), UC 4 (Input Skor), UC 5 (MOORA), UC 6 (Dashboard) -->
    <line x1="200" y1="583" x2="415" y2="180" />
    <line x1="200" y1="583" x2="415" y2="525" />
    <line x1="200" y1="583" x2="415" y2="640" />
    <line x1="200" y1="583" x2="415" y2="755" />

    <!-- Branch Manager connects to UC 1 (Login), UC 6 (Dashboard), UC 7 (Cetak SK) -->
    <line x1="200" y1="863" x2="415" y2="180" />
    <line x1="200" y1="863" x2="415" y2="755" />
    <line x1="200" y1="863" x2="415" y2="870" />
  </g>

  <!-- ==================== COLUMN 1: PRIMARY USE CASES (CX = 585) ==================== -->
  <!-- UC-01: Login / Autentikasi Sistem (Y=180) -->
  <g id="uc-1">
    <ellipse cx="585" cy="180" rx="170" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="185" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Login / Autentikasi Sistem</text>
  </g>

  <!-- UC-02: Mengelola Data Karyawan (Y=295) -->
  <g id="uc-2">
    <ellipse cx="585" cy="295" rx="170" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="300" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Mengelola Data Karyawan</text>
  </g>

  <!-- UC-03: Mengatur Kriteria & Bobot (Y=410) -->
  <g id="uc-3">
    <ellipse cx="585" cy="410" rx="170" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="415" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Mengatur Kriteria &amp; Bobot</text>
  </g>

  <!-- UC-04: Input Skor Penilaian Kinerja (Y=525) -->
  <g id="uc-4">
    <ellipse cx="585" cy="525" rx="170" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="530" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Input Skor Penilaian Kinerja</text>
  </g>

  <!-- UC-05: Sinkronisasi & Komputasi MOORA (Y=640) -->
  <g id="uc-5">
    <ellipse cx="585" cy="640" rx="170" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="645" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Sinkronisasi &amp; Komputasi MOORA</text>
  </g>

  <!-- UC-06: Melihat Dashboard & Klasemen (Y=755) -->
  <g id="uc-6">
    <ellipse cx="585" cy="755" rx="170" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="760" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Melihat Dashboard &amp; Klasemen</text>
  </g>

  <!-- UC-07: Mencetak SK & Berita Acara (Y=870) -->
  <g id="uc-7">
    <ellipse cx="585" cy="870" rx="170" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="875" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Mencetak SK &amp; Berita Acara</text>
  </g>

  <!-- ==================== COLUMN 2: SECONDARY USE CASES (CX = 1270) ==================== -->
  <!-- UC-01 Include: Verifikasi Akun & Hak Akses (Y=180) -->
  <g id="uc-1-inc">
    <ellipse cx="1270" cy="180" rx="180" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="185" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Verifikasi Akun &amp; Hak Akses</text>
  </g>

  <!-- UC-02 Include: Validasi Duplikasi NIP (Y=295) -->
  <g id="uc-2-inc">
    <ellipse cx="1270" cy="295" rx="180" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="300" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Validasi Duplikasi NIP</text>
  </g>

  <!-- UC-03 Include: Validasi Total Bobot 100% (Y=410) -->
  <g id="uc-3-inc">
    <ellipse cx="1270" cy="410" rx="180" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="415" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Validasi Total Bobot 100%</text>
  </g>

  <!-- UC-04 Include: Validasi Rentang Nilai (1-100) (Y=525) -->
  <g id="uc-4-inc">
    <ellipse cx="1270" cy="525" rx="180" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="530" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Validasi Rentang Nilai (1 - 100)</text>
  </g>

  <!-- UC-05 Include: Normalisasi & Optimasi Multiobjektif Yi (Y=640) -->
  <g id="uc-5-inc">
    <ellipse cx="1270" cy="640" rx="180" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="645" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Normalisasi &amp; Optimasi Multiobjektif Yi</text>
  </g>

  <!-- UC-06 Extend: Filter Divisi CS & Messenger (Y=755) -->
  <g id="uc-6-ext">
    <ellipse cx="1270" cy="755" rx="180" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="760" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Filter Divisi CS &amp; Messenger</text>
  </g>

  <!-- UC-07 Include: Export PDF Dokumen Resmi (Y=870) -->
  <g id="uc-7-inc">
    <ellipse cx="1270" cy="870" rx="180" ry="28" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="875" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Export PDF Dokumen Resmi</text>
  </g>

  <!-- ==================== HORIZONTAL DEPENDENCY CONNECTORS (INCLUDE / EXTEND) ==================== -->
  <!-- Row 1: Include (Login -> Verifikasi) -->
  <line x1="755" y1="180" x2="1086" y2="180" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="171" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

  <!-- Row 2: Include (Karyawan -> NIP) -->
  <line x1="755" y1="295" x2="1086" y2="295" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="286" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

  <!-- Row 3: Include (Kriteria -> Bobot 100%) -->
  <line x1="755" y1="410" x2="1086" y2="410" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="401" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

  <!-- Row 4: Include (Input Skor -> Rentang 1-100) -->
  <line x1="755" y1="525" x2="1086" y2="525" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="516" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

  <!-- Row 5: Include (MOORA -> Normalisasi & Optimasi Yi) -->
  <line x1="755" y1="640" x2="1086" y2="640" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="631" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

  <!-- Row 6: Extend (Filter -> Dashboard) -->
  <line x1="1090" y1="755" x2="759" y2="755" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="746" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;extend&gt;&gt;</text>

  <!-- Row 7: Include (SK -> Export PDF) -->
  <line x1="755" y1="870" x2="1086" y2="870" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="861" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

</svg>'''

with open('public/diagrams/test_7_use_cases.svg', 'w') as f:
    f.write(svg_content)

html_content = f'''<!DOCTYPE html><html><body style="margin:0;padding:0;background:#fff;display:flex;justify-content:center;">{svg_content}</body></html>'''
with open('public/diagrams/test_7_use_cases.html', 'w') as f:
    f.write(html_content)

cmd = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless',
    '--disable-gpu',
    '--window-size=1600,1140',
    '--screenshot=public/diagrams/test_7_use_cases.png',
    f'file://{os.path.abspath("public/diagrams/test_7_use_cases.html")}'
]
subprocess.run(cmd, check=True)
print("Rendered test_7_use_cases.png successfully")
