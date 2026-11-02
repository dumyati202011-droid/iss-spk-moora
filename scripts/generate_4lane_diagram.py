import os
import subprocess

html_usulan_4lane = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Activity Diagram Sistem Usulan (4 Swimlane)</title>
  <style>
    body {
      margin: 0;
      padding: 20px;
      background-color: #ffffff;
      font-family: Arial, Helvetica, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .diagram-container {
      background: #ffffff;
      padding: 18px;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    }
    .diagram-title {
      text-align: center;
      font-size: 15px;
      font-weight: bold;
      color: #0f172a;
      margin-bottom: 16px;
      letter-spacing: 0.5px;
    }
  </style>
</head>
<body>
  <div class="diagram-container">
    <div class="diagram-title">ACTIVITY DIAGRAM SISTEM USULAN SPK METODE MOORA (4 SWIMLANE TERINTEGRASI)</div>
    <svg width="1240" height="920" viewBox="0 0 1240 920" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
          <feDropShadow dx="1" dy="2" stdDeviation="1.5" flood-color="#000000" flood-opacity="0.12" />
        </filter>
        <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569" />
        </marker>
        <marker id="arrow-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
        </marker>
        <marker id="arrow-green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
        </marker>
        <marker id="arrow-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626" />
        </marker>
      </defs>

      <!-- ================= SWIMLANES ================= -->
      <!-- Lane 1: Super Admin / HRD ISS Pusat -->
      <rect x="15" y="20" width="295" height="880" fill="#fcfdfe" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="15" y="20" width="295" height="38" fill="#f3e8ff" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="162" y="44" font-size="12.5" font-weight="bold" fill="#6b21a8" text-anchor="middle">Super Admin / HRD (PT ISS Pusat)</text>

      <!-- Lane 2: Supervisor Lapangan ISS -->
      <rect x="310" y="20" width="295" height="880" fill="#fcfdfe" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="310" y="20" width="295" height="38" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="457" y="44" font-size="12.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Supervisor Lapangan (PT ISS Site)</text>

      <!-- Lane 3: Sistem SPK MOORA (Web Next.js) -->
      <rect x="605" y="20" width="320" height="880" fill="#f8fafc" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="605" y="20" width="320" height="38" fill="#e0e7ff" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="765" y="44" font-size="12.5" font-weight="bold" fill="#312e81" text-anchor="middle">Sistem SPK MOORA (Web Next.js)</text>

      <!-- Lane 4: Branch Manager Prodia -->
      <rect x="925" y="20" width="300" height="880" fill="#fcfdfe" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="925" y="20" width="300" height="38" fill="#d1fae5" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="1075" y="44" font-size="12.5" font-weight="bold" fill="#065f46" text-anchor="middle">Branch Manager (Prodia Kebayoran)</text>

      <!-- ================= LANE 1: HRD ISS (SETUP & FINALIZE) ================= -->
      <!-- Start Node -->
      <circle cx="162" cy="80" r="12" fill="#1e293b" />

      <!-- Step 1: Login HR Admin -->
      <rect x="67" y="115" width="190" height="46" rx="8" ry="8" fill="#f3e8ff" stroke="#a855f7" stroke-width="1.5" filter="url(#shadow)" />
      <text x="162" y="142" font-size="11.5" font-weight="600" fill="#581c87" text-anchor="middle">Login Akun Super Admin</text>

      <!-- Step 2: Kelola Master Karyawan -->
      <rect x="67" y="185" width="190" height="50" rx="8" ry="8" fill="#f3e8ff" stroke="#a855f7" stroke-width="1.5" filter="url(#shadow)" />
      <text x="162" y="205" font-size="11" font-weight="600" fill="#581c87" text-anchor="middle">Kelola Master Data Karyawan</text>
      <text x="162" y="221" font-size="10.5" fill="#7e22ce" text-anchor="middle">20 Personel (CS &amp; Messenger)</text>

      <!-- Step 3: Konfigurasi Bobot & Periode -->
      <rect x="67" y="265" width="190" height="52" rx="8" ry="8" fill="#f3e8ff" stroke="#a855f7" stroke-width="1.5" filter="url(#shadow)" />
      <text x="162" y="285" font-size="11" font-weight="600" fill="#581c87" text-anchor="middle">Tetapkan Bobot Kriteria (Wj)</text>
      <text x="162" y="301" font-size="10.5" fill="#7e22ce" text-anchor="middle">&amp; Buka Periode Penilaian Aktif</text>

      <!-- Step 16 (Lanjutan dari Lane 4 di bagian bawah): Terima SK Final -->
      <rect x="67" y="785" width="190" height="54" rx="8" ry="8" fill="#d1fae5" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)" />
      <text x="162" y="805" font-size="11" font-weight="600" fill="#065f46" text-anchor="middle">Menerima SK Sah dari Klien</text>
      <text x="162" y="821" font-size="10.5" fill="#047857" text-anchor="middle">sebagai Dasar Payroll Insentif</text>

      <!-- End Node -->
      <circle cx="162" cy="875" r="14" fill="#ffffff" stroke="#1e293b" stroke-width="2" />
      <circle cx="162" cy="875" r="8" fill="#1e293b" />

      <!-- ================= LANE 2: SUPERVISOR LAPANGAN ================= -->
      <!-- Step 4: Login SPV -->
      <rect x="362" y="265" width="190" height="52" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="457" y="295" font-size="11.5" font-weight="600" fill="#1e3a8a" text-anchor="middle">Login Akun Supervisor Lapangan</text>

      <!-- Step 5: Pilih Kategori -->
      <rect x="362" y="350" width="190" height="48" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="457" y="370" font-size="11" font-weight="600" fill="#1e3a8a" text-anchor="middle">Pilih Kategori Independen</text>
      <text x="457" y="385" font-size="10.5" fill="#475569" text-anchor="middle">(Cleaning Service / Messenger)</text>

      <!-- Step 6: Input Nilai Lapangan -->
      <rect x="362" y="430" width="190" height="50" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="457" y="450" font-size="11" font-weight="600" fill="#1e3a8a" text-anchor="middle">Input Nilai Kinerja Lapangan</text>
      <text x="457" y="466" font-size="10.5" fill="#475569" text-anchor="middle">Skor Skala 1 - 100 per Kriteria</text>

      <!-- Step 7: Klik Sinkronkan -->
      <rect x="362" y="510" width="190" height="48" rx="8" ry="8" fill="#d5e8d4" stroke="#82b366" stroke-width="1.5" filter="url(#shadow)" />
      <text x="457" y="530" font-size="11" font-weight="600" fill="#065f46" text-anchor="middle">Klik Tombol Aksi</text>
      <text x="457" y="545" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">"Sinkronkan MOORA"</text>

      <!-- ================= LANE 3: SISTEM SPK MOORA ================= -->
      <!-- Step 8: Validasi Data -->
      <rect x="670" y="510" width="190" height="48" rx="8" ry="8" fill="#ffffff" stroke="#6366f1" stroke-width="1.5" filter="url(#shadow)" />
      <text x="765" y="530" font-size="11" font-weight="600" fill="#1e1b4b" text-anchor="middle">Validasi Kelengkapan Nilai</text>
      <text x="765" y="545" font-size="10.5" fill="#64748b" text-anchor="middle">&amp; Parameter Bobot Kriteria</text>

      <!-- Step 9: Matriks X & Normalisasi R -->
      <rect x="670" y="585" width="190" height="50" rx="8" ry="8" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5" filter="url(#shadow)" />
      <text x="765" y="605" font-size="11" font-weight="600" fill="#1e1b4b" text-anchor="middle">Bentuk Matriks Keputusan X</text>
      <text x="765" y="621" font-size="10.5" fill="#4338ca" text-anchor="middle">&amp; Normalisasi Rasio Matriks R</text>

      <!-- Step 10: Matriks V & Nilai Optimasi Yi -->
      <rect x="670" y="660" width="190" height="50" rx="8" ry="8" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5" filter="url(#shadow)" />
      <text x="765" y="680" font-size="11" font-weight="600" fill="#1e1b4b" text-anchor="middle">Hitung Matriks Terbobot V</text>
      <text x="765" y="696" font-size="10.5" font-weight="bold" fill="#4338ca" text-anchor="middle">&amp; Nilai Optimasi Yi = Benefit - Cost</text>

      <!-- Step 11: Ranking & Simpan DB -->
      <rect x="670" y="735" width="190" height="50" rx="8" ry="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5" filter="url(#shadow)" />
      <text x="765" y="755" font-size="11" font-weight="600" fill="#1e3a8a" text-anchor="middle">Urutkan Ranking &amp; Sorot Juara</text>
      <text x="765" y="771" font-size="10.5" fill="#2563eb" text-anchor="middle">Simpan ke DB SQLite (Prisma)</text>

      <!-- Step 12: Sajikan Klasemen -->
      <rect x="670" y="810" width="190" height="46" rx="8" ry="8" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5" filter="url(#shadow)" />
      <text x="765" y="828" font-size="11" font-weight="600" fill="#1e3a8a" text-anchor="middle">Sajikan Klasemen Real-time</text>
      <text x="765" y="843" font-size="10.5" fill="#64748b" text-anchor="middle">&amp; 4 Tab Transparansi Audit</text>

      <!-- ================= LANE 4: BRANCH MANAGER PRODIA ================= -->
      <!-- Step 13: Login BM Prodia -->
      <rect x="980" y="585" width="190" height="50" rx="8" ry="8" fill="#d1fae5" stroke="#10b981" stroke-width="1.5" filter="url(#shadow)" />
      <text x="1075" y="615" font-size="11.5" font-weight="600" fill="#065f46" text-anchor="middle">Login Akun Branch Manager</text>

      <!-- Step 14: Audit 4 Tab -->
      <rect x="980" y="660" width="190" height="50" rx="8" ry="8" fill="#ffe6cc" stroke="#d79b00" stroke-width="1.5" filter="url(#shadow)" />
      <text x="1075" y="680" font-size="11" font-weight="600" fill="#7c2d12" text-anchor="middle">Audit 4 Tab Matriks MOORA</text>
      <text x="1075" y="696" font-size="10.5" fill="#9a3412" text-anchor="middle">&amp; Validasi Skor Optimasi Yi</text>

      <!-- Decision Diamond: Ambang Batas Yi -->
      <polygon points="1075,735 1145,765 1075,795 1005,765" fill="#fff2cc" stroke="#d6b656" stroke-width="1.5" filter="url(#shadow)" />
      <text x="1075" y="762" font-size="11" font-weight="bold" fill="#854d0e" text-anchor="middle">Skor Yi &gt;=</text>
      <text x="1075" y="775" font-size="10" font-weight="bold" fill="#854d0e" text-anchor="middle">Ambang Batas?</text>

      <!-- Path Tidak: Pembinaan Tambahan -->
      <rect x="945" y="810" width="115" height="42" rx="6" ry="6" fill="#fef2f2" stroke="#f87171" stroke-width="1.2" />
      <text x="1002" y="828" font-size="10" font-weight="600" fill="#991b1b" text-anchor="middle">Evaluasi &amp; Pembinaan</text>
      <text x="1002" y="842" font-size="9" fill="#7f1d1d" text-anchor="middle">Ulang Personel</text>

      <!-- Path Ya: Sahkan SK & TTD Digital -->
      <rect x="1085" y="810" width="125" height="42" rx="6" ry="6" fill="#ecfdf5" stroke="#34d399" stroke-width="1.2" />
      <text x="1147" y="828" font-size="10" font-weight="600" fill="#065f46" text-anchor="middle">Sahkan &amp; E-Sign SK</text>
      <text x="1147" y="842" font-size="9" font-weight="bold" fill="#047857" text-anchor="middle">Serta Cetak Dokumen PDF</text>

      <!-- ================= CONNECTOR ARROWS ================= -->
      <!-- Lane 1: Start -> Step 1 -->
      <line x1="162" y1="92" x2="162" y2="115" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 1: Step 1 -> Step 2 -->
      <line x1="162" y1="161" x2="162" y2="185" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 1: Step 2 -> Step 3 -->
      <line x1="162" y1="235" x2="162" y2="265" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 1 Step 3 -> Lane 2 Step 4 (Setup Selesai, Akses Dibuka) -->
      <line x1="257" y1="291" x2="362" y2="291" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrow-blue)" />

      <!-- Lane 2: Step 4 -> Step 5 -->
      <line x1="457" y1="317" x2="457" y2="350" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 2: Step 5 -> Step 6 -->
      <line x1="457" y1="398" x2="457" y2="430" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 2: Step 6 -> Step 7 -->
      <line x1="457" y1="480" x2="457" y2="510" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 2 Step 7 -> Lane 3 Step 8 (Memicu Engine) -->
      <line x1="552" y1="534" x2="670" y2="534" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrow-blue)" />

      <!-- Lane 3: Step 8 -> Step 9 -->
      <line x1="765" y1="558" x2="765" y2="585" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 3: Step 9 -> Step 10 -->
      <line x1="765" y1="635" x2="765" y2="660" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 3: Step 10 -> Step 11 -->
      <line x1="765" y1="710" x2="765" y2="735" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 3: Step 11 -> Step 12 -->
      <line x1="765" y1="785" x2="765" y2="810" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 3 Step 9 -> Lane 4 Step 13 (Akses Paralel BM Prodia) -->
      <line x1="860" y1="610" x2="980" y2="610" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 4: Step 13 -> Step 14 -->
      <line x1="1075" y1="635" x2="1075" y2="660" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Lane 4: Step 14 -> Decision -->
      <line x1="1075" y1="710" x2="1075" y2="735" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Decision -> Tidak (Left Branch) -->
      <polyline points="1005,765 985,765 985,810" fill="none" stroke="#dc2626" stroke-width="1.5" marker-end="url(#arrow-red)" />
      <rect x="977" y="775" width="34" height="15" rx="3" fill="#ffffff" stroke="#fca5a5" stroke-width="1" />
      <text x="994" y="786" font-size="8.5" font-weight="bold" fill="#dc2626" text-anchor="middle">Tidak</text>

      <!-- Decision -> Ya (Right Branch) -->
      <polyline points="1145,765 1165,765 1165,810" fill="none" stroke="#16a34a" stroke-width="1.5" marker-end="url(#arrow-green)" />
      <rect x="1152" y="775" width="22" height="15" rx="3" fill="#ffffff" stroke="#86efac" stroke-width="1" />
      <text x="1163" y="786" font-size="8.5" font-weight="bold" fill="#16a34a" text-anchor="middle">Ya</text>

      <!-- Loopback dari Sahkan SK (Lane 4) kembali ke HRD (Lane 1 Step 16) -->
      <polyline points="1147,852 1147,885 580,885 580,812 257,812" fill="none" stroke="#059669" stroke-width="1.8" stroke-dasharray="6,4" marker-end="url(#arrow-green)" />
      <rect x="490" y="876" width="180" height="18" rx="4" fill="#ecfdf5" stroke="#a7f3d0" stroke-width="1" />
      <text x="580" y="889" font-size="9" font-weight="bold" fill="#047857" text-anchor="middle">Serah Terima SK Sah ke HR ISS (Payroll)</text>

      <!-- Lane 1: Step 16 -> End Node -->
      <line x1="162" y1="839" x2="162" y2="861" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />
    </svg>
  </div>
</body>
</html>
"""

html_path = "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_usulan_4lane.html"
png_path = "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_diagram_sistem_usulan.png"
svg_path = "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_diagram_sistem_usulan.svg"
artifact_dir = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/bf16a660-61d1-4c97-9b52-171c84a54e6d"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_usulan_4lane)

# Extract SVG pure
start_tag = "<svg"
end_tag = "</svg>"
s_idx = html_usulan_4lane.find(start_tag)
e_idx = html_usulan_4lane.find(end_tag) + len(end_tag)
pure_svg = html_usulan_4lane[s_idx:e_idx]

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(pure_svg)

with open(os.path.join(artifact_dir, "activity_diagram_sistem_usulan.svg"), "w", encoding="utf-8") as f:
    f.write(pure_svg)

print("Pure SVG saved without usernames.")

# Compile to PNG via Chrome headless
chrome_cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=1300,1000",
    f"--screenshot={png_path}",
    html_path
]

res = subprocess.run(chrome_cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

# Copy PNG to artifact
subprocess.run(["cp", png_path, os.path.join(artifact_dir, "activity_diagram_sistem_usulan.png")])
print("Updated PNG copied to artifact successfully!")
