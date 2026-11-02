import subprocess, os

W, H = 1600, 1050

def draw_actor(cx, cy, label, sublabel):
    return f'''  <!-- Actor: {label} -->
  <g id="actor-{label.lower().replace(' ', '-')}">
    <circle cx="{cx}" cy="{cy}" r="26" fill="#ffffff" stroke="#000000" stroke-width="2.0"/>
    <line x1="{cx}" y1="{cy + 26}" x2="{cx}" y2="{cy + 95}" stroke="#000000" stroke-width="2.0"/>
    <line x1="{cx - 42}" y1="{cy + 52}" x2="{cx + 42}" y2="{cy + 52}" stroke="#000000" stroke-width="2.0"/>
    <line x1="{cx}" y1="{cy + 95}" x2="{cx - 32}" y2="{cy + 160}" stroke="#000000" stroke-width="2.0"/>
    <line x1="{cx}" y1="{cy + 95}" x2="{cx + 32}" y2="{cy + 160}" stroke="#000000" stroke-width="2.0"/>
    <text x="{cx}" y="{cy + 188}" font-family="Arial" font-size="15" font-weight="bold" text-anchor="middle" fill="#000000">{label}</text>
    <text x="{cx}" y="{cy + 208}" font-family="Arial" font-size="12.5" text-anchor="middle" fill="#555555">{sublabel}</text>
  </g>'''

def draw_uc(cx, cy, label, rx=165, ry=32):
    return f'''  <g id="uc-{label.lower().replace(' ', '-')}">
    <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
    <text x="{cx}" y="{cy + 5}" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle" fill="#000000">{label}</text>
  </g>'''

def draw_uc_rel(x1, y1, x2, y2, stereo):
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2 - 8
    return f'''  <g>
    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#000000" stroke-width="1.5" stroke-dasharray="6,4" marker-end="url(#arrow-open)"/>
    <text x="{mx}" y="{my}" font-family="Arial" font-size="12.5" font-style="italic" text-anchor="middle" fill="#000000">&lt;&lt;{stereo}&gt;&gt;</text>
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

  <!-- System Boundary -->
  <rect x="390" y="130" width="1140" height="870" rx="12" ry="12" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <path d="M 390 175 L 1530 175" stroke="#000000" stroke-width="1.5"/>
  <text x="960" y="160" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle" fill="#000000">Sistem Aplikasi SPK MOORA ISS Prodia</text>
''')

# 3 Actors on Left
c.append(draw_actor(190, 190, "Super Admin", "(HRD PT ISS)"))
c.append(draw_actor(190, 480, "Site Supervisor", "(ISS Prodia)"))
c.append(draw_actor(190, 770, "Branch Manager", "(Prodia Kebayoran)"))

# Primary Use Cases
cx1 = 680
c.append(draw_uc(cx1, 205, "Mengelola Master Karyawan"))
c.append(draw_uc(cx1, 315, "Mengatur Kriteria &amp; Bobot"))
c.append(draw_uc(cx1, 425, "Mengelola Periode Penilaian"))
c.append(draw_uc(cx1, 535, "Input Skor Kinerja Lapangan"))
c.append(draw_uc(cx1, 645, "Sinkronisasi Metode MOORA"))
c.append(draw_uc(cx1, 755, "Melihat Klasemen Peringkat"))
c.append(draw_uc(cx1, 865, "Mencetak SK &amp; Berita Acara"))

# Secondary Use Cases
cx2 = 1270
c.append(draw_uc(cx2, 205, "Validasi Duplikasi NIP", rx=160))
c.append(draw_uc(cx2, 535, "Normalisasi Rasio Matriks R", rx=165))
c.append(draw_uc(cx2, 645, "Optimasi Multiobjektif Yi", rx=165))
c.append(draw_uc(cx2, 755, "Filter Divisi CS &amp; Messenger", rx=165))
c.append(draw_uc(cx2, 865, "Export PDF Laporan Resmi", rx=165))

# Association Lines from Actors to Primary Use Cases
c.append('  <!-- Association Lines -->')
c.append('  <g stroke="#000000" stroke-width="1.5">')

# 1. Super Admin (hand at 232, 242)
c.append('    <!-- Super Admin Associations -->')
c.append('    <line x1="232" y1="242" x2="515" y2="205"/>')
c.append('    <line x1="232" y1="242" x2="515" y2="315"/>')
c.append('    <line x1="232" y1="242" x2="515" y2="425"/>')
c.append('    <line x1="232" y1="242" x2="515" y2="755"/>')

# 2. Site Supervisor (hand at 232, 532)
c.append('    <!-- Site Supervisor Associations -->')
c.append('    <line x1="232" y1="532" x2="515" y2="535"/>')
c.append('    <line x1="232" y1="532" x2="515" y2="645"/>')
c.append('    <line x1="232" y1="532" x2="515" y2="755"/>')
c.append('    <line x1="232" y1="532" x2="515" y2="865"/>')

# 3. Branch Manager (hand at 232, 822)
c.append('    <!-- Branch Manager Associations -->')
c.append('    <line x1="232" y1="822" x2="515" y2="755"/>')
c.append('    <line x1="232" y1="822" x2="515" y2="865"/>')
c.append('  </g>')

# Include & Extend Relationships
c.append('  <!-- Include / Extend Relationships -->')
c.append(draw_uc_rel(845, 205, 1110, 205, "include"))
c.append(draw_uc_rel(845, 535, 1105, 535, "include"))
c.append(draw_uc_rel(845, 645, 1105, 645, "include"))
c.append(draw_uc_rel(1105, 755, 845, 755, "extend"))
c.append(draw_uc_rel(845, 865, 1105, 865, "include"))

c.append('</svg>')

svg_code = "\n".join(c)
with open("public/diagrams/use_case_diagram.svg", "w") as f:
    f.write(svg_code)

html_content = f'''<!DOCTYPE html>
<html>
<head><meta charset="utf-8">
<style>* {{ margin: 0; padding: 0; }} body {{ background: #ffffff; width: {W}px; height: {H}px; overflow: hidden; }}</style>
</head><body>{svg_code}</body></html>'''

with open("public/diagrams/use_case_diagram.html", "w") as f:
    f.write(html_content)

chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([
    chrome_bin,
    "--headless",
    "--disable-gpu",
    f"--screenshot=public/diagrams/use_case_diagram.png",
    f"--window-size={W},{H}",
    "--default-background-color=00000000",
    f"file://{os.path.abspath('public/diagrams/use_case_diagram.html')}"
], check=True)

# Copy to artifacts
artifact_png = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/bf16a660-61d1-4c97-9b52-171c84a54e6d/use_case_diagram.png"
with open("public/diagrams/use_case_diagram.png", "rb") as rf, open(artifact_png, "wb") as wf:
    wf.write(rf.read())

print("✓ Done rendering 3-actor Use Case Diagram!")
