import subprocess, os

W, H = 1600, 960

def draw_actor(cx, cy, label, sublabel):
    return f'''  <!-- Actor: {label} -->
  <g id="actor-{label.lower().replace(' ', '-')}">
    <circle cx="{cx}" cy="{cy}" r="28" fill="#ffffff" stroke="#000000" stroke-width="2.0"/>
    <line x1="{cx}" y1="{cy + 28}" x2="{cx}" y2="{cy + 105}" stroke="#000000" stroke-width="2.0"/>
    <line x1="{cx - 45}" y1="{cy + 55}" x2="{cx + 45}" y2="{cy + 55}" stroke="#000000" stroke-width="2.0"/>
    <line x1="{cx}" y1="{cy + 105}" x2="{cx - 35}" y2="{cy + 175}" stroke="#000000" stroke-width="2.0"/>
    <line x1="{cx}" y1="{cy + 105}" x2="{cx + 35}" y2="{cy + 175}" stroke="#000000" stroke-width="2.0"/>
    <text x="{cx}" y="{cy + 205}" font-family="Arial" font-size="15" font-weight="bold" text-anchor="middle" fill="#000000">{label}</text>
    <text x="{cx}" y="{cy + 225}" font-family="Arial" font-size="12.5" text-anchor="middle" fill="#555555">{sublabel}</text>
  </g>'''

def draw_uc(cx, cy, label, rx=155, ry=30):
    return f'''  <g id="uc-{label.lower().replace(' ', '-')}">
    <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
    <text x="{cx}" y="{cy + 5}" font-family="Arial" font-size="13.5" font-weight="bold" text-anchor="middle" fill="#000000">{label}</text>
  </g>'''

def draw_uc_rel(x1, y1, x2, y2, stereo):
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2 - 8
    return f'''  <g>
    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000000" stroke-width="1.5" stroke-dasharray="6,4" marker-end="url(#arrow-open)"/>
    <text x="{mx}" y="{my}" font-family="Arial" font-size="12" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;{stereo}&gt;&gt;</text>
  </g>'''

c = []
c.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f3f5" stroke-width="0.8"/>
    </pattern>
    <marker id="arrow-open" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9" fill="none" stroke="#000000" stroke-width="1.6"/>
    </marker>
  </defs>

  <rect width="{W}" height="{H}" fill="#ffffff"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <rect x="25" y="25" width="{W - 50}" height="{H - 50}" fill="none" stroke="#000000" stroke-width="1.6"/>

  <g id="title-header">
    <text x="{W/2}" y="65" font-family="'Times New Roman', Times, serif" font-size="22" font-weight="bold" text-anchor="middle" fill="#000000" letter-spacing="1">USE CASE DIAGRAM</text>
    <text x="{W/2}" y="90" font-family="'Times New Roman', Times, serif" font-size="13.5" font-style="italic" text-anchor="middle" fill="#333333">Sistem Pendukung Keputusan Penilaian Kinerja Karyawan MOORA - PT ISS Indonesia Site Prodia</text>
  </g>

  <!-- System Boundary in Center -->
  <rect x="330" y="130" width="940" height="770" rx="12" ry="12" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <path d="M 330 175 L 1270 175" stroke="#000000" stroke-width="1.5"/>
  <text x="800" y="160" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle" fill="#000000">Sistem Aplikasi SPK MOORA ISS Prodia</text>
''')

# Left Actors (PT ISS Indonesia)
c.append(draw_actor(165, 230, "Super Admin", "(HRD PT ISS)"))
c.append(draw_actor(165, 600, "Site Supervisor", "(ISS Prodia)"))

# Right Actor (PT Prodia Widyahusada)
c.append(draw_actor(1435, 640, "Branch Manager", "(Prodia Kebayoran)"))

# Center Column (Primary Use Cases)
cx1 = 660
c.append(draw_uc(cx1, 215, "Mengelola Master Karyawan"))
c.append(draw_uc(cx1, 315, "Mengatur Kriteria &amp; Bobot"))
c.append(draw_uc(cx1, 415, "Mengelola Periode Penilaian"))
c.append(draw_uc(cx1, 525, "Input Skor Kinerja Lapangan"))
c.append(draw_uc(cx1, 635, "Sinkronisasi Metode MOORA"))
c.append(draw_uc(cx1, 745, "Melihat Klasemen Peringkat"))
c.append(draw_uc(cx1, 845, "Mencetak SK &amp; Berita Acara"))

# Right Column (Included & Extended Use Cases)
cx2 = 1100
c.append(draw_uc(cx2, 215, "Validasi Duplikasi NIP", rx=140))
c.append(draw_uc(cx2, 635, "Normalisasi &amp; Optimasi Yi", rx=150))
c.append(draw_uc(cx2, 745, "Filter Divisi CS &amp; Messenger", rx=150))
c.append(draw_uc(cx2, 845, "Export PDF Laporan Resmi", rx=145))

# Connectors:
c.append('  <!-- Association Lines -->')
c.append('  <g stroke="#000000" stroke-width="1.5">')

# 1. Super Admin (Hand at 210, 285) -> touches left edge of Use Cases at x = 505
c.append('    <line x1="210" y1="285" x2="505" y2="215"/>')
c.append('    <line x1="210" y1="285" x2="505" y2="315"/>')
c.append('    <line x1="210" y1="285" x2="505" y2="415"/>')

# 2. Site Supervisor (Hand at 210, 655) -> touches left edge at x = 505
c.append('    <line x1="210" y1="655" x2="505" y2="525"/>')
c.append('    <line x1="210" y1="655" x2="505" y2="635"/>')
c.append('    <line x1="210" y1="655" x2="505" y2="745"/>')
c.append('    <line x1="210" y1="655" x2="505" y2="845"/>')

# 3. Branch Manager on Right (Hand at 1390, 695) -> connects to right side of UC 6 & 7
# To avoid touching Filter Divisi (at cx2=1100, y=745), Branch Manager connects to:
# Melihat Klasemen at (815, 745)? Wait, between 815 and 950!
# Wait, look: UC 6 right edge is at 660 + 155 = 815!
# And UC 8 (Filter Divisi) left edge is at 1100 - 150 = 950!
# So between x=815 and x=950 there is 135px space!
# But if Branch Manager is at x=1390, the line from (1390, 695) to (815, 745) would pass through Filter Divisi!
