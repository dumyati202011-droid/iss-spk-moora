import subprocess, os

W, H = 1650, 980

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

def draw_uc(cx, cy, label, rx=160, ry=30):
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
  <rect x="330" y="130" width="1030" height="820" rx="12" ry="12" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <path d="M 330 175 L 1360 175" stroke="#000000" stroke-width="1.5"/>
  <text x="845" y="160" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle" fill="#000000">Sistem Aplikasi SPK MOORA ISS Prodia</text>
''')

# Left Actors (PT ISS Indonesia)
c.append(draw_actor(165, 230, "Super Admin", "(HRD PT ISS)"))
c.append(draw_actor(165, 600, "Site Supervisor", "(ISS Prodia)"))

# Right Actor (PT Prodia Widyahusada)
c.append(draw_actor(1500, 700, "Branch Manager", "(Prodia Kebayoran)"))

# Primary Use Cases (Center Column, cx = 690)
cx1 = 690
c.append(draw_uc(cx1, 215, "Mengelola Data Karyawan", rx=165))
c.append(draw_uc(cx1, 335, "Mengatur Kriteria &amp; Bobot", rx=165))
c.append(draw_uc(cx1, 465, "Input Skor Penilaian Kinerja", rx=165))
c.append(draw_uc(cx1, 585, "Sinkronisasi &amp; Komputasi MOORA", rx=165))
c.append(draw_uc(cx1, 715, "Melihat Dashboard &amp; Klasemen", rx=165))
c.append(draw_uc(cx1, 825, "Mencetak SK &amp; Berita Acara", rx=165))
c.append(draw_uc(cx1, 915, "Export PDF Dokumen Resmi", rx=150, ry=25))

# Secondary Use Cases (Right Column inside boundary, cx = 1170)
cx2 = 1170
c.append(draw_uc(cx2, 215, "Validasi Duplikasi NIP", rx=145))
c.append(draw_uc(cx2, 335, "Validasi Total Bobot 100%", rx=145))
c.append(draw_uc(cx2, 465, "Filter Divisi CS &amp; Messenger", rx=150))
c.append(draw_uc(cx2, 585, "Normalisasi &amp; Optimasi Yi", rx=150))

# Connectors:
c.append('  <!-- Association Lines -->')
c.append('  <g stroke="#000000" stroke-width="1.5">')

# 1. Super Admin (Hand at 210, 285)
c.append('    <line x1="210" y1="285" x2="525" y2="215"/>')
c.append('    <line x1="210" y1="285" x2="525" y2="335"/>')
c.append('    <line x1="210" y1="285" x2="525" y2="715"/>')

# 2. Site Supervisor (Hand at 210, 655)
c.append('    <line x1="210" y1="655" x2="525" y2="465"/>')
c.append('    <line x1="210" y1="655" x2="525" y2="585"/>')
c.append('    <line x1="210" y1="655" x2="525" y2="715"/>')
c.append('    <line x1="210" y1="655" x2="525" y2="825"/>')

# 3. Branch Manager on Right (Hand at 1455, 755)
# Direct completely unobstructed connection to right edge of Klasemen and Cetak SK!
c.append('    <line x1="1455" y1="755" x2="855" y2="715"/>')
c.append('    <line x1="1455" y1="755" x2="855" y2="825"/>')
c.append('  </g>')

# Include & Extend Relationships
c.append('  <!-- Include / Extend Relationships -->')
# Mengelola Data Karyawan -> Validasi Duplikasi NIP
c.append(draw_uc_rel(855, 215, 1025, 215, "include"))

# Mengatur Kriteria & Bobot -> Validasi Total Bobot 100%
c.append(draw_uc_rel(855, 335, 1025, 335, "include"))

# Filter Divisi -> Melihat Dashboard (diagonal extend)
c.append(draw_uc_rel(1050, 490, 840, 690, "extend"))

# Sinkronisasi MOORA -> Normalisasi & Optimasi Yi
c.append(draw_uc_rel(855, 585, 1020, 585, "include"))

# Mencetak SK -> Export PDF (vertical include)
c.append(draw_uc_rel(690, 855, 690, 890, "include"))

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

artifact_png = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/bf16a660-61d1-4c97-9b52-171c84a54e6d/use_case_diagram.png"
with open("public/diagrams/use_case_diagram.png", "rb") as rf, open(artifact_png, "wb") as wf:
    wf.write(rf.read())

print("✓ Done rendering masterpiece Use Case Diagram!")
