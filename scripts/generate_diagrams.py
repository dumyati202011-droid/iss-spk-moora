import os
import subprocess

html_berjalan = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Activity Diagram Sistem Berjalan</title>
  <style>
    body {
      margin: 0;
      padding: 30px;
      background-color: #ffffff;
      font-family: Arial, Helvetica, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .diagram-container {
      background: #ffffff;
      padding: 20px;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    }
    .diagram-title {
      text-align: center;
      font-size: 16px;
      font-weight: bold;
      color: #1e293b;
      margin-bottom: 20px;
      letter-spacing: 0.5px;
    }
  </style>
</head>
<body>
  <div class="diagram-container">
    <div class="diagram-title">ACTIVITY DIAGRAM SISTEM BERJALAN (EVALUASI KINERJA KARYAWAN)</div>
    <svg width="960" height="740" viewBox="0 0 960 740" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
          <feDropShadow dx="1" dy="2" stdDeviation="1.5" flood-color="#000000" flood-opacity="0.12" />
        </filter>
        <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#475569" />
        </marker>
        <marker id="arrow-red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626" />
        </marker>
      </defs>

      <!-- SWIMLANE BACKGROUND & BORDERS -->
      <!-- Lane 1: Supervisor -->
      <rect x="20" y="20" width="300" height="690" fill="#fcfdfe" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="20" y="20" width="300" height="38" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="170" y="44" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Supervisor Lapangan (PT ISS)</text>

      <!-- Lane 2: HRD ISS -->
      <rect x="320" y="20" width="320" height="690" fill="#fcfdfe" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="320" y="20" width="320" height="38" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="480" y="44" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Personalia / HRD (PT ISS)</text>

      <!-- Lane 3: Branch Manager Prodia -->
      <rect x="640" y="20" width="300" height="690" fill="#fcfdfe" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="640" y="20" width="300" height="38" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="790" y="44" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Branch Manager (Prodia Kebayoran)</text>

      <!-- ================= LANE 1 ELEMENTS ================= -->
      <!-- Start Node -->
      <circle cx="170" cy="85" r="12" fill="#1e293b" />

      <!-- Step 1: Terima Blangko -->
      <rect x="75" y="130" width="190" height="48" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="170" y="150" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Menerima Blangko Penilaian</text>
      <text x="170" y="165" font-size="11" fill="#475569" text-anchor="middle">Fisik (Hardcopy)</text>

      <!-- Step 2: Mengamati Kinerja -->
      <rect x="75" y="215" width="190" height="52" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="170" y="236" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Mengamati Kinerja Harian</text>
      <text x="170" y="252" font-size="11" fill="#475569" text-anchor="middle">Personel CS &amp; Messenger</text>

      <!-- Step 3: Tuliskan Skor -->
      <rect x="75" y="305" width="190" height="48" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="170" y="325" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Menuliskan Skor Mentah</text>
      <text x="170" y="340" font-size="11" fill="#475569" text-anchor="middle">pada Lembaran Kertas</text>

      <!-- Step 4: Menyerahkan Berkas -->
      <rect x="75" y="390" width="190" height="48" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="170" y="410" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Menyerahkan Berkas Fisik</text>
      <text x="170" y="425" font-size="11" fill="#475569" text-anchor="middle">ke Kantor HR ISS</text>

      <!-- ================= LANE 2 ELEMENTS ================= -->
      <!-- Step 5: Input Ulang Excel -->
      <rect x="385" y="390" width="190" height="48" rx="8" ry="8" fill="#d5e8d4" stroke="#82b366" stroke-width="1.5" filter="url(#shadow)" />
      <text x="480" y="410" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Input Ulang Skor ke Dalam</text>
      <text x="480" y="425" font-size="11" fill="#475569" text-anchor="middle">Lembar Kerja Excel</text>

      <!-- Step 6: Hitung Rata-rata -->
      <rect x="385" y="475" width="190" height="52" rx="8" ry="8" fill="#d5e8d4" stroke="#82b366" stroke-width="1.5" filter="url(#shadow)" />
      <text x="480" y="496" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Menghitung Rata-rata Skor</text>
      <text x="480" y="512" font-size="11" fill="#475569" text-anchor="middle">(Tanpa Pembobotan MOORA)</text>

      <!-- Step 7: Buat Draf Rekap -->
      <rect x="385" y="565" width="190" height="48" rx="8" ry="8" fill="#d5e8d4" stroke="#82b366" stroke-width="1.5" filter="url(#shadow)" />
      <text x="480" y="585" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Mencetak Draf Rekapitulasi</text>
      <text x="480" y="600" font-size="11" fill="#475569" text-anchor="middle">Daftar Nominasi Karyawan</text>

      <!-- Step 9: Terbitkan SK (di Lane 2 bawah) -->
      <rect x="385" y="640" width="190" height="48" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="480" y="660" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Menerbitkan SK Insentif</text>
      <text x="480" y="675" font-size="11" fill="#475569" text-anchor="middle">&amp; Perpanjangan Kontrak</text>

      <!-- End Node (Tepat Presisi di Tengah Swimlane Supervisor cx = 170) -->
      <circle cx="170" cy="664" r="14" fill="#ffffff" stroke="#1e293b" stroke-width="2" />
      <circle cx="170" cy="664" r="8" fill="#1e293b" />
      <text x="170" y="694" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">Selesai</text>

      <!-- ================= LANE 3 ELEMENTS ================= -->
      <!-- Step 8: Periksa Draf -->
      <rect x="695" y="475" width="190" height="48" rx="8" ry="8" fill="#ffe6cc" stroke="#d79b00" stroke-width="1.5" filter="url(#shadow)" />
      <text x="790" y="495" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Memeriksa Draf Nominasi</text>
      <text x="790" y="510" font-size="11" fill="#475569" text-anchor="middle">Hasil Evaluasi Kerja</text>

      <!-- Decision Diamond: Disetujui? -->
      <polygon points="790,550 855,585 790,620 725,585" fill="#fff2cc" stroke="#d6b656" stroke-width="1.5" filter="url(#shadow)" />
      <text x="790" y="589" font-size="11.5" font-weight="bold" fill="#854d0e" text-anchor="middle">Disetujui?</text>

      <!-- Step: Tanda Tangan -->
      <rect x="695" y="640" width="190" height="48" rx="8" ry="8" fill="#ffe6cc" stroke="#d79b00" stroke-width="1.5" filter="url(#shadow)" />
      <text x="790" y="660" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Menandatangani Lembar</text>
      <text x="790" y="675" font-size="11" fill="#475569" text-anchor="middle">Pengesahan Rekapitulasi</text>

      <!-- ================= CONNECTOR ARROWS ================= -->
      <!-- Start -> Step 1 -->
      <line x1="170" y1="97" x2="170" y2="130" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 1 -> Step 2 -->
      <line x1="170" y1="178" x2="170" y2="215" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 2 -> Step 3 -->
      <line x1="170" y1="267" x2="170" y2="305" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 3 -> Step 4 -->
      <line x1="170" y1="353" x2="170" y2="390" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 4 -> Step 5 (Cross Lane to HR) -->
      <line x1="265" y1="414" x2="385" y2="414" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 5 -> Step 6 -->
      <line x1="480" y1="438" x2="480" y2="475" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 6 -> Step 7 -->
      <line x1="480" y1="527" x2="480" y2="565" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 7 -> Step 8 (Cross Lane to BM) -->
      <polyline points="575,589 618,589 618,499 695,499" fill="none" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 8 -> Decision -->
      <line x1="790" y1="523" x2="790" y2="550" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Decision -> Tidak (Loop back to Step 2) -->
      <polyline points="855,585 910,585 910,241 265,241" fill="none" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arrow-red)" />
      <!-- Label Tidak -->
      <rect x="862" y="573" width="42" height="18" rx="3" fill="#ffffff" stroke="#fca5a5" stroke-width="1" />
      <text x="883" y="586" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">Tidak</text>

      <!-- Decision -> Ya (Down to Tanda Tangan) -->
      <line x1="790" y1="620" x2="790" y2="640" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />
      <!-- Label Ya -->
      <rect x="795" y="621" width="26" height="16" rx="3" fill="#ffffff" stroke="#86efac" stroke-width="1" />
      <text x="808" y="633" font-size="10" font-weight="bold" fill="#16a34a" text-anchor="middle">Ya</text>

      <!-- Tanda Tangan -> Terbitkan SK (Back to HR) -->
      <line x1="695" y1="664" x2="575" y2="664" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Terbitkan SK -> End Node (Menuju cx = 170, berhenti di r=14 -> x=184) -->
      <line x1="385" y1="664" x2="184" y2="664" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />
    </svg>
  </div>
</body>
</html>
"""

html_usulan = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Activity Diagram Sistem Usulan</title>
  <style>
    body {
      margin: 0;
      padding: 30px;
      background-color: #ffffff;
      font-family: Arial, Helvetica, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .diagram-container {
      background: #ffffff;
      padding: 20px;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.06);
    }
    .diagram-title {
      text-align: center;
      font-size: 16px;
      font-weight: bold;
      color: #1e293b;
      margin-bottom: 20px;
      letter-spacing: 0.5px;
    }
  </style>
</head>
<body>
  <div class="diagram-container">
    <div class="diagram-title">ACTIVITY DIAGRAM SISTEM USULAN (SPK METODE MOORA)</div>
    <svg width="980" height="840" viewBox="0 0 980 840" xmlns="http://www.w3.org/2000/svg">
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
      </defs>

      <!-- SWIMLANE BACKGROUND & BORDERS -->
      <!-- Lane 1: Supervisor -->
      <rect x="20" y="20" width="300" height="790" fill="#fcfdfe" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="20" y="20" width="300" height="38" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="170" y="44" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Supervisor Operasional (PT ISS)</text>

      <!-- Lane 2: Sistem SPK MOORA -->
      <rect x="320" y="20" width="340" height="790" fill="#f8fafc" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="320" y="20" width="340" height="38" fill="#e0e7ff" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="490" y="44" font-size="13" font-weight="bold" fill="#312e81" text-anchor="middle">Sistem SPK MOORA (Web Next.js)</text>

      <!-- Lane 3: Branch Manager Prodia -->
      <rect x="660" y="20" width="300" height="790" fill="#fcfdfe" stroke="#6c8ebf" stroke-width="1.5" />
      <rect x="660" y="20" width="300" height="38" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" />
      <text x="810" y="44" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Branch Manager (Prodia Kebayoran)</text>

      <!-- ================= LANE 1 ELEMENTS ================= -->
      <!-- Start Node -->
      <circle cx="170" cy="85" r="12" fill="#1e293b" />

      <!-- Step 1: Login Akun -->
      <rect x="75" y="125" width="190" height="46" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="170" y="145" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Akses Web SPK &amp; Login Akun</text>
      <text x="170" y="160" font-size="11" fill="#475569" text-anchor="middle">(Hak Akses Supervisor)</text>

      <!-- Step 2: Pilih Kategori -->
      <rect x="75" y="205" width="190" height="48" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="170" y="225" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Pilih Kategori Independen</text>
      <text x="170" y="240" font-size="11" fill="#475569" text-anchor="middle">(Cleaning Service / Messenger)</text>

      <!-- Step 3: Input Skor -->
      <rect x="75" y="285" width="190" height="48" rx="8" ry="8" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.5" filter="url(#shadow)" />
      <text x="170" y="305" font-size="11.5" font-weight="600" fill="#0f172a" text-anchor="middle">Input Nilai Skor Mentah</text>
      <text x="170" y="320" font-size="11" fill="#475569" text-anchor="middle">Karyawan (Skala 1 - 100)</text>

      <!-- Step 4: Klik Tombol Sinkronkan -->
      <rect x="75" y="365" width="190" height="48" rx="8" ry="8" fill="#d5e8d4" stroke="#82b366" stroke-width="1.5" filter="url(#shadow)" />
      <text x="170" y="385" font-size="11.5" font-weight="600" fill="#065f46" text-anchor="middle">Klik Tombol Aksi</text>
      <text x="170" y="400" font-size="11" font-weight="bold" fill="#047857" text-anchor="middle">"Sinkronkan MOORA"</text>

      <!-- ================= LANE 2 ELEMENTS (ENGINE) ================= -->
      <!-- Step 5: Validasi Data -->
      <rect x="395" y="365" width="190" height="48" rx="8" ry="8" fill="#ffffff" stroke="#6366f1" stroke-width="1.5" filter="url(#shadow)" />
      <text x="490" y="385" font-size="11.5" font-weight="600" fill="#1e1b4b" text-anchor="middle">Validasi Kelengkapan Nilai</text>
      <text x="490" y="400" font-size="11" fill="#64748b" text-anchor="middle">&amp; Bobot Kriteria Aktif</text>

      <!-- Step 6: Matriks X & Normalisasi R -->
      <rect x="395" y="445" width="190" height="52" rx="8" ry="8" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5" filter="url(#shadow)" />
      <text x="490" y="465" font-size="11.5" font-weight="600" fill="#1e1b4b" text-anchor="middle">Bentuk Matriks Keputusan X</text>
      <text x="490" y="482" font-size="11" fill="#4338ca" text-anchor="middle">&amp; Normalisasi Rasio Matriks R</text>

      <!-- Step 7: Matriks V & Optimasi Yi -->
      <rect x="395" y="530" width="190" height="52" rx="8" ry="8" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5" filter="url(#shadow)" />
      <text x="490" y="550" font-size="11.5" font-weight="600" fill="#1e1b4b" text-anchor="middle">Hitung Matriks Terbobot V</text>
      <text x="490" y="567" font-size="11" font-weight="bold" fill="#4338ca" text-anchor="middle">&amp; Skor Optimasi Yi = Benefit - Cost</text>

      <!-- Step 8: Ranking & Simpan DB -->
      <rect x="395" y="615" width="190" height="52" rx="8" ry="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5" filter="url(#shadow)" />
      <text x="490" y="635" font-size="11.5" font-weight="600" fill="#1e3a8a" text-anchor="middle">Urutkan Ranking &amp; Sorot Juara</text>
      <text x="490" y="652" font-size="11" fill="#2563eb" text-anchor="middle">Simpan ke DB SQLite (Prisma)</text>

      <!-- Step 9: Sajikan Data Real-time -->
      <rect x="395" y="700" width="190" height="48" rx="8" ry="8" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5" filter="url(#shadow)" />
      <text x="490" y="720" font-size="11.5" font-weight="600" fill="#1e3a8a" text-anchor="middle">Sajikan Klasemen Real-time</text>
      <text x="490" y="735" font-size="11" fill="#64748b" text-anchor="middle">&amp; 4 Tab Transparansi Audit</text>

      <!-- ================= LANE 3 ELEMENTS (BRANCH MANAGER) ================= -->
      <!-- Step 10: Tinjau Klasemen & Audit -->
      <rect x="715" y="615" width="190" height="52" rx="8" ry="8" fill="#ffe6cc" stroke="#d79b00" stroke-width="1.5" filter="url(#shadow)" />
      <text x="810" y="635" font-size="11.5" font-weight="600" fill="#7c2d12" text-anchor="middle">Login &amp; Tinjau Klasemen</text>
      <text x="810" y="652" font-size="11" fill="#9a3412" text-anchor="middle">Serta 4 Tab Transparansi MOORA</text>

      <!-- Decision Diamond: Ambang Batas Yi -->
      <polygon points="810,695 885,730 810,765 735,730" fill="#fff2cc" stroke="#d6b656" stroke-width="1.5" filter="url(#shadow)" />
      <text x="810" y="726" font-size="11" font-weight="bold" fill="#854d0e" text-anchor="middle">Skor Yi &gt;=</text>
      <text x="810" y="740" font-size="10.5" font-weight="bold" fill="#854d0e" text-anchor="middle">Ambang Batas?</text>

      <!-- Path Tidak: Pembinaan Tambahan -->
      <rect x="680" y="780" width="120" height="36" rx="6" ry="6" fill="#fef2f2" stroke="#f87171" stroke-width="1.2" />
      <text x="740" y="798" font-size="10" font-weight="600" fill="#991b1b" text-anchor="middle">Pembinaan / Pelatihan</text>
      <text x="740" y="809" font-size="9" fill="#7f1d1d" text-anchor="middle">Ulang Karyawan</text>

      <!-- Path Ya: Validasi & Cetak SK PDF -->
      <rect x="825" y="780" width="125" height="36" rx="6" ry="6" fill="#ecfdf5" stroke="#34d399" stroke-width="1.2" />
      <text x="887" y="798" font-size="10" font-weight="600" fill="#065f46" text-anchor="middle">Cetak Dokumen SK</text>
      <text x="887" y="809" font-size="9" fill="#047857" text-anchor="middle">Insentif Format PDF</text>

      <!-- End Node -->
      <circle cx="810" cy="800" r="12" fill="#ffffff" stroke="#1e293b" stroke-width="1.8" />
      <circle cx="810" cy="800" r="7" fill="#1e293b" />

      <!-- ================= CONNECTOR ARROWS ================= -->
      <!-- Start -> Step 1 -->
      <line x1="170" y1="97" x2="170" y2="125" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 1 -> Step 2 -->
      <line x1="170" y1="171" x2="170" y2="205" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 2 -> Step 3 -->
      <line x1="170" y1="253" x2="170" y2="285" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 3 -> Step 4 -->
      <line x1="170" y1="333" x2="170" y2="365" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 4 -> Step 5 (Cross Lane to Engine) -->
      <line x1="265" y1="389" x2="395" y2="389" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arrow-blue)" />

      <!-- Step 5 -> Step 6 -->
      <line x1="490" y1="413" x2="490" y2="445" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 6 -> Step 7 -->
      <line x1="490" y1="497" x2="490" y2="530" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 7 -> Step 8 -->
      <line x1="490" y1="582" x2="490" y2="615" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 8 -> Step 9 -->
      <line x1="490" y1="667" x2="490" y2="700" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 8 -> Step 10 (Cross Lane to BM) -->
      <line x1="585" y1="641" x2="715" y2="641" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Step 10 -> Decision -->
      <line x1="810" y1="667" x2="810" y2="695" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)" />

      <!-- Decision -> Tidak (Left branch) -->
      <polyline points="735,730 710,730 710,780" fill="none" stroke="#dc2626" stroke-width="1.5" marker-end="url(#arrow)" />
      <rect x="702" y="740" width="36" height="15" rx="3" fill="#ffffff" stroke="#fca5a5" stroke-width="1" />
      <text x="720" y="751" font-size="9" font-weight="bold" fill="#dc2626" text-anchor="middle">Tidak</text>

      <!-- Decision -> Ya (Right branch) -->
      <polyline points="885,730 910,730 910,780" fill="none" stroke="#16a34a" stroke-width="1.5" marker-end="url(#arrow)" />
      <rect x="893" y="740" width="22" height="15" rx="3" fill="#ffffff" stroke="#86efac" stroke-width="1" />
      <text x="904" y="751" font-size="9" font-weight="bold" fill="#16a34a" text-anchor="middle">Ya</text>

      <!-- Path Tidak -> End -->
      <polyline points="740,816 740,828 795,828 798,806" fill="none" stroke="#475569" stroke-width="1.2" marker-end="url(#arrow)" />

      <!-- Path Ya -> End -->
      <polyline points="887,816 887,828 825,828 822,806" fill="none" stroke="#475569" stroke-width="1.2" marker-end="url(#arrow)" />
    </svg>
  </div>
</body>
</html>
"""

with open("/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_berjalan.html", "w", encoding="utf-8") as f:
    f.write(html_berjalan)

with open("/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_usulan.html", "w", encoding="utf-8") as f:
    f.write(html_usulan)

print("HTML files generated successfully.")
