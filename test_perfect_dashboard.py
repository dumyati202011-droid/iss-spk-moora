import subprocess
import os

def generate_svg(line_type="straight"):
    # line_type: "straight", "curved", or "outer"
    
    if line_type == "straight":
        # Straight line from Super Admin to Dashboard
        admin_dash_line = '<line x1="200" y1="248" x2="415" y2="685" stroke="#111827" stroke-width="1.8" />'
    elif line_type == "outer":
        # Outer line routed along X=260
        admin_dash_line = '<polyline points="200,248 275,248 275,675 415,685" fill="none" stroke="#111827" stroke-width="1.8" />'
    else:
        # Smooth bezier curve routing
        admin_dash_line = '<path d="M 200 248 Q 280 460 415 685" fill="none" stroke="#111827" stroke-width="1.8" />'

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1020" width="1600" height="1020" style="background:#ffffff; font-family:'Segoe UI', Helvetica, Arial, sans-serif;">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f3f5" stroke-width="0.8"/>
    </pattern>
    <marker id="openArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5" fill="none" stroke="#000000" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>

  <rect width="1600" height="1020" fill="url(#grid)" />
  <rect x="15" y="15" width="1570" height="990" fill="none" stroke="#d0d5dd" stroke-width="1.2" />

  <g text-anchor="middle">
    <text x="800" y="52" font-family="'Times New Roman', Georgia, serif" font-size="23" font-weight="bold" letter-spacing="1.5" fill="#111827">USE CASE DIAGRAM</text>
    <text x="800" y="78" font-family="'Times New Roman', Georgia, serif" font-size="13.5" font-style="italic" fill="#4b5563">Sistem Pendukung Keputusan Penilaian Kinerja Karyawan Metode MOORA - PT ISS Indonesia Site Prodia</text>
  </g>

  <!-- System Boundary Box -->
  <rect x="330" y="110" width="1210" height="860" rx="8" fill="#ffffff" stroke="#111827" stroke-width="2" />
  <line x1="330" y1="152" x2="1540" y2="152" stroke="#111827" stroke-width="1.5" />
  <text x="935" y="137" text-anchor="middle" font-size="15" font-weight="bold" fill="#111827" letter-spacing="0.5">Sistem Aplikasi SPK MOORA ISS Prodia</text>

  <!-- ACTORS -->
  <!-- 1. Super Admin (Agung Permadi) -->
  <g id="actor-admin">
    <circle cx="160" cy="195" r="22" fill="#ffffff" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="217" x2="160" y2="270" stroke="#111827" stroke-width="2.2" />
    <line x1="120" y1="238" x2="200" y2="238" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="270" x2="130" y2="320" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="270" x2="190" y2="320" stroke="#111827" stroke-width="2.2" />
    <text x="160" y="344" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#111827">Super Admin</text>
    <text x="160" y="362" text-anchor="middle" font-size="12" font-weight="500" fill="#4b5563">(Agung Permadi - HRD)</text>
  </g>

  <!-- 2. Site Supervisor (Septo Aribowo) -->
  <g id="actor-spv">
    <circle cx="160" cy="460" r="22" fill="#ffffff" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="482" x2="160" y2="535" stroke="#111827" stroke-width="2.2" />
    <line x1="120" y1="503" x2="200" y2="503" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="535" x2="130" y2="585" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="535" x2="190" y2="585" stroke="#111827" stroke-width="2.2" />
    <text x="160" y="609" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#111827">Site Supervisor</text>
    <text x="160" y="627" text-anchor="middle" font-size="12" font-weight="500" fill="#4b5563">(Septo Aribowo - ISS)</text>
  </g>

  <!-- 3. Branch Manager (Siska Darmayanti) -->
  <g id="actor-manager">
    <circle cx="160" cy="715" r="22" fill="#ffffff" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="737" x2="160" y2="790" stroke="#111827" stroke-width="2.2" />
    <line x1="120" y1="758" x2="200" y2="758" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="790" x2="130" y2="840" stroke="#111827" stroke-width="2.2" />
    <line x1="160" y1="790" x2="190" y2="840" stroke="#111827" stroke-width="2.2" />
    <text x="160" y="864" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#111827">Branch Manager</text>
    <text x="160" y="882" text-anchor="middle" font-size="12" font-weight="500" fill="#4b5563">(Siska Darmayanti - Prodia)</text>
  </g>

  <!-- ASSOCIATIONS -->
  <g stroke="#111827" stroke-width="1.8">
    <!-- Super Admin connects to UC 1 & UC 2 -->
    <line x1="200" y1="238" x2="415" y2="205" />
    <line x1="200" y1="238" x2="415" y2="315" />
    {admin_dash_line}

    <!-- Site Supervisor connects to UC 3, 4, & 5 -->
    <line x1="200" y1="503" x2="415" y2="445" />
    <line x1="200" y1="503" x2="415" y2="555" />
    <line x1="200" y1="503" x2="415" y2="690" />

    <!-- Branch Manager connects to UC 5 & 6 -->
    <line x1="200" y1="758" x2="415" y2="695" />
    <line x1="200" y1="758" x2="415" y2="815" />
  </g>

  <!-- COLUMN 1: PRIMARY USE CASES -->
  <g id="uc-1">
    <ellipse cx="585" cy="205" rx="170" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="210" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Mengelola Data Karyawan</text>
  </g>
  <g id="uc-2">
    <ellipse cx="585" cy="315" rx="170" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="320" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Mengatur Kriteria &amp; Bobot</text>
  </g>
  <g id="uc-3">
    <ellipse cx="585" cy="445" rx="170" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="450" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Input Skor Penilaian Kinerja</text>
  </g>
  <g id="uc-4">
    <ellipse cx="585" cy="555" rx="170" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="560" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Sinkronisasi &amp; Komputasi MOORA</text>
  </g>
  <g id="uc-5">
    <ellipse cx="585" cy="690" rx="170" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="695" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Melihat Dashboard &amp; Klasemen</text>
  </g>
  <g id="uc-6">
    <ellipse cx="585" cy="815" rx="170" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="585" y="820" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Mencetak SK &amp; Berita Acara</text>
  </g>

  <!-- COLUMN 2: SECONDARY USE CASES -->
  <g id="uc-1-inc">
    <ellipse cx="1270" cy="205" rx="180" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="210" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Validasi Duplikasi NIP</text>
  </g>
  <g id="uc-2-inc">
    <ellipse cx="1270" cy="315" rx="180" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="320" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Validasi Total Bobot 100%</text>
  </g>
  <g id="uc-3-inc">
    <ellipse cx="1270" cy="445" rx="180" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="450" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Validasi Rentang Nilai (1 - 100)</text>
  </g>
  <g id="uc-4-inc">
    <ellipse cx="1270" cy="555" rx="180" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="560" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Normalisasi &amp; Optimasi Multiobjektif Yi</text>
  </g>
  <g id="uc-5-ext">
    <ellipse cx="1270" cy="690" rx="180" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="695" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Filter Divisi CS &amp; Messenger</text>
  </g>
  <g id="uc-6-inc">
    <ellipse cx="1270" cy="815" rx="180" ry="29" fill="#ffffff" stroke="#111827" stroke-width="2" />
    <text x="1270" y="820" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#111827">Export PDF Dokumen Resmi</text>
  </g>

  <!-- HORIZONTAL CONNECTORS -->
  <line x1="755" y1="205" x2="1086" y2="205" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="196" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

  <line x1="755" y1="315" x2="1086" y2="315" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="306" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

  <line x1="755" y1="445" x2="1086" y2="445" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="436" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

  <line x1="755" y1="555" x2="1086" y2="555" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="546" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>

  <line x1="1090" y1="690" x2="759" y2="690" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="681" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;extend&gt;&gt;</text>

  <line x1="755" y1="815" x2="1086" y2="815" stroke="#111827" stroke-width="1.6" stroke-dasharray="6,4" marker-end="url(#openArrow)" />
  <text x="922" y="806" text-anchor="middle" font-size="12" font-style="italic" font-weight="600" fill="#111827">&lt;&lt;include&gt;&gt;</text>
</svg>'''
    return svg

# Generate straight line version
svg_straight = generate_svg("straight")
with open('public/diagrams/use_case_diagram.svg', 'w') as f:
    f.write(svg_straight)

html = f'''<!DOCTYPE html><html><body style="margin:0;padding:0;background:#fff;display:flex;justify-content:center;">{svg_straight}</body></html>'''
with open('public/diagrams/use_case_diagram.html', 'w') as f:
    f.write(html)

cmd = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '--headless',
    '--disable-gpu',
    '--window-size=1600,1020',
    '--screenshot=public/diagrams/use_case_diagram.png',
    f'file://{os.path.abspath("public/diagrams/use_case_diagram.html")}'
]
subprocess.run(cmd, check=True)
print("Updated use_case_diagram.png with Super Admin connecting to Dashboard!")
