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

def draw_uc(cx, cy, label, rx=160, ry=32):
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

  <!-- System Boundary in Center -->
  <rect x="330" y="130" width="940" height="770" rx="12" ry="12" fill="#ffffff" stroke="#000000" stroke-width="1.8"/>
  <path d="M 330 175 L 1270 175" stroke="#000000" stroke-width="1.5"/>
  <text x="800" y="160" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle" fill="#000000">Sistem Aplikasi SPK MOORA ISS Prodia</text>
''')

# Left Actors (PT ISS Indonesia)
c.append(draw_actor(165, 230, "Super Admin", "(HRD PT ISS)"))
c.append(draw_actor(165, 600, "Site Supervisor", "(ISS Prodia)"))

# Right Actor (PT Prodia Widyahusada)
c.append(draw_actor(1435, 410, "Branch Manager", "(Prodia Kebayoran)"))

# Use Cases Inside Boundary
# Column 1 (Left): Master Data & Operational Input
cx1 = 540
c.append(draw_uc(cx1, 220, "Mengelola Master Karyawan"))
c.append(draw_uc(cx1, 340, "Mengatur Kriteria &amp; Bobot"))
c.append(draw_uc(cx1, 460, "Mengelola Periode Penilaian"))
c.append(draw_uc(cx1, 600, "Input Skor Kinerja Lapangan"))
c.append(draw_uc(cx1, 720, "Sinkronisasi Metode MOORA"))

# Column 2 (Right): Results, Reporting & Calculations
cx2 = 1060
c.append(draw_uc(cx2, 220, "Validasi Duplikasi NIP", rx=150))
c.append(draw_uc(cx2, 340, "Filter Divisi CS &amp; Messenger", rx=155))
c.append(draw_uc(cx2, 460, "Melihat Klasemen Peringkat", rx=160))
c.append(draw_uc(cx2, 580, "Mencetak SK &amp; Berita Acara", rx=160))
c.append(draw_uc(cx2, 720, "Normalisasi &amp; Optimasi Yi", rx=155))
c.append(draw_uc(cx2, 840, "Export PDF Laporan Resmi", rx=150))

# Connectors:
c.append('  <!-- Association Lines -->')
c.append('  <g stroke="#000000" stroke-width="1.5">')

# 1. Super Admin (Hand at 210, 285)
c.append('    <line x1="210" y1="285" x2="380" y2="220"/>')
c.append('    <line x1="210" y1="285" x2="380" y2="340"/>')
c.append('    <line x1="210" y1="285" x2="380" y2="460"/>')
c.append('    <line x1="210" y1="285" x2="900" y2="460"/>') # to Melihat Klasemen Peringkat

# 2. Site Supervisor (Hand at 210, 655)
c.append('    <line x1="210" y1="655" x2="380" y2="600"/>')
c.append('    <line x1="210" y1="655" x2="380" y2="720"/>')
c.append('    <line x1="210" y1="655" x2="900" y2="460"/>') # to Melihat Klasemen Peringkat
c.append('    <line x1="210" y1="655" x2="900" y2="580"/>') # to Mencetak SK & Berita Acara

# 3. Branch Manager (Hand at 1390, 465)
c.append('    <line x1="1390" y1="465" x2="1220" y2="460"/>') # to Melihat Klasemen Peringkat
c.append('    <line x1="1390" y1="465" x2="1220" y2="580"/>') # to Mencetak SK & Berita Acara
c.append('  </g>')

# Include & Extend Relationships
c.append('  <!-- Include / Extend Relationships -->')
# Mengelola Master Karyawan -> Validasi Duplikasi NIP
c.append(draw_uc_rel(700, 220, 910, 220, "include"))

# Sinkronisasi Metode MOORA -> Normalisasi & Optimasi Yi
c.append(draw_uc_rel(700, 720, 905, 720, "include"))

# Filter Divisi -> Melihat Klasemen Peringkat (extend)
c.append(draw_uc_rel(1060, 372, 1060, 428, "extend"))

# Mencetak SK & Berita Acara -> Export PDF (include)
c.append(draw_uc_rel(1060, 612, 1060, 808, "include"))

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

print("✓ Done rendering perfect split Use Case Diagram!")
