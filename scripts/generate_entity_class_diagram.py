#!/usr/bin/env python3
"""
generate_entity_class_diagram.py
Generates the pristine 1:1 Database Entity Class Diagram matching prisma/schema.prisma:
7 Entities:
1. User
2. AssessmentPeriod
3. Employee
4. Criteria
5. Assessment
6. AssessmentScore
7. MooraResult
"""

import os
import subprocess
import shutil

OUT_DIR = "public/diagrams"
ARTIFACT_DIR = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/e6c145f5-ba78-4f4a-bc31-4712ef0b13ed"

W = 1620
H = 1100

def create_entity_class_diagram():
    c = []
    
    # SVG Wrapper Start
    c.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <!-- Subtle 20px Grid Background -->
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="0.9"/>
    </pattern>

    <!-- Drop Shadow for Class Cards -->
    <filter id="card-shadow" x="-3%" y="-2%" width="106%" height="106%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="2" dy="3" stdDeviation="2.5" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>

    <!-- UML Arrowhead Markers -->
    <marker id="uml-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#1e293b"/>
    </marker>
    <marker id="uml-diamond" viewBox="0 0 12 12" refX="1" refY="6" markerWidth="9" markerHeight="9" orient="auto-start-reverse">
      <polygon points="1,6 6,1.5 11,6 6,10.5" fill="#1e293b" stroke="#1e293b" stroke-width="1"/>
    </marker>
  </defs>

  <!-- Background Canvas -->
  <rect width="{W}" height="{H}" fill="#ffffff"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>

  <!-- Outer Frame -->
  <rect x="25" y="25" width="{W - 50}" height="{H - 50}" fill="none" stroke="#1e293b" stroke-width="1.8"/>

  <!-- Diagram Title Header -->
  <g id="title-header">
    <text x="{W/2}" y="65" font-family="'Times New Roman', Georgia, serif" font-size="22" font-weight="bold" text-anchor="middle" fill="#0f172a" letter-spacing="1">CLASS DIAGRAM (ENTITY DOMAIN MODEL)</text>
    <text x="{W/2}" y="90" font-family="'Times New Roman', Georgia, serif" font-size="13.5" font-style="italic" text-anchor="middle" fill="#475569">Struktur Relasi Kelas Entitas Basis Data — SPK Penilaian Kinerja Metode MOORA PT ISS Indonesia Site Prodia</text>
  </g>''')

    # Card Drawer Helper
    def draw_class(x, y, w, title, sub_title, attrs, methods):
        out = []
        header_h = 56
        attr_item_h = 22
        method_item_h = 22
        
        attrs_h = 16 + (len(attrs) * attr_item_h)
        methods_h = 16 + (len(methods) * method_item_h)
        total_h = header_h + attrs_h + methods_h
        
        out.append(f'  <!-- CLASS: {title} (height={total_h}, bottom={y+total_h}) -->')
        out.append(f'  <g id="class-{title.lower()}" filter="url(#card-shadow)">')
        
        # Outer Card Box
        out.append(f'    <rect x="{x}" y="{y}" width="{w}" height="{total_h}" fill="#ffffff" stroke="#1e293b" stroke-width="1.6" rx="4"/>')
        
        # Header Box (Soft Professional Blue-Gray)
        out.append(f'    <path d="M {x} {y} L {x+w} {y} L {x+w} {y+header_h} L {x} {y+header_h} Z" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6"/>')
        out.append(f'    <text x="{x + w/2}" y="{y + 20}" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-style="italic" text-anchor="middle" fill="#475569">&lt;&lt;entity&gt;&gt;</text>')
        out.append(f'    <text x="{x + w/2}" y="{y + 39}" font-family="Arial, Helvetica, sans-serif" font-size="15" font-weight="bold" text-anchor="middle" fill="#0f172a">{title}</text>')
        out.append(f'    <text x="{x + w/2}" y="{y + 51}" font-family="Arial, Helvetica, sans-serif" font-size="10" text-anchor="middle" fill="#64748b">({sub_title})</text>')
        
        # Divider 1
        out.append(f'    <line x1="{x}" y1="{y+header_h}" x2="{x+w}" y2="{y+header_h}" stroke="#1e293b" stroke-width="1.4"/>')
        
        # Attributes Compartment
        out.append(f'    <rect x="{x+1}" y="{y+header_h+1}" width="{w-2}" height="{attrs_h-1}" fill="#ffffff"/>')
        ay = y + header_h + 18
        for attr in attrs:
            out.append(f'    <text x="{x + 14}" y="{ay}" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#0f172a">{attr}</text>')
            ay += attr_item_h
            
        # Divider 2
        div2_y = y + header_h + attrs_h
        out.append(f'    <line x1="{x}" y1="{div2_y}" x2="{x+w}" y2="{div2_y}" stroke="#1e293b" stroke-width="1.4"/>')
        
        # Methods Compartment
        out.append(f'    <rect x="{x+1}" y="{div2_y+1}" width="{w-2}" height="{methods_h-2}" fill="#f8fafc" rx="0 0 4 4"/>')
        my = div2_y + 18
        for m in methods:
            out.append(f'    <text x="{x + 14}" y="{my}" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#1e293b">{m}</text>')
            my += method_item_h
            
        out.append('  </g>')
        return "\n".join(out)

    # Multiplicity Badge Drawer Helper
    def draw_badge(x, y, text):
        return f'''    <g>
      <rect x="{x-12}" y="{y-10}" width="24" height="18" rx="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
      <text x="{x}" y="{y+3}" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#0f172a" text-anchor="middle">{text}</text>
    </g>'''

    # ========================================================
    # ROW 1 (TOP): 4 Primary / Master Tables (Y = 120)
    # Total heights:
    # User: 56 + 148 + 126 = 330 -> bottom = 450
    # Criteria: 56 + 148 + 126 = 330 -> bottom = 450
    # AssessmentPeriod: 56 + 148 + 126 = 330 -> bottom = 450
    # Employee: 56 + 170 + 126 = 352 -> bottom = 472
    # ========================================================
    
    # 1. USER (x: 50, w: 325, y: 120..450)
    c.append(draw_class(50, 120, 325, "User", "Tabel Akun &amp; Hak Akses", [
        "- id : String [PK]",
        "- username : String [Unique]",
        "- password : String",
        "- fullName : String",
        "- role : String (SUPER_ADMIN / SPV / MGR)",
        "- createdAt : DateTime"
    ], [
        "+ tambahPengguna() : Boolean",
        "+ ubahPengguna() : Boolean",
        "+ hapusPengguna() : Boolean",
        "+ verifikasiPassword(password: String) : Boolean",
        "+ getPenggunaById(id: String) : User"
    ]))

    # 2. CRITERIA (x: 430, w: 345, y: 120..450)
    c.append(draw_class(430, 120, 345, "Criteria", "Tabel Kriteria Penilaian", [
        "- id : String [PK]",
        "- code : String (C1, C2, C3, C4, C5)",
        "- name : String",
        "- type : String (BENEFIT / COST)",
        "- weight : Float (Bobot Kriteria Wj)",
        "- division : String (CLEANING / MESSENGER)"
    ], [
        "+ tambahKriteria() : Boolean",
        "+ ubahKriteria() : Boolean",
        "+ validasiTotalBobot() : Boolean",
        "+ getKriteriaByDivisi(divisi: String) : List",
        "+ getBobotTernormalisasi() : Float"
    ]))

    # 3. ASSESSMENT PERIOD (x: 830, w: 340, y: 120..450)
    c.append(draw_class(830, 120, 340, "AssessmentPeriod", "Tabel Periode Penilaian", [
        "- id : String [PK]",
        "- periodName : String (Kuartal / Semester)",
        "- year : Int",
        "- status : String (ACTIVE / CLOSED / DRAFT)",
        "- startDate : DateTime",
        "- endDate : DateTime"
    ], [
        "+ tambahPeriode() : Boolean",
        "+ ubahPeriode() : Boolean",
        "+ tutupPeriode() : Boolean",
        "+ getPeriodeAktif() : AssessmentPeriod",
        "+ getSemuaPeriode() : List"
    ]))

    # 4. EMPLOYEE (x: 1225, w: 345, y: 120..472)
    c.append(draw_class(1225, 120, 345, "Employee", "Tabel Data Karyawan", [
        "- id : String [PK]",
        "- nip : String [Unique]",
        "- fullName : String",
        "- division : String (CLEANING / MESSENGER)",
        "- placementUnit : String",
        "- joinDate : DateTime",
        "- isActive : Boolean"
    ], [
        "+ tambahKaryawan() : Boolean",
        "+ ubahKaryawan() : Boolean",
        "+ updateStatusAktif() : Boolean",
        "+ getKaryawanByNip(nip: String) : Employee",
        "+ getKaryawanByDivisi(divisi: String) : List"
    ]))

    # ========================================================
    # ROW 2 (BOTTOM): Transaction, Score & Results (Y = 620)
    # ========================================================

    # 5. ASSESSMENT (x: 80, w: 350, y: 620..950)
    c.append(draw_class(80, 620, 350, "Assessment", "Tabel Lembar Penilaian", [
        "- id : String [PK]",
        "- periodId : String [FK]",
        "- employeeId : String [FK]",
        "- userId : String [FK - Penilai]",
        "- createdAt : DateTime"
    ], [
        "+ buatPenilaian() : Boolean",
        "+ ubahPenilaian() : Boolean",
        "+ hapusPenilaian() : Boolean",
        "+ cekKelengkapanSkor() : Boolean",
        "+ getPenilaianByKaryawan(id: String) : Assessment"
    ]))

    # 6. ASSESSMENT SCORE (x: 600, w: 365, y: 620..930)
    c.append(draw_class(600, 620, 365, "AssessmentScore", "Tabel Rincian Skor Nilai", [
        "- id : String [PK]",
        "- assessmentId : String [FK]",
        "- criteriaId : String [FK]",
        "- rawScore : Float (Nilai Mentah Xij 1..100)"
    ], [
        "+ simpanSkor() : Boolean",
        "+ ubahSkor() : Boolean",
        "+ validasiRentangSkor(skor: Float) : Boolean",
        "+ getRincianSkor(assessmentId: String) : List"
    ]))

    # 7. MOORA RESULT (x: 1120, w: 395, y: 620..990)
    c.append(draw_class(1120, 620, 395, "MooraResult", "Tabel Hasil Perhitungan MOORA", [
        "- id : String [PK]",
        "- periodId : String [FK]",
        "- employeeId : String [FK]",
        "- division : String",
        "- sumBenefit : Float",
        "- sumCost : Float",
        "- yScore : Float (Nilai Optimasi Yi)",
        "- rankPosition : Int (Peringkat 1..N)"
    ], [
        "+ simpanHasilKomputasi() : Boolean",
        "+ getPeringkatTeratas(limit: Int) : List",
        "+ getHasilByPeriode(periodId: String) : List",
        "+ exportSuratKeputusanPDF() : File",
        "+ getStatusKelayakanReward() : String"
    ]))

    # ========================================================
    # RELATIONSHIPS (100% COLLISION FREE ORTHOGONAL LINES)
    # Corridor between Row 1 and Row 2 is Y = 472 to Y = 620 (148px height)
    # Channels:
    # y = 510 : Criteria -> AssessmentScore
    # y = 530 : AssessmentPeriod -> Assessment
    # y = 555 : AssessmentPeriod -> MooraResult
    # y = 580 : Employee -> Assessment
    # ========================================================
    c.append('  <!-- ================= RELATIONSHIP CONNECTORS ================= -->')
    c.append('  <g stroke="#1e293b" stroke-width="1.6" fill="none">')

    # 1. USER (1) ---- (0..*) ASSESSMENT
    # Line: User bottom (x=170, y=450) straight down to Assessment top (x=170, y=620)
    c.append('    <!-- 1. User -> Assessment (1 : N) -->')
    c.append('    <line x1="170" y1="450" x2="170" y2="620" marker-end="url(#uml-arrow)"/>')
    c.append(draw_badge(190, 470, "1"))
    c.append(draw_badge(190, 600, "0..*"))
    c.append('    <text x="185" y="535" font-family="Arial, Helvetica, sans-serif" font-size="11" font-style="italic" fill="#475569" text-anchor="start">menilai</text>')

    # 2. CRITERIA (1) ---- (0..*) ASSESSMENT_SCORE
    # Line: Criteria bottom (x=600, y=450) down to y=510, right to AssessmentScore top (x=700, y=620)
    c.append('    <!-- 2. Criteria -> AssessmentScore (1 : N) -->')
    c.append('    <path d="M 600 450 L 600 510 L 700 510 L 700 620" marker-end="url(#uml-arrow)"/>')
    c.append(draw_badge(620, 470, "1"))
    c.append(draw_badge(720, 600, "0..*"))
    c.append('    <text x="650" y="502" font-family="Arial, Helvetica, sans-serif" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">menjadi acuan skor</text>')

    # 3. ASSESSMENT (1) ---- (1..*) ASSESSMENT_SCORE (Composition)
    # Line: Assessment right (x=430, y=720) horizontal straight to AssessmentScore left (x=600, y=720)
    c.append('    <!-- 3. Assessment -> AssessmentScore (1 : 1..*) Composition -->')
    c.append('    <line x1="430" y1="720" x2="600" y2="720" marker-start="url(#uml-diamond)" marker-end="url(#uml-arrow)"/>')
    c.append(draw_badge(460, 700, "1"))
    c.append(draw_badge(570, 700, "1..*"))
    c.append('    <text x="515" y="712" font-family="Arial, Helvetica, sans-serif" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">merinci &gt;</text>')

    # 4. ASSESSMENT_PERIOD (1) ---- (0..*) ASSESSMENT
    # Line: AssessmentPeriod bottom-left (x=900, y=450) down to corridor y=535, left to Assessment top-right (x=350, y=620)
    c.append('    <!-- 4. AssessmentPeriod -> Assessment (1 : N) -->')
    c.append('    <path d="M 900 450 L 900 535 L 350 535 L 350 620" marker-end="url(#uml-arrow)"/>')
    c.append(draw_badge(920, 470, "1"))
    c.append(draw_badge(370, 600, "0..*"))
    c.append('    <text x="470" y="527" font-family="Arial, Helvetica, sans-serif" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">lingkup periode</text>')

    # 5. ASSESSMENT_PERIOD (1) ---- (0..*) MOORA_RESULT
    # Line: AssessmentPeriod bottom-right (x=1100, y=450) down to corridor y=555, right to MooraResult top-left (x=1200, y=620)
    c.append('    <!-- 5. AssessmentPeriod -> MooraResult (1 : N) -->')
    c.append('    <path d="M 1100 450 L 1100 555 L 1200 555 L 1200 620" marker-end="url(#uml-arrow)"/>')
    c.append(draw_badge(1120, 470, "1"))
    c.append(draw_badge(1220, 600, "0..*"))
    c.append('    <text x="1150" y="547" font-family="Arial, Helvetica, sans-serif" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">menampung hasil</text>')

    # 6. EMPLOYEE (1) ---- (0..*) ASSESSMENT
    # Line: Employee bottom-left (x=1280, y=472) down to corridor y=580, left to Assessment top-center (x=260, y=620)
    c.append('    <!-- 6. Employee -> Assessment (1 : N) -->')
    c.append('    <path d="M 1280 472 L 1280 580 L 260 580 L 260 620" marker-end="url(#uml-arrow)"/>')
    c.append(draw_badge(1300, 492, "1"))
    c.append(draw_badge(280, 600, "0..*"))
    c.append('    <text x="800" y="572" font-family="Arial, Helvetica, sans-serif" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">karyawan dievaluasi</text>')

    # 7. EMPLOYEE (1) ---- (0..*) MOORA_RESULT
    # Line: Employee bottom-right (x=1420, y=472) straight down to MooraResult top-right (x=1420, y=620)
    c.append('    <!-- 7. Employee -> MooraResult (1 : N) -->')
    c.append('    <line x1="1420" y1="472" x2="1420" y2="620" marker-end="url(#uml-arrow)"/>')
    c.append(draw_badge(1440, 492, "1"))
    c.append(draw_badge(1440, 600, "0..*"))
    c.append('    <text x="1435" y="545" font-family="Arial, Helvetica, sans-serif" font-size="11" font-style="italic" fill="#475569" text-anchor="start">memperoleh ranking</text>')

    c.append('  </g>')
    c.append('</svg>')
    
    return "\n".join(c)

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    
    svg_content = create_entity_class_diagram()
    
    svg_file = os.path.join(OUT_DIR, "class_diagram.svg")
    png_file = os.path.join(OUT_DIR, "class_diagram.png")
    html_file = os.path.join(OUT_DIR, "class_diagram.html")
    
    with open(svg_file, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[OK] Saved SVG to: {svg_file}")
    
    html_content = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #ffffff; width: {W}px; height: {H}px; overflow: hidden; }}
</style>
</head>
<body>
{svg_content}
</body>
</html>'''
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--force-device-scale-factor=2",
        f"--window-size={W},{H}",
        f"--screenshot={png_file}",
        html_file
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[OK] Rendered High-Res PNG to: {png_file}")
        artifact_png = os.path.join(ARTIFACT_DIR, "class_diagram.png")
        shutil.copyfile(png_file, artifact_png)
        print(f"[OK] Copied to Artifact: {artifact_png}")
    else:
        print(f"[ERR] Chrome screenshot failed: {res.stderr}")

if __name__ == "__main__":
    main()
