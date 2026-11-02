#!/usr/bin/env python3
"""
generate_wireframes.py
Generates 7 Pristine Grayscale/Black & White Wireframes matching the exact UI layout:
1. wireframe_01_login.svg / png
2. wireframe_02_dashboard.svg / png
3. wireframe_03_karyawan.svg / png
4. wireframe_04_kriteria.svg / png
5. wireframe_05_penilaian.svg / png
6. wireframe_06_moora.svg / png
7. wireframe_07_laporan_sk.svg / png
"""

import os
import subprocess
import shutil

OUT_DIR = "public/diagrams"
ARTIFACT_DIR = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/e6c145f5-ba78-4f4a-bc31-4712ef0b13ed"

W = 1200
H = 800

def get_browser_shell(window_title, breadcrumb_title, current_url, active_nav, inner_content, annotations=None):
    c = []
    c.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <filter id="badge-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="1" dy="1" stdDeviation="1" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="{W}" height="{H}" fill="#ffffff"/>

  <!-- Browser Window Frame -->
  <rect x="10" y="10" width="{W - 20}" height="{H - 20}" rx="6" fill="#ffffff" stroke="#111827" stroke-width="1.8"/>

  <!-- Browser Title Bar (Y: 10 - 48) -->
  <path d="M 10 10 L {W - 10} 10 L {W - 10} 48 L 10 48 Z" fill="#f3f4f6" stroke="#111827" stroke-width="1.8"/>
  <circle cx="32" cy="29" r="5" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <circle cx="48" cy="29" r="5" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <circle cx="64" cy="29" r="5" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>

  <!-- URL Address Bar -->
  <rect x="100" y="18" width="540" height="22" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="115" y="34" font-family="'Courier New', monospace" font-size="11" fill="#374151">🔒 {current_url}</text>

  <!-- Title Text in Window Header -->
  <text x="{W - 30}" y="33" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" text-anchor="end" fill="#111827">{window_title}</text>
  <line x1="10" y1="48" x2="{W - 10}" y2="48" stroke="#111827" stroke-width="1.8"/>
''')

    if active_nav == "none":
        c.append(inner_content)
    else:
        # Standard App Layout with Sidebar (W: 220, X: 10..230)
        c.append(f'''
  <!-- ================= SIDEBAR NAVIGATION ================= -->
  <rect x="10" y="48" width="220" height="{H - 58}" fill="#f9fafb" stroke="#111827" stroke-width="1.8"/>
  
  <!-- Brand / Logo Box -->
  <rect x="25" y="65" width="190" height="48" fill="#ffffff" stroke="#111827" stroke-width="1.4" rx="4"/>
  <text x="35" y="86" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="bold" fill="#111827">ISS — SPK MOORA</text>
  <text x="35" y="102" font-family="Arial, Helvetica, sans-serif" font-size="9.5" fill="#4b5563">Site Prodia Kebayoran</text>

  <!-- Navigation Menu List -->
  <g id="sidebar-nav" font-family="Arial, Helvetica, sans-serif" font-size="12">
''')
        nav_items = [
            ("dashboard", "Dashboard", 135),
            ("employees", "Data Karyawan", 175),
            ("criteria", "Kriteria & Bobot", 215),
            ("assessment", "Input Penilaian", 255),
            ("moora", "Hitung MOORA", 295),
            ("reports", "Laporan & SK", 335),
        ]
        
        for key, label, y in nav_items:
            is_active = (key == active_nav)
            bg = "#111827" if is_active else "#ffffff"
            text_color = "#ffffff" if is_active else "#111827"
            weight = "bold" if is_active else "normal"
            c.append(f'''    <!-- Nav Item: {key} -->
    <rect x="25" y="{y}" width="190" height="32" rx="4" fill="{bg}" stroke="#111827" stroke-width="1.2"/>
    <text x="40" y="{y + 20}" font-weight="{weight}" fill="{text_color}">{label}</text>''')

        # Sidebar Bottom Profile
        c.append(f'''    <!-- User Profile Box -->
    <rect x="25" y="680" width="190" height="90" fill="#ffffff" stroke="#111827" stroke-width="1.2" rx="4"/>
    <circle cx="45" cy="710" r="12" fill="#e5e7eb" stroke="#111827" stroke-width="1.2"/>
    <text x="45" y="714" font-size="10" font-weight="bold" text-anchor="middle" fill="#111827">SA</text>
    <text x="65" y="707" font-weight="bold" font-size="11" fill="#111827">Septo Aribowo</text>
    <text x="65" y="722" font-size="9.5" fill="#4b5563">Site Supervisor (ISS)</text>
    
    <rect x="35" y="736" width="170" height="24" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="120" y="752" font-size="10" font-weight="bold" text-anchor="middle" fill="#111827">[ Keluar / Logout ]</text>
  </g>

  <!-- ================= TOP ACTION BAR (Y: 48 - 105) ================= -->
  <line x1="230" y1="105" x2="{W - 10}" y2="105" stroke="#111827" stroke-width="1.5"/>
  <rect x="230" y="48" width="{W - 240}" height="57" fill="#ffffff"/>
  
  <!-- Breadcrumb / Header Title -->
  <text x="255" y="78" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="bold" fill="#111827">{breadcrumb_title}</text>
  <text x="255" y="94" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#6b7280">Sistem Pendukung Keputusan Kinerja Tenaga Kerja Outsourcing</text>

  <!-- Top Right Division Filter & Period Selector -->
  <!-- Divisi Switcher -->
  <rect x="790" y="62" width="190" height="30" rx="4" fill="#f3f4f6" stroke="#111827" stroke-width="1.2"/>
  <rect x="792" y="64" width="95" height="26" rx="3" fill="#111827"/>
  <text x="839" y="81" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">Cleaning</text>
  <text x="935" y="81" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" text-anchor="middle" fill="#111827">Messenger</text>

  <!-- Periode Dropdown -->
  <rect x="990" y="62" width="180" height="30" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="1005" y="81" font-family="Arial, Helvetica, sans-serif" font-size="10.5" fill="#111827">📅 Q3 2026 ▾</text>

  <!-- ================= MAIN CONTENT VIEWPORT ================= -->
  <g id="main-content">
{inner_content}
  </g>
''')

    if annotations:
        c.append('  <!-- ================= ANNOTATION CALLOUTS ================= -->')
        c.append('  <g id="annotations">')
        for ax, ay, num in annotations:
            c.append(f'''    <circle cx="{ax}" cy="{ay}" r="11" fill="#111827" stroke="#ffffff" stroke-width="1.8" filter="url(#badge-shadow)"/>
    <text x="{ax}" y="{ay + 4}" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">{num}</text>''')
        c.append('  </g>')

    c.append('</svg>')
    return "\n".join(c)

# -------------------------------------------------------------
# 1. WIREFRAME 01: LOGIN SCREEN
# -------------------------------------------------------------
def build_wf_01():
    inner = f'''
  <!-- Centered Login Box (W: 420, H: 490) -->
  <rect x="390" y="150" width="420" height="490" rx="8" fill="#ffffff" stroke="#111827" stroke-width="2"/>
  <rect x="390" y="150" width="420" height="70" rx="8 8 0 0" fill="#f3f4f6" stroke="#111827" stroke-width="1.5"/>
  
  <text x="600" y="185" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#111827">MASUK SISTEM SPK MOORA</text>
  <text x="600" y="204" font-family="Arial, Helvetica, sans-serif" font-size="11" text-anchor="middle" fill="#4b5563">PT ISS Indonesia — Site Prodia Kebayoran</text>

  <!-- Form Fields -->
  <text x="425" y="255" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">NIP / Nama Pengguna:</text>
  <rect x="425" y="265" width="350" height="36" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  <text x="440" y="288" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#4b5563">septo.aribowo</text>

  <text x="425" y="330" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">Kata Sandi (Password):</text>
  <rect x="425" y="340" width="350" height="36" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  <text x="440" y="364" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#111827">••••••••••••</text>

  <text x="425" y="405" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">Hak Akses (Peran):</text>
  <rect x="425" y="415" width="350" height="36" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  <text x="440" y="438" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#111827">Site Supervisor (Operasional Lapangan)</text>
  <text x="755" y="438" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">▾</text>

  <rect x="425" y="475" width="14" height="14" rx="2" fill="#111827" stroke="#111827" stroke-width="1"/>
  <text x="429" y="486" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#ffffff">✓</text>
  <text x="448" y="487" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#374151">Ingat kredensial login pada perangkat ini</text>

  <rect x="425" y="520" width="350" height="42" rx="4" fill="#111827" stroke="#111827" stroke-width="1.4"/>
  <text x="600" y="546" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="bold" text-anchor="middle" fill="#ffffff">MASUK KE DASHBOARD →</text>

  <text x="600" y="595" font-family="Arial, Helvetica, sans-serif" font-size="10" font-style="italic" text-anchor="middle" fill="#6b7280">Autentikasi terenkripsi SSL 256-bit — Khusus Personel Berwenang</text>
  <text x="600" y="615" font-family="Arial, Helvetica, sans-serif" font-size="9.5" text-anchor="middle" fill="#9ca3af">© 2026 Facility Services PT ISS Indonesia</text>
'''
    ann = [(390, 150, "1"), (795, 283, "2"), (795, 358, "3"), (795, 433, "4"), (795, 541, "5")]
    return get_browser_shell("Wireframe 01: Login & Autentikasi Sistem", "LOGIN", "https://spk-moora.iss.co.id/auth/login", "none", inner, ann)

# -------------------------------------------------------------
# 2. WIREFRAME 02: DASHBOARD UTAMA
# -------------------------------------------------------------
def build_wf_02():
    inner = f'''
  <!-- 4 Stat Metric Cards (Y: 120 - 185) -->
  <g font-family="Arial, Helvetica, sans-serif">
    <rect x="250" y="120" width="215" height="68" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
    <text x="265" y="142" font-size="10.5" fill="#4b5563">TOTAL KARYAWAN AKTIF</text>
    <text x="265" y="170" font-size="22" font-weight="bold" fill="#111827">20 Personel</text>
    
    <rect x="480" y="120" width="215" height="68" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
    <text x="495" y="142" font-size="10.5" fill="#4b5563">KRITERIA PENILAIAN</text>
    <text x="495" y="170" font-size="22" font-weight="bold" fill="#111827">5 Indikator (100%)</text>
    
    <rect x="710" y="120" width="220" height="68" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
    <text x="725" y="142" font-size="10.5" fill="#4b5563">STATUS PERIODE KERJA</text>
    <text x="725" y="170" font-size="19" font-weight="bold" fill="#111827">Q3 - 2026 [Aktif]</text>
    
    <rect x="945" y="120" width="225" height="68" rx="4" fill="#111827" stroke="#111827" stroke-width="1.4"/>
    <text x="960" y="142" font-size="10.5" fill="#9ca3af">STATUS KOMPUTASI MOORA</text>
    <text x="960" y="170" font-size="18" font-weight="bold" fill="#ffffff">Tersinkronisasi ✓</text>
  </g>

  <!-- Left: Top Candidate Highlight Card -->
  <rect x="250" y="205" width="445" height="210" rx="6" fill="#f3f4f6" stroke="#111827" stroke-width="1.5"/>
  <rect x="250" y="205" width="445" height="34" rx="6 6 0 0" fill="#111827"/>
  <text x="265" y="227" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#ffffff">🏆 KARYAWAN TERBAIK #1 — DIVISI CLEANING</text>
  
  <circle cx="310" cy="295" r="34" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <text x="310" y="302" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#111827">RP</text>
  
  <text x="365" y="275" font-family="Arial, Helvetica, sans-serif" font-size="15" font-weight="bold" fill="#111827">Rendy Pratama (NIP: 2601)</text>
  <text x="365" y="295" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">Unit Penempatan: Prodia Kebayoran Baru</text>
  <text x="365" y="315" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">Nilai Akhir Optimasi MOORA: <tspan font-weight="bold" fill="#111827">Yi = 0.2817</tspan></text>
  
  <rect x="265" y="355" width="415" height="42" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="280" y="380" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#111827">Rekomendasi Legalitas: Penerima Insentif Kinerja Utama Kuartal III</text>

  <!-- Right: Chart Box -->
  <rect x="710" y="205" width="460" height="210" rx="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <rect x="710" y="205" width="460" height="34" rx="6 6 0 0" fill="#f3f4f6" stroke="#111827" stroke-width="1.2"/>
  <text x="725" y="227" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">📊 Grafik Distribusi Nilai Optimasi Yi (Top 5)</text>
  
  <g font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#111827">
    <text x="730" y="265">Rendy (0.282)</text>
    <rect x="830" y="254" width="280" height="14" fill="#111827"/>
    
    <text x="730" y="295">Siti A. (0.264)</text>
    <rect x="830" y="284" width="240" height="14" fill="#4b5563"/>
    
    <text x="730" y="325">Budi S. (0.241)</text>
    <rect x="830" y="314" width="200" height="14" fill="#6b7280"/>
    
    <text x="730" y="355">Agus W. (0.218)</text>
    <rect x="830" y="344" width="165" height="14" fill="#9ca3af"/>
    
    <text x="730" y="385">Dewi K. (0.195)</text>
    <rect x="830" y="374" width="130" height="14" fill="#d1d5db"/>
  </g>

  <!-- Bottom: Table Klasemen Ringkas (Y: 430 - 770) -->
  <rect x="250" y="430" width="920" height="340" rx="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <rect x="250" y="430" width="920" height="35" rx="6 6 0 0" fill="#f3f4f6" stroke="#111827" stroke-width="1.2"/>
  <text x="265" y="453" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">📋 Tabel Klasemen Rangking Kinerja Periode Kuartal III</text>
  
  <rect x="250" y="465" width="920" height="28" fill="#e5e7eb" stroke="#111827" stroke-width="1"/>
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">
    <text x="270" y="483">Rank</text>
    <text x="325" y="483">NIP</text>
    <text x="410" y="483">Nama Lengkap Karyawan</text>
    <text x="630" y="483">Divisi Unit</text>
    <text x="770" y="483">Nilai Optimasi (Yi)</text>
    <text x="920" y="483">Status Rekomendasi</text>
    <text x="1100" y="483">Aksi</text>
  </g>

  <g font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">
    <rect x="250" y="493" width="920" height="38" fill="#f3f4f6" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="517" font-weight="bold">#1</text>
    <text x="325" y="517" font-family="monospace">2601</text>
    <text x="410" y="517" font-weight="bold">Rendy Pratama</text>
    <text x="630" y="517">Cleaning Service</text>
    <text x="770" y="517" font-weight="bold">0.2817</text>
    <text x="920" y="517">[★ Insentif Utama]</text>
    <text x="1100" y="517">[ Detail ]</text>

    <rect x="250" y="531" width="920" height="38" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="555" font-weight="bold">#2</text>
    <text x="325" y="555" font-family="monospace">2602</text>
    <text x="410" y="555">Siti Aminah</text>
    <text x="630" y="555">Cleaning Service</text>
    <text x="770" y="555">0.2641</text>
    <text x="920" y="555">[ Insentif Madya ]</text>
    <text x="1100" y="555">[ Detail ]</text>

    <rect x="250" y="569" width="920" height="38" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="593" font-weight="bold">#3</text>
    <text x="325" y="593" font-family="monospace">2603</text>
    <text x="410" y="593">Budi Santoso</text>
    <text x="630" y="593">Cleaning Service</text>
    <text x="770" y="593">0.2409</text>
    <text x="920" y="593">[ Insentif Madya ]</text>
    <text x="1100" y="593">[ Detail ]</text>

    <rect x="250" y="607" width="920" height="38" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="631">#4</text>
    <text x="325" y="631" font-family="monospace">2604</text>
    <text x="410" y="631">Agus Wahyudi</text>
    <text x="630" y="631">Cleaning Service</text>
    <text x="770" y="631">0.2178</text>
    <text x="920" y="631">[ Memenuhi Syarat ]</text>
    <text x="1100" y="631">[ Detail ]</text>
  </g>
'''
    ann = [(465, 120, "1"), (695, 205, "2"), (1170, 205, "3"), (1170, 430, "4")]
    return get_browser_shell("Wireframe 02: Dashboard Utama & Klasemen Ringkasan", "DASHBOARD UTAMA", "https://spk-moora.iss.co.id/dashboard", "dashboard", inner, ann)

# -------------------------------------------------------------
# 3. WIREFRAME 03: MANAJEMEN DATA KARYAWAN
# -------------------------------------------------------------
def build_wf_03():
    inner = f'''
  <!-- Action Header Bar (Y: 120 - 165) -->
  <rect x="250" y="120" width="380" height="36" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="265" y="143" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">🔍 Cari NIP atau nama karyawan...</text>
  
  <rect x="645" y="120" width="160" height="36" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="660" y="143" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#111827">Status: Semua Aktif ▾</text>

  <rect x="975" y="120" width="195" height="36" rx="4" fill="#111827" stroke="#111827" stroke-width="1.4"/>
  <text x="1072" y="143" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">+ Tambah Karyawan Baru</text>

  <!-- Main Employee Table (Y: 175 - 770) -->
  <rect x="250" y="175" width="920" height="595" rx="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <rect x="250" y="175" width="920" height="36" rx="6 6 0 0" fill="#e5e7eb" stroke="#111827" stroke-width="1.2"/>
  
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">
    <text x="270" y="198">No</text>
    <text x="315" y="198">NIP</text>
    <text x="400" y="198">Nama Lengkap Karyawan</text>
    <text x="590" y="198">Divisi Penugasan</text>
    <text x="735" y="198">Unit Penempatan</text>
    <text x="890" y="198">Status</text>
    <text x="1010" y="198">Aksi Operasional</text>
  </g>

  <g font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">
    <rect x="250" y="211" width="920" height="42" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="237">1</text>
    <text x="315" y="237" font-family="monospace">2601</text>
    <text x="400" y="237" font-weight="bold">Rendy Pratama</text>
    <text x="590" y="237">Cleaning Service</text>
    <text x="735" y="237">Prodia Kebayoran Baru</text>
    <text x="890" y="237">[✓ Aktif]</text>
    <text x="1010" y="237">[ Ubah ]  [ Hapus ]</text>

    <rect x="250" y="253" width="920" height="42" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="279">2</text>
    <text x="315" y="279" font-family="monospace">2602</text>
    <text x="400" y="279" font-weight="bold">Siti Aminah</text>
    <text x="590" y="279">Cleaning Service</text>
    <text x="735" y="279">Prodia Kebayoran Baru</text>
    <text x="890" y="279">[✓ Aktif]</text>
    <text x="1010" y="279">[ Ubah ]  [ Hapus ]</text>

    <rect x="250" y="295" width="920" height="42" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="321">3</text>
    <text x="315" y="321" font-family="monospace">2603</text>
    <text x="400" y="321" font-weight="bold">Budi Santoso</text>
    <text x="590" y="321">Cleaning Service</text>
    <text x="735" y="321">Prodia Kebayoran Baru</text>
    <text x="890" y="321">[✓ Aktif]</text>
    <text x="1010" y="321">[ Ubah ]  [ Hapus ]</text>
  </g>

  <!-- Modal Inset Box: Form Tambah Karyawan -->
  <rect x="520" y="375" width="460" height="360" rx="8" fill="#ffffff" stroke="#111827" stroke-width="2"/>
  <rect x="520" y="375" width="460" height="40" rx="8 8 0 0" fill="#111827"/>
  <text x="540" y="400" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="bold" fill="#ffffff">FORM MODAL: TAMBAH DATA KARYAWAN</text>
  
  <g font-family="Arial, Helvetica, sans-serif" font-size="11">
    <text x="545" y="440" font-weight="bold">Nomor Induk Pegawai (NIP):</text>
    <rect x="545" y="448" width="410" height="30" rx="3" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
    <text x="555" y="468" fill="#4b5563">Contoh: 2611 (Wajib Unik)</text>

    <text x="545" y="500" font-weight="bold">Nama Lengkap Karyawan:</text>
    <rect x="545" y="508" width="410" height="30" rx="3" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
    <text x="555" y="528" fill="#4b5563">Masukkan nama lengkap sesuai KTP...</text>

    <text x="545" y="560" font-weight="bold">Divisi Penugasan:</text>
    <rect x="545" y="568" width="410" height="30" rx="3" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
    <text x="555" y="588" fill="#111827">Cleaning Service ▾</text>

    <rect x="740" y="670" width="100" height="34" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
    <text x="790" y="691" font-weight="bold" text-anchor="middle" fill="#111827">Batal</text>

    <rect x="855" y="670" width="100" height="34" rx="4" fill="#111827" stroke="#111827" stroke-width="1.2"/>
    <text x="905" y="691" font-weight="bold" text-anchor="middle" fill="#ffffff">Simpan</text>
  </g>
'''
    ann = [(630, 120, "1"), (1170, 120, "2"), (1170, 175, "3"), (980, 375, "4")]
    return get_browser_shell("Wireframe 03: Pengelolaan Data Karyawan", "DATA MASTER KARYAWAN", "https://spk-moora.iss.co.id/employees", "employees", inner, ann)

# -------------------------------------------------------------
# 4. WIREFRAME 04: PENGATURAN KRITERIA & BOBOT
# -------------------------------------------------------------
def build_wf_04():
    inner = f'''
  <!-- Warning / Info Alert Banner (Y: 120 - 170) -->
  <rect x="250" y="120" width="920" height="46" rx="4" fill="#f3f4f6" stroke="#111827" stroke-width="1.4"/>
  <text x="270" y="148" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">ℹ️ KETENTUAN PEMBOBOTAN: Akumulasi seluruh bobot kriteria wajib bernilai tepat 100% (atau total 1.00).</text>

  <!-- Criteria Table Card (Y: 185 - 770) -->
  <rect x="250" y="185" width="920" height="585" rx="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <rect x="250" y="185" width="920" height="36" rx="6 6 0 0" fill="#e5e7eb" stroke="#111827" stroke-width="1.2"/>
  
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">
    <text x="275" y="208">Kode</text>
    <text x="340" y="208">Nama Kriteria Evaluasi</text>
    <text x="560" y="208">Jenis / Tipe</text>
    <text x="700" y="208">Bobot (%)</text>
    <text x="820" y="208">Bobot Desimal (Wj)</text>
    <text x="980" y="208">Tindakan / Aksi</text>
  </g>

  <!-- Rows C1 to C5 -->
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">
    <rect x="250" y="221" width="920" height="52" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="252" font-weight="bold">C1</text>
    <text x="340" y="244" font-weight="bold">Disiplin &amp; Kehadiran Kerja</text>
    <text x="340" y="261" font-size="10" fill="#4b5563">Presensi fingerprint &amp; ketepatan waktu shift</text>
    <text x="560" y="252">[ Benefit ]</text>
    <text x="700" y="252" font-weight="bold">25 %</text>
    <text x="820" y="252">0.25</text>
    <text x="980" y="252">[ Edit Bobot ]</text>

    <rect x="250" y="273" width="920" height="52" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="304" font-weight="bold">C2</text>
    <text x="340" y="296" font-weight="bold">Kualitas Kebersihan &amp; SOP</text>
    <text x="340" y="313" font-size="10" fill="#4b5563">Kepatuhan standar operasional higienitas laboratorium</text>
    <text x="560" y="304">[ Benefit ]</text>
    <text x="700" y="304" font-weight="bold">20 %</text>
    <text x="820" y="304">0.20</text>
    <text x="980" y="304">[ Edit Bobot ]</text>

    <rect x="250" y="325" width="920" height="52" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="356" font-weight="bold">C3</text>
    <text x="340" y="348" font-weight="bold">Tanggung Jawab &amp; Inisiatif</text>
    <text x="340" y="365" font-size="10" fill="#4b5563">Penyelesaian checklist area tanpa pengawasan ketat</text>
    <text x="560" y="356">[ Benefit ]</text>
    <text x="700" y="356" font-weight="bold">20 %</text>
    <text x="820" y="356">0.20</text>
    <text x="980" y="356">[ Edit Bobot ]</text>

    <rect x="250" y="377" width="920" height="52" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="408" font-weight="bold">C4</text>
    <text x="340" y="400" font-weight="bold">Kerjasama Tim &amp; Sikap</text>
    <text x="340" y="417" font-size="10" fill="#4b5563">Komunikasi dengan staf medis Prodia &amp; rekan ISS</text>
    <text x="560" y="408">[ Benefit ]</text>
    <text x="700" y="408" font-weight="bold">20 %</text>
    <text x="820" y="408">0.20</text>
    <text x="980" y="408">[ Edit Bobot ]</text>

    <rect x="250" y="429" width="920" height="52" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="275" y="460" font-weight="bold">C5</text>
    <text x="340" y="452" font-weight="bold">Tingkat Komplain Pelanggan</text>
    <text x="340" y="469" font-size="10" fill="#4b5563">Keluhan dari pasien atau petugas klinik</text>
    <text x="560" y="460" font-weight="bold">[ COST ]</text>
    <text x="700" y="460" font-weight="bold">15 %</text>
    <text x="820" y="460">0.15</text>
    <text x="980" y="460">[ Edit Bobot ]</text>

    <rect x="250" y="481" width="920" height="42" fill="#111827"/>
    <text x="340" y="507" font-weight="bold" fill="#ffffff">TOTAL AKUMULASI BOBOT SELURUH PARAMETER</text>
    <text x="700" y="507" font-weight="bold" fill="#ffffff">100 %</text>
    <text x="820" y="507" font-weight="bold" fill="#ffffff">1.00 [VALID ✓]</text>
  </g>
'''
    ann = [(1170, 120, "1"), (1170, 185, "2"), (1050, 252, "3"), (1170, 481, "4")]
    return get_browser_shell("Wireframe 04: Pengaturan Kriteria & Bobot", "KRITERIA & BOBOT", "https://spk-moora.iss.co.id/criteria", "criteria", inner, ann)

# -------------------------------------------------------------
# 5. WIREFRAME 05: INPUT PENILAIAN KINERJA
# -------------------------------------------------------------
def build_wf_05():
    inner = f'''
  <!-- Action Filter Bar (Y: 120 - 165) -->
  <text x="255" y="145" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">Input Nilai Mentah (Skala 1 - 100 per Indikator)</text>
  
  <rect x="830" y="122" width="160" height="34" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="910" y="143" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">💾 Simpan Draf</text>

  <rect x="1000" y="122" width="170" height="34" rx="4" fill="#111827" stroke="#111827" stroke-width="1.4"/>
  <text x="1085" y="143" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#ffffff">Sinkronkan MOORA →</text>

  <!-- Matrix Scoring Table Card (Y: 175 - 770) -->
  <rect x="250" y="175" width="920" height="595" rx="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <rect x="250" y="175" width="920" height="36" rx="6 6 0 0" fill="#e5e7eb" stroke="#111827" stroke-width="1.2"/>
  
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">
    <text x="265" y="198">No</text>
    <text x="300" y="198">NIP</text>
    <text x="365" y="198">Nama Karyawan</text>
    <text x="530" y="198">C1 (25%)</text>
    <text x="620" y="198">C2 (20%)</text>
    <text x="710" y="198">C3 (20%)</text>
    <text x="800" y="198">C4 (20%)</text>
    <text x="890" y="198">C5 (15%)</text>
    <text x="990" y="198">Kelengkapan</text>
    <text x="1110" y="198">Aksi</text>
  </g>

  <!-- Table Rows with Input Boxes -->
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">
    <rect x="250" y="211" width="920" height="48" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="270" y="240">1</text>
    <text x="300" y="240" font-family="monospace">2601</text>
    <text x="365" y="240" font-weight="bold">Rendy Pratama</text>
    
    <rect x="525" y="223" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="552" y="240" text-anchor="middle" font-weight="bold">92</text>
    <rect x="615" y="223" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="642" y="240" text-anchor="middle" font-weight="bold">88</text>
    <rect x="705" y="223" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="732" y="240" text-anchor="middle" font-weight="bold">90</text>
    <rect x="795" y="223" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="822" y="240" text-anchor="middle" font-weight="bold">85</text>
    <rect x="885" y="223" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="912" y="240" text-anchor="middle" font-weight="bold">12</text>

    <text x="990" y="240">[✓ Lengkap]</text>
    <text x="1110" y="240">[ Kunci ]</text>

    <rect x="250" y="259" width="920" height="48" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="270" y="288">2</text>
    <text x="300" y="288" font-family="monospace">2602</text>
    <text x="365" y="288" font-weight="bold">Siti Aminah</text>
    
    <rect x="525" y="271" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="552" y="288" text-anchor="middle">88</text>
    <rect x="615" y="271" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="642" y="288" text-anchor="middle">90</text>
    <rect x="705" y="271" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="732" y="288" text-anchor="middle">85</text>
    <rect x="795" y="271" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="822" y="288" text-anchor="middle">86</text>
    <rect x="885" y="271" width="55" height="26" rx="3" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
    <text x="912" y="288" text-anchor="middle">15</text>

    <text x="990" y="288">[✓ Lengkap]</text>
    <text x="1110" y="288">[ Kunci ]</text>
  </g>
'''
    ann = [(990, 122, "1"), (1170, 122, "2"), (1170, 175, "3"), (1050, 240, "4")]
    return get_browser_shell("Wireframe 05: Formulir Matriks Input Penilaian", "INPUT PENILAIAN", "https://spk-moora.iss.co.id/assessment", "assessment", inner, ann)

# -------------------------------------------------------------
# 6. WIREFRAME 06: KOMPUTASI MOORA (4 LANGKAH AUDIT)
# -------------------------------------------------------------
def build_wf_06():
    inner = f'''
  <!-- 4 Step Pill Tabs (Y: 120 - 160) -->
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold">
    <rect x="250" y="120" width="220" height="34" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
    <text x="360" y="141" text-anchor="middle" fill="#111827">1. Matriks Keputusan (X)</text>

    <rect x="480" y="120" width="220" height="34" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
    <text x="590" y="141" text-anchor="middle" fill="#111827">2. Normalisasi Vektor (R)</text>

    <rect x="710" y="120" width="220" height="34" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
    <text x="820" y="141" text-anchor="middle" fill="#111827">3. Matriks Terbobot (V)</text>

    <rect x="940" y="120" width="230" height="34" rx="4" fill="#111827" stroke="#111827" stroke-width="1.4"/>
    <text x="1055" y="141" text-anchor="middle" fill="#ffffff">4. Nilai Akhir Optimasi (Yi) ★</text>
  </g>

  <!-- Formula Callout Box (Y: 170 - 235) -->
  <rect x="250" y="170" width="920" height="60" rx="4" fill="#f3f4f6" stroke="#111827" stroke-width="1.4"/>
  <text x="270" y="195" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">RUMUS TAHAP 4: Nilai Akhir Optimasi Multiobjektif (Yi)</text>
  <text x="270" y="215" font-family="'Times New Roman', Georgia, serif" font-size="14" font-weight="bold" fill="#111827">Yi = Σ (Bobot × Nilai Benefit) − Σ (Bobot × Nilai Cost)</text>

  <!-- Results Table (Y: 245 - 770) -->
  <rect x="250" y="245" width="920" height="525" rx="6" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <rect x="250" y="245" width="920" height="36" rx="6 6 0 0" fill="#e5e7eb" stroke="#111827" stroke-width="1.2"/>
  
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">
    <text x="270" y="268">Peringkat</text>
    <text x="345" y="268">NIP</text>
    <text x="425" y="268">Nama Karyawan Alternatif</text>
    <text x="650" y="268">Σ Nilai Benefit</text>
    <text x="780" y="268">Σ Nilai Cost</text>
    <text x="910" y="268">Nilai Optimasi (Yi)</text>
    <text x="1070" y="268">Keputusan</text>
  </g>

  <!-- Table Rows -->
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">
    <rect x="250" y="281" width="920" height="42" fill="#f3f4f6" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="285" y="307" font-weight="bold">#1</text>
    <text x="345" y="307" font-family="monospace">2601</text>
    <text x="425" y="307" font-weight="bold">Rendy Pratama</text>
    <text x="650" y="307">0.3142</text>
    <text x="780" y="307">0.0325</text>
    <text x="910" y="307" font-weight="bold">0.2817</text>
    <text x="1070" y="307">[★ Juara 1]</text>

    <rect x="250" y="323" width="920" height="42" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="285" y="349" font-weight="bold">#2</text>
    <text x="345" y="349" font-family="monospace">2602</text>
    <text x="425" y="349">Siti Aminah</text>
    <text x="650" y="349">0.2985</text>
    <text x="780" y="349">0.0344</text>
    <text x="910" y="349" font-weight="bold">0.2641</text>
    <text x="1070" y="349">[ Juara 2 ]</text>

    <rect x="250" y="365" width="920" height="42" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="285" y="391" font-weight="bold">#3</text>
    <text x="345" y="391" font-family="monospace">2603</text>
    <text x="425" y="391">Budi Santoso</text>
    <text x="650" y="391">0.2811</text>
    <text x="780" y="391">0.0402</text>
    <text x="910" y="391" font-weight="bold">0.2409</text>
    <text x="1070" y="391">[ Juara 3 ]</text>
  </g>
'''
    ann = [(1170, 120, "1"), (1170, 170, "2"), (1170, 245, "3")]
    return get_browser_shell("Wireframe 06: Komputasi MOORA (4 Langkah)", "KOMPUTASI MOORA", "https://spk-moora.iss.co.id/moora", "moora", inner, ann)

# -------------------------------------------------------------
# 7. WIREFRAME 07: LAPORAN & PENGESAHAN SK PDF
# -------------------------------------------------------------
def build_wf_07():
    inner = f'''
  <!-- Action Header Bar (Y: 120 - 165) -->
  <text x="255" y="145" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">Pratinjau Legal Dokumen Surat Keputusan (SK) Hasil MOORA</text>
  
  <rect x="760" y="122" width="200" height="34" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="860" y="143" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">📥 Unduh Berita Acara</text>

  <rect x="975" y="122" width="195" height="34" rx="4" fill="#111827" stroke="#111827" stroke-width="1.4"/>
  <text x="1072" y="143" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#ffffff">🖨️ Cetak Dokumen SK PDF</text>

  <!-- Sheet Paper Mockup (Center Y: 175 - 770) -->
  <rect x="360" y="175" width="700" height="595" fill="#ffffff" stroke="#111827" stroke-width="1.6" filter="drop-shadow(2px 3px 2px rgba(0,0,0,0.1))"/>
  
  <!-- Kop Surat -->
  <rect x="390" y="195" width="640" height="65" fill="#f9fafb" stroke="#111827" stroke-width="1"/>
  <text x="710" y="218" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="bold" text-anchor="middle" fill="#111827">PT ISS INDONESIA — FACILITY SERVICES</text>
  <text x="710" y="234" font-family="Arial, Helvetica, sans-serif" font-size="10.5" text-anchor="middle" fill="#4b5563">Site Operasional: Laboratorium Klinik Prodia Kebayoran Baru</text>
  <text x="710" y="248" font-family="Arial, Helvetica, sans-serif" font-size="9" text-anchor="middle" fill="#6b7280">Alamat: Jl. Kramat Pela No. 9, Kebayoran Baru, Jakarta Selatan | Telp: (021) 7279-0123</text>
  
  <line x1="390" y1="265" x2="1030" y2="265" stroke="#111827" stroke-width="1.8"/>

  <!-- Document Title -->
  <text x="710" y="290" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#111827">SURAT KEPUTUSAN PENETAPAN KINERJA TERBAIK</text>
  <text x="710" y="306" font-family="Arial, Helvetica, sans-serif" font-size="10" font-style="italic" text-anchor="middle" fill="#4b5563">Nomor: 048/SK-DIR/ISS-PRD/IX/2026</text>

  <!-- Paragraph Body -->
  <g font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#111827">
    <text x="400" y="335">Berdasarkan hasil komputasi sistem pendukung keputusan metode MOORA pada Periode Kuartal III - 2026,</text>
    <text x="400" y="350">maka diputuskan tenaga kerja outsourcing berkinerja terbaik dengan hak insentif resmi sebagai berikut:</text>
  </g>

  <!-- Table In SK -->
  <rect x="400" y="365" width="620" height="24" fill="#e5e7eb" stroke="#111827" stroke-width="1"/>
  <g font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" fill="#111827">
    <text x="415" y="381">Peringkat</text>
    <text x="475" y="381">NIP</text>
    <text x="545" y="381">Nama Lengkap</text>
    <text x="705" y="381">Divisi Kerja</text>
    <text x="815" y="381">Skor Optimasi Yi</text>
    <text x="915" y="381">Kategori Reward</text>
  </g>
  <rect x="400" y="389" width="620" height="26" fill="#f3f4f6" stroke="#e5e7eb" stroke-width="0.8"/>
  <g font-family="Arial, Helvetica, sans-serif" font-size="9.5" fill="#111827">
    <text x="420" y="405" font-weight="bold">#1</text>
    <text x="475" y="405" font-family="monospace">2601</text>
    <text x="545" y="405" font-weight="bold">Rendy Pratama</text>
    <text x="705" y="405">Cleaning Service</text>
    <text x="815" y="405" font-weight="bold">0.2817</text>
    <text x="915" y="405">Insentif Utama</text>
  </g>

  <!-- Signature Section -->
  <g font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#111827">
    <text x="450" y="465" text-anchor="middle">Disusun oleh:</text>
    <text x="450" y="478" text-anchor="middle" font-weight="bold">Site Supervisor ISS</text>
    <rect x="415" y="490" width="70" height="40" fill="#f3f4f6" stroke="#111827" stroke-dasharray="3,2"/>
    <text x="450" y="514" font-size="8" text-anchor="middle" fill="#6b7280">[ E-Sign ]</text>
    <text x="450" y="545" text-anchor="middle" font-weight="bold">Septo Aribowo</text>

    <text x="970" y="465" text-anchor="middle">Disahkan oleh:</text>
    <text x="970" y="478" text-anchor="middle" font-weight="bold">Branch Manager Prodia</text>
    <rect x="935" y="490" width="70" height="40" fill="#f3f4f6" stroke="#111827" stroke-dasharray="3,2"/>
    <text x="970" y="514" font-size="8" text-anchor="middle" fill="#6b7280">[ E-Sign ]</text>
    <text x="970" y="545" text-anchor="middle" font-weight="bold">Siska Darmayanti</text>
  </g>
'''
    ann = [(1060, 195, "1"), (1020, 365, "2"), (1005, 490, "3"), (1170, 122, "4")]
    return get_browser_shell("Wireframe 07: Pratinjau & Pengesahan Surat Keputusan (SK)", "LAPORAN & SK RESMI", "https://spk-moora.iss.co.id/reports", "reports", inner, ann)

# -------------------------------------------------------------
# Main Runner & Chrome Rasterizer
# -------------------------------------------------------------
wireframes = [
    ("wireframe_01_login", build_wf_01()),
    ("wireframe_02_dashboard", build_wf_02()),
    ("wireframe_03_karyawan", build_wf_03()),
    ("wireframe_04_kriteria", build_wf_04()),
    ("wireframe_05_penilaian", build_wf_05()),
    ("wireframe_06_moora", build_wf_06()),
    ("wireframe_07_laporan_sk", build_wf_07()),
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    print("Generating 7 Pristine Grayscale Wireframes...")
    for name, svg_content in wireframes:
        svg_file = os.path.join(OUT_DIR, f"{name}.svg")
        png_file = os.path.join(OUT_DIR, f"{name}.png")
        html_file = os.path.join(OUT_DIR, f"{name}.html")
        
        with open(svg_file, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"  [OK] Saved SVG: {svg_file}")
        
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
            print(f"  [OK] Rendered PNG: {png_file}")
            artifact_png = os.path.join(ARTIFACT_DIR, f"{name}.png")
            shutil.copyfile(png_file, artifact_png)
            print(f"  [OK] Copied to Artifact: {artifact_png}")
        else:
            print(f"  [ERR] Failed rendering {name}: {res.stderr}")

if __name__ == "__main__":
    main()
