#!/usr/bin/env python3
"""
Generate exact B&W Wireframes for Super Admin (HRD ISS Pusat):
1. Wireframe Login
2. Wireframe Master Karyawan
3. Wireframe Dashboard Super Admin
4. Wireframe Kriteria & Bobot

Using initial placeholders like Nama 1, Nama 2, NIP-001, etc.
"""

import os
import subprocess
import shutil

OUT_DIR = "public/diagrams"
ARTIFACT_DIR = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/e6c145f5-ba78-4f4a-bc31-4712ef0b13ed"

W = 1280
H = 820

# -------------------------------------------------------------------------
# Base Frame with Admin Sidebar (Dashboard, Kalkulasi, Input, Master Karyawan, Kriteria & Bobot, Laporan)
# -------------------------------------------------------------------------
def get_admin_base_frame(active_nav, inner_content, is_dashboard=False):
    navs = [
        ("dashboard", "Dashboard", "▦", 115, None),
        ("moora", "Kalkulasi MOORA", "📄", 155, None),
        ("input", "Input Nilai", "☑️", 195, None),
        ("karyawan", "Master Karyawan", "👥", 235, "HR"),
        ("kriteria", "Kriteria &amp; Bobot", "⚖", 275, "HR"),
        ("reports", "Laporan &amp; SK", "📑", 315, None),
    ]

    sidebar_items = []
    for key, label, icon, y, badge in navs:
        is_active = (key == active_nav)
        if is_active:
            sidebar_items.append(f'''    <!-- Active Nav: {key} -->
    <rect x="15" y="{y}" width="160" height="34" rx="8" fill="#111827"/>
    <text x="32" y="{y+21}" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#ffffff">{icon}  {label}</text>''')
            if badge:
                sidebar_items.append(f'<rect x="145" y="{y+9}" width="24" height="16" rx="4" fill="#ffffff"/><text x="157" y="{y+21}" font-family="Arial" font-size="8" font-weight="bold" text-anchor="middle" fill="#111827">{badge}</text>')
        else:
            sidebar_items.append(f'''    <!-- Nav: {key} -->
    <text x="32" y="{y+21}" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">{icon}  {label}</text>''')
            if badge:
                sidebar_items.append(f'<rect x="145" y="{y+9}" width="24" height="16" rx="4" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/><text x="157" y="{y+21}" font-family="Arial" font-size="8" font-weight="bold" text-anchor="middle" fill="#4b5563">{badge}</text>')

    sidebar_svg = "\n".join(sidebar_items)

    if is_dashboard:
        top_bar_right = '''  <!-- Right Actions (Dashboard Admin) -->
  <rect x="735" y="25" width="165" height="36" rx="18" fill="#111827"/>
  <text x="817" y="48" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#ffffff">🔄  Sinkronkan MOORA</text>

  <!-- Right Header (above executive panel) -->
  <circle cx="955" cy="43" r="14" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="955" y="47" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">⚙</text>

  <circle cx="995" cy="43" r="14" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="995" y="47" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">🔔</text>
  <circle cx="1005" cy="35" r="5" fill="#111827"/>
  <text x="1005" y="38" font-family="Arial" font-size="7" font-weight="bold" text-anchor="middle" fill="#ffffff">3</text>

  <g font-family="Arial, Helvetica, sans-serif">
    <text x="1145" y="38" font-size="11" font-weight="bold" text-anchor="end" fill="#111827">[Nama Admin]</text>
    <rect x="1075" y="44" width="70" height="15" rx="3" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/>
    <text x="1110" y="55" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#111827">SUPER ADMIN</text>
  </g>

  <circle cx="1175" cy="43" r="16" fill="#111827"/>
  <text x="1175" y="48" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">A</text>'''
    else:
        top_bar_right = '''  <!-- Right Actions (Full Width layout Admin) -->
  <rect x="840" y="25" width="165" height="36" rx="18" fill="#111827"/>
  <text x="922" y="48" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#ffffff">🔄  Sinkronkan MOORA</text>

  <circle cx="1030" cy="43" r="15" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="1030" y="47" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">⚙</text>

  <circle cx="1070" cy="43" r="15" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="1070" y="47" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">🔔</text>
  <circle cx="1080" cy="35" r="5" fill="#111827"/>
  <text x="1080" y="38" font-family="Arial" font-size="7" font-weight="bold" text-anchor="middle" fill="#ffffff">3</text>

  <circle cx="1115" cy="43" r="16" fill="#111827"/>
  <text x="1115" y="48" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">A</text>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <filter id="wf-shadow" x="-3%" y="-2%" width="106%" height="106%">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000000" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="{W}" height="{H}" fill="#ffffff"/>

  <!-- ================= LEFT SIDEBAR ================= -->
  <!-- Logo Section -->
  <circle cx="45" cy="45" r="14" fill="#ffffff" stroke="#111827" stroke-width="1.8"/>
  <text x="45" y="49" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" text-anchor="middle" fill="#111827">ISS</text>
  <text x="68" y="42" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="bold" fill="#111827">ISS Prodia</text>
  <text x="68" y="54" font-family="Arial, Helvetica, sans-serif" font-size="9" font-weight="bold" fill="#6b7280">SPK MOORA</text>

  <!-- Sidebar Navs -->
  <g id="sidebar-items">
{sidebar_svg}
  </g>

  <!-- Sidebar Logout -->
  <text x="32" y="775" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#4b5563">↪  Logout</text>

  <!-- Divider line -->
  <line x1="185" y1="15" x2="185" y2="{H-15}" stroke="#e5e7eb" stroke-width="1"/>

  <!-- ================= TOP APP BAR ================= -->
  <!-- Search Bar -->
  <rect x="210" y="25" width="370" height="36" rx="18" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="235" y="48" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#6b7280">🔍  Cari karyawan, NIP, atau indikator...</text>

{top_bar_right}

  <!-- ================= MAIN VIEWPORT ================= -->
  <g id="main-viewport">
{inner_content}
  </g>
</svg>'''

# -------------------------------------------------------------------------
# 1. WIREFRAME LOGIN
# -------------------------------------------------------------------------
def build_wf_login():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <filter id="wf-shadow-login" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="{W}" height="{H}" fill="#ffffff"/>

  <!-- Centered Login Card Container (W: 420, H: 450) -->
  <rect x="430" y="185" width="420" height="450" rx="20" fill="#ffffff" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow-login)"/>

  <!-- ISS Logo Badge in Login -->
  <circle cx="640" cy="245" r="28" fill="#ffffff" stroke="#111827" stroke-width="2"/>
  <text x="640" y="253" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="bold" text-anchor="middle" fill="#111827">ISS</text>

  <!-- Title & Subtitle -->
  <text x="640" y="305" font-family="Arial, Helvetica, sans-serif" font-size="17" font-weight="bold" text-anchor="middle" fill="#111827">SPK Kinerja Karyawan MOORA</text>
  <text x="640" y="325" font-family="Arial, Helvetica, sans-serif" font-size="10.5" text-anchor="middle" fill="#6b7280">PT ISS Indonesia - Evaluasi Mitra Laboratorium Prodia</text>
  <text x="640" y="340" font-family="Arial, Helvetica, sans-serif" font-size="10.5" text-anchor="middle" fill="#6b7280">Kebayoran</text>

  <!-- Form Username -->
  <text x="465" y="375" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#111827">Username:</text>
  <rect x="465" y="385" width="350" height="38" rx="8" fill="#ffffff" stroke="#9ca3af" stroke-width="1.2"/>
  <text x="480" y="409" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#9ca3af">[Username / NIP Pengguna]</text>

  <!-- Form Password -->
  <text x="465" y="445" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#111827">Password:</text>
  <rect x="465" y="455" width="350" height="38" rx="8" fill="#ffffff" stroke="#9ca3af" stroke-width="1.2"/>
  <text x="480" y="480" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#9ca3af">••••••••••••</text>

  <!-- Submit Button -->
  <rect x="465" y="515" width="350" height="42" rx="21" fill="#111827"/>
  <text x="640" y="541" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#ffffff">🔑  Masuk ke Sistem</text>
</svg>'''

# -------------------------------------------------------------------------
# 2. WIREFRAME MASTER KARYAWAN (Super Admin)
# -------------------------------------------------------------------------
def build_wf_master_karyawan():
    inner = f'''
  <!-- Hero Banner (Y: 80 - 220, W: 1040) -->
  <rect x="210" y="80" width="1040" height="140" rx="16" fill="#f3f4f6" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow)"/>
  <text x="240" y="125" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="bold" fill="#111827">Selamat Datang, [Nama Admin]!</text>
  <text x="240" y="150" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">Sistem evaluasi kinerja outsourcing PT ISS Indonesia di</text>
  <text x="240" y="167" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">[Unit Kerja / Laboratorium Klinik Prodia] siap ditinjau.</text>

  <!-- Button Audit Rumus MOORA in Hero -->
  <rect x="240" y="180" width="160" height="28" rx="14" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="320" y="198" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle" fill="#111827">✨ Audit Rumus MOORA</text>

  <!-- Medal Icon Graphic on right of Hero -->
  <circle cx="1180" cy="150" r="38" fill="#e5e7eb" stroke="#111827" stroke-width="1.4"/>
  <circle cx="1180" cy="144" r="14" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  <path d="M 1172 156 L 1166 178 L 1180 170 L 1194 178 L 1188 156 Z" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>

  <!-- ================= FORM TAMBAH DATA PERSONEL ================= -->
  <rect x="210" y="240" width="1040" height="100" rx="14" fill="#ffffff" stroke="#111827" stroke-width="1.4" filter="url(#wf-shadow)"/>
  <text x="235" y="265" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="bold" fill="#111827">Tambah Data Personel Baru</text>

  <!-- Input NIP -->
  <text x="235" y="288" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" fill="#111827">NIP:</text>
  <rect x="235" y="295" width="200" height="30" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
  <text x="245" y="314" font-family="Arial, Helvetica, sans-serif" font-size="10.5" fill="#9ca3af">[NIP-00X]</text>

  <!-- Input Nama Lengkap -->
  <text x="450" y="288" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" fill="#111827">Nama Lengkap:</text>
  <rect x="450" y="295" width="370" height="30" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
  <text x="460" y="314" font-family="Arial, Helvetica, sans-serif" font-size="10.5" fill="#9ca3af">[Nama Personel Baru]</text>

  <!-- Select Divisi -->
  <text x="835" y="288" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" fill="#111827">Divisi:</text>
  <rect x="835" y="295" width="180" height="30" rx="6" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
  <text x="845" y="314" font-family="Arial, Helvetica, sans-serif" font-size="10.5" fill="#111827">Cleaning Service  ▾</text>

  <!-- Button Tambah -->
  <rect x="1030" y="295" width="100" height="30" rx="15" fill="#111827"/>
  <text x="1080" y="314" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle" fill="#ffffff">+ Tambah</text>

  <!-- ================= DATATABLE KARYAWAN ================= -->
  <rect x="210" y="360" width="1040" height="420" rx="12" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  
  <!-- Table Header -->
  <rect x="210" y="360" width="1040" height="36" rx="12 12 0 0" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
  <g font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" fill="#4b5563">
    <text x="235" y="383">NIP</text>
    <text x="370" y="383">NAMA PERSONEL</text>
    <text x="630" y="383">DIVISI</text>
    <text x="850" y="383">PENEMPATAN</text>
    <text x="1170" y="383" text-anchor="middle">AKSI</text>
  </g>

  <!-- Row 1 -->
  <rect x="210" y="396" width="1040" height="50" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="235" y="426" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">NIP-001</text>
  <text x="370" y="426" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Nama 1</text>
  <text x="630" y="426" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Cleaning Service</text>
  <text x="850" y="426" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Prodia Kebayoran</text>
  <rect x="1155" y="411" width="30" height="26" rx="4" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/>
  <text x="1170" y="428" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">🗑️</text>

  <!-- Row 2 -->
  <rect x="210" y="446" width="1040" height="50" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="235" y="476" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">NIP-002</text>
  <text x="370" y="476" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Nama 2</text>
  <text x="630" y="476" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Cleaning Service</text>
  <text x="850" y="476" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Prodia Kebayoran</text>
  <rect x="1155" y="461" width="30" height="26" rx="4" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/>
  <text x="1170" y="478" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">🗑️</text>

  <!-- Row 3 -->
  <rect x="210" y="496" width="1040" height="50" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="235" y="526" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">NIP-003</text>
  <text x="370" y="526" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Nama 3</text>
  <text x="630" y="526" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Cleaning Service</text>
  <text x="850" y="526" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Prodia Kebayoran</text>
  <rect x="1155" y="511" width="30" height="26" rx="4" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/>
  <text x="1170" y="528" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">🗑️</text>

  <!-- Row 4 -->
  <rect x="210" y="546" width="1040" height="50" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="235" y="576" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">NIP-004</text>
  <text x="370" y="576" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Nama 4</text>
  <text x="630" y="576" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Cleaning Service</text>
  <text x="850" y="576" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Prodia Kebayoran</text>
  <rect x="1155" y="561" width="30" height="26" rx="4" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/>
  <text x="1170" y="578" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">🗑️</text>

  <!-- Row 5 -->
  <rect x="210" y="596" width="1040" height="50" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="235" y="626" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">NIP-005</text>
  <text x="370" y="626" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Nama 5</text>
  <text x="630" y="626" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Cleaning Service</text>
  <text x="850" y="626" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Prodia Kebayoran</text>
  <rect x="1155" y="611" width="30" height="26" rx="4" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/>
  <text x="1170" y="628" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">🗑️</text>
'''
    return get_admin_base_frame("karyawan", inner)

# -------------------------------------------------------------------------
# 3. WIREFRAME DASHBOARD SUPER ADMIN
# -------------------------------------------------------------------------
def build_wf_dashboard_admin():
    inner = f'''
  <!-- Hero Banner (Y: 80 - 220, W: 690) -->
  <rect x="210" y="80" width="690" height="140" rx="16" fill="#f3f4f6" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow)"/>
  <text x="240" y="125" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="bold" fill="#111827">Selamat Datang, [Nama Admin]!</text>
  <text x="240" y="150" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">Sistem evaluasi kinerja outsourcing PT ISS Indonesia di</text>
  <text x="240" y="167" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">[Unit Kerja / Laboratorium Klinik Prodia] siap ditinjau.</text>

  <!-- Button Audit Rumus MOORA in Hero -->
  <rect x="240" y="180" width="160" height="28" rx="14" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="320" y="198" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle" fill="#111827">✨ Audit Rumus MOORA</text>

  <!-- Medal Icon Graphic on right of Hero -->
  <circle cx="830" cy="150" r="38" fill="#e5e7eb" stroke="#111827" stroke-width="1.4"/>
  <circle cx="830" cy="144" r="14" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  <path d="M 822 156 L 816 178 L 830 170 L 844 178 L 838 156 Z" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>

  <!-- ================= KATEGORI & RINGKASAN ================= -->
  <text x="210" y="250" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="bold" fill="#111827">Kategori Penilaian &amp; Ringkasan</text>
  <rect x="760" y="235" width="140" height="22" rx="11" fill="#f3f4f6" stroke="#9ca3af" stroke-width="1"/>
  <text x="830" y="250" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#111827">[Kategori Aktif] ▾</text>

  <!-- 5 Horizontal Summary Cards (W: 130 each) -->
  <!-- Card 1: Cleaning Service -->
  <rect x="210" y="265" width="130" height="100" rx="12" fill="#ffffff" stroke="#111827" stroke-width="2"/>
  <rect x="250" y="278" width="36" height="36" rx="8" fill="#111827"/>
  <text x="268" y="300" font-family="Arial" font-size="14" text-anchor="middle" fill="#ffffff">🧹</text>
  <text x="275" y="332" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">Cleaning Service</text>
  <text x="275" y="348" font-family="Arial, Helvetica, sans-serif" font-size="9.5" text-anchor="middle" fill="#6b7280">([n] Personel)</text>

  <!-- Card 2: Messenger Lab -->
  <rect x="350" y="265" width="130" height="100" rx="12" fill="#ffffff" stroke="#9ca3af" stroke-width="1.2"/>
  <rect x="390" y="278" width="36" height="36" rx="8" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
  <text x="408" y="300" font-family="Arial" font-size="14" text-anchor="middle" fill="#111827">👥</text>
  <text x="415" y="332" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">Messenger Lab</text>
  <text x="415" y="348" font-family="Arial, Helvetica, sans-serif" font-size="9.5" text-anchor="middle" fill="#6b7280">([n] Personel)</text>

  <!-- Card 3: Kriteria Evaluasi -->
  <rect x="490" y="265" width="130" height="100" rx="12" fill="#ffffff" stroke="#9ca3af" stroke-width="1.2"/>
  <rect x="530" y="278" width="36" height="36" rx="8" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
  <text x="548" y="300" font-family="Arial" font-size="14" text-anchor="middle" fill="#111827">⚖</text>
  <text x="555" y="332" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">Kriteria Evaluasi</text>
  <text x="555" y="348" font-family="Arial, Helvetica, sans-serif" font-size="9.5" text-anchor="middle" fill="#6b7280">([n] Indikator)</text>

  <!-- Card 4: Periode Aktif -->
  <rect x="630" y="265" width="130" height="100" rx="12" fill="#ffffff" stroke="#9ca3af" stroke-width="1.2"/>
  <rect x="670" y="278" width="36" height="36" rx="8" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
  <text x="688" y="300" font-family="Arial" font-size="14" text-anchor="middle" fill="#111827">📅</text>
  <text x="695" y="332" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">Periode Aktif</text>
  <text x="695" y="348" font-family="Arial, Helvetica, sans-serif" font-size="9.5" text-anchor="middle" fill="#6b7280">[Periode Aktif]</text>

  <!-- Card 5: Skor Yi Tertinggi -->
  <rect x="770" y="265" width="130" height="100" rx="12" fill="#ffffff" stroke="#9ca3af" stroke-width="1.2"/>
  <rect x="810" y="278" width="36" height="36" rx="8" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
  <text x="828" y="300" font-family="Arial" font-size="14" text-anchor="middle" fill="#111827">🏅</text>
  <text x="835" y="332" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">Skor Yi Tertinggi</text>
  <text x="835" y="348" font-family="Arial, Helvetica, sans-serif" font-size="9.5" text-anchor="middle" fill="#6b7280">[0.0000]</text>

  <!-- ================= KLASEMEN KINERJA TABLE ================= -->
  <text x="210" y="395" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="bold" fill="#111827">Klasemen Kinerja ([Kategori Layanan])</text>
  <rect x="785" y="380" width="115" height="22" rx="11" fill="#f3f4f6" stroke="#9ca3af" stroke-width="1"/>
  <text x="842" y="395" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#111827">Lihat Audit MOORA</text>

  <rect x="210" y="410" width="690" height="370" rx="12" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  
  <!-- Table Header -->
  <rect x="210" y="410" width="690" height="32" rx="12 12 0 0" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
  <g font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" fill="#4b5563">
    <text x="240" y="430">NAMA PERSONEL</text>
    <text x="430" y="430">JABATAN / DIVISI</text>
    <text x="560" y="430">STATUS / PERINGKAT</text>
    <text x="730" y="430">NILAI OPTIMASI (YI)</text>
  </g>

  <!-- Row 1: Nama 1 (Rank 1 Highlighted) -->
  <rect x="210" y="442" width="690" height="58" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
  <line x1="210" y1="442" x2="210" y2="500" stroke="#111827" stroke-width="4"/>
  <circle cx="240" cy="471" r="14" fill="#111827"/>
  <text x="240" y="475" font-family="Arial" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">👤</text>
  <text x="265" y="466" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#111827">Nama 1</text>
  <text x="265" y="482" font-family="Arial, Helvetica, sans-serif" font-size="9.5" fill="#6b7280">NIP-001 – Prodia Kebayoran</text>
  <text x="430" y="473" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Cleaning Service</text>
  
  <!-- Badge Rank 1 -->
  <rect x="555" y="461" width="140" height="22" rx="11" fill="#111827"/>
  <text x="625" y="476" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#ffffff">★ [Peringkat #1] ★</text>
  
  <text x="750" y="474" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">[0.0000]</text>
  <text x="860" y="474" font-family="Arial" font-size="12" fill="#9ca3af">⋮</text>

  <!-- Row 2: Nama 2 -->
  <rect x="210" y="500" width="690" height="54" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
  <circle cx="240" cy="527" r="14" fill="#4b5563"/>
  <text x="240" y="531" font-family="Arial" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">👤</text>
  <text x="265" y="522" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#111827">Nama 2</text>
  <text x="265" y="538" font-family="Arial, Helvetica, sans-serif" font-size="9.5" fill="#6b7280">NIP-002 – Prodia Kebayoran</text>
  <text x="430" y="529" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Cleaning Service</text>
  <text x="560" y="529" font-family="Arial, Helvetica, sans-serif" font-size="10.5" fill="#111827">• [Peringkat #2]</text>
  <text x="750" y="530" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#111827">[0.0000]</text>
  <text x="860" y="530" font-family="Arial" font-size="12" fill="#9ca3af">⋮</text>

  <!-- Row 3: Nama 3 -->
  <rect x="210" y="554" width="690" height="54" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
  <circle cx="240" cy="581" r="14" fill="#6b7280"/>
  <text x="240" y="585" font-family="Arial" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">👤</text>
  <text x="265" y="576" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#111827">Nama 3</text>
  <text x="265" y="592" font-family="Arial, Helvetica, sans-serif" font-size="9.5" fill="#6b7280">NIP-003 – Prodia Kebayoran</text>
  <text x="430" y="583" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">Cleaning Service</text>
  <text x="560" y="583" font-family="Arial, Helvetica, sans-serif" font-size="10.5" fill="#111827">• [Peringkat #3]</text>
  <text x="750" y="584" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" fill="#111827">[0.0000]</text>
  <text x="860" y="584" font-family="Arial" font-size="12" fill="#9ca3af">⋮</text>

  <!-- ================= RIGHT COLUMN (EXECUTIVE PANEL X: 930..1260) ================= -->
  <!-- Jadwal Penilaian Header -->
  <text x="930" y="105" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">Jadwal Penilaian &lt; &gt;</text>
  <rect x="1170" y="90" width="90" height="20" rx="10" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/>
  <text x="1215" y="104" font-family="Arial, Helvetica, sans-serif" font-size="9.5" text-anchor="middle" fill="#111827">[Bulan Tahun]</text>

  <!-- Mini Calendar Strip -->
  <g font-family="Arial, Helvetica, sans-serif" font-size="10" text-anchor="middle">
    <!-- Day 1 -->
    <rect x="935" y="125" width="45" height="52" rx="10" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
    <text x="957" y="142" font-size="8.5" fill="#6b7280">Sen</text>
    <text x="957" y="163" font-size="13" font-weight="bold" fill="#111827">19</text>

    <!-- Day 2 -->
    <rect x="990" y="125" width="45" height="52" rx="10" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
    <text x="1012" y="142" font-size="8.5" fill="#6b7280">Sel</text>
    <text x="1012" y="163" font-size="13" font-weight="bold" fill="#111827">20</text>

    <!-- Day 3 (Active) -->
    <rect x="1045" y="125" width="45" height="52" rx="10" fill="#111827"/>
    <text x="1067" y="142" font-size="8.5" fill="#ffffff">Rab</text>
    <text x="1067" y="163" font-size="13" font-weight="bold" fill="#ffffff">21</text>

    <!-- Day 4 -->
    <rect x="1100" y="125" width="45" height="52" rx="10" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
    <text x="1122" y="142" font-size="8.5" fill="#6b7280">Kam</text>
    <text x="1122" y="163" font-size="13" font-weight="bold" fill="#111827">22</text>

    <!-- Day 5 -->
    <rect x="1155" y="125" width="45" height="52" rx="10" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
    <text x="1177" y="142" font-size="8.5" fill="#6b7280">Jum</text>
    <text x="1177" y="163" font-size="13" font-weight="bold" fill="#111827">23</text>
  </g>

  <!-- Kandidat Unggul (Top 3) -->
  <text x="930" y="215" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">Kandidat Unggul (Top 3)</text>
  <text x="1260" y="215" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" text-anchor="end" fill="#4b5563">Lihat Semua</text>

  <!-- Top 1 List Item -->
  <circle cx="950" cy="248" r="14" fill="#111827"/>
  <text x="950" y="252" font-family="Arial" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">👤</text>
  <text x="975" y="244" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Nama 1</text>
  <text x="975" y="258" font-family="Arial, Helvetica, sans-serif" font-size="9.5" fill="#6b7280">Skor Yi: [0.0000]</text>
  <text x="1255" y="252" font-family="Arial" font-size="12" fill="#9ca3af">☆</text>

  <!-- Top 2 List Item -->
  <circle cx="950" cy="295" r="14" fill="#4b5563"/>
  <text x="950" y="299" font-family="Arial" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">👤</text>
  <text x="975" y="291" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Nama 2</text>
  <text x="975" y="305" font-family="Arial, Helvetica, sans-serif" font-size="9.5" fill="#6b7280">Skor Yi: [0.0000]</text>
  <text x="1255" y="299" font-family="Arial" font-size="12" fill="#9ca3af">☆</text>

  <!-- Top 3 List Item -->
  <circle cx="950" cy="342" r="14" fill="#6b7280"/>
  <text x="950" y="346" font-family="Arial" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">👤</text>
  <text x="975" y="338" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Nama 3</text>
  <text x="975" y="352" font-family="Arial, Helvetica, sans-serif" font-size="9.5" fill="#6b7280">Skor Yi: [0.0000]</text>
  <text x="1255" y="346" font-family="Arial" font-size="12" fill="#9ca3af">☆</text>

  <!-- Rekomendasi Insentif -->
  <text x="930" y="395" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">Rekomendasi Insentif</text>
  <text x="1260" y="395" font-family="Arial, Helvetica, sans-serif" font-size="9" fill="#6b7280" text-anchor="end">Prodia Kebayoran</text>

  <!-- 3 Mini Candidate Cards -->
  <!-- Mini 1 -->
  <rect x="935" y="415" width="70" height="95" rx="8" fill="#ffffff" stroke="#e5e7eb" stroke-width="1"/>
  <circle cx="970" cy="438" r="13" fill="#111827"/>
  <text x="970" y="442" font-family="Arial" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#ffffff">👤</text>
  <text x="970" y="462" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#111827">Nama 1</text>
  <text x="970" y="474" font-family="Arial, Helvetica, sans-serif" font-size="8" fill="#6b7280" text-anchor="middle">Rank #1</text>
  <rect x="942" y="482" width="56" height="18" rx="9" fill="#111827"/>
  <text x="970" y="494" font-family="Arial, Helvetica, sans-serif" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#ffffff">Pilih SK</text>

  <!-- Mini 2 -->
  <rect x="1015" y="415" width="70" height="95" rx="8" fill="#ffffff" stroke="#e5e7eb" stroke-width="1"/>
  <circle cx="1050" cy="438" r="13" fill="#4b5563"/>
  <text x="1050" y="442" font-family="Arial" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#ffffff">👤</text>
  <text x="1050" y="462" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#111827">Nama 2</text>
  <text x="1050" y="474" font-family="Arial, Helvetica, sans-serif" font-size="8" fill="#6b7280" text-anchor="middle">Rank #2</text>
  <rect x="1022" y="482" width="56" height="18" rx="9" fill="#111827"/>
  <text x="1050" y="494" font-family="Arial, Helvetica, sans-serif" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#ffffff">Pilih SK</text>

  <!-- Mini 3 -->
  <rect x="1095" y="415" width="70" height="95" rx="8" fill="#ffffff" stroke="#e5e7eb" stroke-width="1"/>
  <circle cx="1130" cy="438" r="13" fill="#6b7280"/>
  <text x="1130" y="442" font-family="Arial" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#ffffff">👤</text>
  <text x="1130" y="462" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#111827">Nama 3</text>
  <text x="1130" y="474" font-family="Arial, Helvetica, sans-serif" font-size="8" fill="#6b7280" text-anchor="middle">Rank #3</text>
  <rect x="1102" y="482" width="56" height="18" rx="9" fill="#111827"/>
  <text x="1130" y="494" font-family="Arial, Helvetica, sans-serif" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#ffffff">Pilih SK</text>
'''
    return get_admin_base_frame("dashboard", inner, is_dashboard=True)

# -------------------------------------------------------------------------
# 4. WIREFRAME KRITERIA & BOBOT (Super Admin)
# -------------------------------------------------------------------------
def build_wf_kriteria_bobot():
    inner = f'''
  <!-- Hero Banner (Y: 80 - 220, W: 1040) -->
  <rect x="210" y="80" width="1040" height="140" rx="16" fill="#f3f4f6" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow)"/>
  <text x="240" y="125" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="bold" fill="#111827">Selamat Datang, [Nama Admin]!</text>
  <text x="240" y="150" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">Sistem evaluasi kinerja outsourcing PT ISS Indonesia di</text>
  <text x="240" y="167" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">[Unit Kerja / Laboratorium Klinik Prodia] siap ditinjau.</text>

  <!-- Button Audit Rumus MOORA in Hero -->
  <rect x="240" y="180" width="160" height="28" rx="14" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="320" y="198" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle" fill="#111827">✨ Audit Rumus MOORA</text>

  <!-- Medal Icon Graphic on right of Hero -->
  <circle cx="1180" cy="150" r="38" fill="#e5e7eb" stroke="#111827" stroke-width="1.4"/>
  <circle cx="1180" cy="144" r="14" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  <path d="M 1172 156 L 1166 178 L 1180 170 L 1194 178 L 1188 156 Z" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>

  <!-- ================= CONTAINER CARD KRITERIA ================= -->
  <rect x="210" y="240" width="1040" height="540" rx="16" fill="#ffffff" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow)"/>
  
  <!-- Header Title inside Card -->
  <text x="240" y="278" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="bold" fill="#111827">Kriteria &amp; Pembobotan (Cleaning Service)</text>
  <text x="240" y="298" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#6b7280">Total bobot seluruh kriteria wajib 1.00 (100%).</text>

  <!-- Data Table -->
  <rect x="240" y="320" width="980" height="420" rx="10" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  
  <!-- Table Header -->
  <rect x="240" y="320" width="980" height="38" rx="10 10 0 0" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
  <g font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" fill="#374151">
    <text x="260" y="344">KODE</text>
    <text x="325" y="344">NAMA KRITERIA</text>
    <text x="590" y="344">SIFAT</text>
    <text x="690" y="338" text-anchor="middle">BOBOT</text>
    <text x="690" y="350" text-anchor="middle">(W)</text>
    <text x="770" y="344" text-anchor="middle">PERSENTASE</text>
    <text x="830" y="344">DESKRIPSI STANDAR</text>
  </g>

  <!-- Row 1: C1 -->
  <rect x="240" y="358" width="980" height="55" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="260" y="390" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">C1</text>
  <text x="325" y="390" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Kedisiplinan &amp; Presensi Kehadiran</text>
  <rect x="585" y="375" width="55" height="20" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1"/>
  <text x="612" y="389" font-family="Arial" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#111827">BENEFIT</text>
  <text x="690" y="390" font-family="Arial, Helvetica, sans-serif" font-size="11" text-anchor="middle" fill="#111827">0.20</text>
  <text x="770" y="390" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">20%</text>
  <text x="830" y="390" font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#4b5563">Tingkat kehadiran, ketepatan waktu jam kerja dan absensi harian</text>

  <!-- Row 2: C2 -->
  <rect x="240" y="413" width="980" height="55" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="260" y="445" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">C2</text>
  <text x="325" y="445" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Kualitas Kebersihan &amp; Kerapihan Area</text>
  <rect x="585" y="430" width="55" height="20" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1"/>
  <text x="612" y="444" font-family="Arial" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#111827">BENEFIT</text>
  <text x="690" y="445" font-family="Arial, Helvetica, sans-serif" font-size="11" text-anchor="middle" fill="#111827">0.25</text>
  <text x="770" y="445" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">25%</text>
  <text x="830" y="445" font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#4b5563">Hasil checklist harian kebersihan ruang lab, poliklinik, dan toilet</text>

  <!-- Row 3: C3 -->
  <rect x="240" y="468" width="980" height="55" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="260" y="500" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">C3</text>
  <text x="325" y="495" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Kepatuhan SOP APD &amp; Penanganan</text>
  <text x="325" y="509" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Limbah Medis</text>
  <rect x="585" y="485" width="55" height="20" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1"/>
  <text x="612" y="499" font-family="Arial" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#111827">BENEFIT</text>
  <text x="690" y="500" font-family="Arial, Helvetica, sans-serif" font-size="11" text-anchor="middle" fill="#111827">0.25</text>
  <text x="770" y="500" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">25%</text>
  <text x="830" y="495" font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#4b5563">Disiplin penggunaan sarung tangan, masker, dan pemilahan safety</text>
  <text x="830" y="509" font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#4b5563">box limbah B3</text>

  <!-- Row 4: C4 -->
  <rect x="240" y="523" width="980" height="55" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="260" y="555" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">C4</text>
  <text x="325" y="555" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Sikap &amp; Kerjasama Tim (Attitude)</text>
  <rect x="585" y="540" width="55" height="20" rx="4" fill="#ffffff" stroke="#111827" stroke-width="1"/>
  <text x="612" y="554" font-family="Arial" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#111827">BENEFIT</text>
  <text x="690" y="555" font-family="Arial, Helvetica, sans-serif" font-size="11" text-anchor="middle" fill="#111827">0.15</text>
  <text x="770" y="555" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">15%</text>
  <text x="830" y="555" font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#4b5563">Kesopanan terhadap pasien/staf lab dan inisiatif saling membantu</text>

  <!-- Row 5: C5 -->
  <rect x="240" y="578" width="980" height="55" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
  <text x="260" y="610" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">C5</text>
  <text x="325" y="610" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">Jumlah Komplain / Teguran Klien</text>
  <rect x="585" y="595" width="55" height="20" rx="4" fill="#111827"/>
  <text x="612" y="609" font-family="Arial" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#ffffff">COST</text>
  <text x="690" y="610" font-family="Arial, Helvetica, sans-serif" font-size="11" text-anchor="middle" fill="#111827">0.15</text>
  <text x="770" y="610" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">15%</text>
  <text x="830" y="605" font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#4b5563">Jumlah catatan teguran atau ketidaksesuaian kerja dari pihak Prodia</text>
  <text x="830" y="619" font-family="Arial, Helvetica, sans-serif" font-size="10" fill="#4b5563">Kebayoran</text>

  <!-- Table Summary Footer -->
  <rect x="240" y="633" width="980" height="42" rx="0 0 10 10" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
  <text x="260" y="659" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">TOTAL BOBOT:</text>
  <text x="690" y="659" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#111827">1.00</text>
  <text x="770" y="659" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#111827">100%</text>
  <text x="830" y="659" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#111827">✓ Valid (Normalisasi Lengkap)</text>
'''
    return get_admin_base_frame("kriteria", inner)

# -------------------------------------------------------------------------
# Main Runner & Chrome Rasterizer
# -------------------------------------------------------------------------
diagrams = [
    ("wireframe_01_login_exact", build_wf_login()),
    ("wireframe_02_master_karyawan_exact", build_wf_master_karyawan()),
    ("wireframe_03_dashboard_admin_exact", build_wf_dashboard_admin()),
    ("wireframe_04_kriteria_bobot_exact", build_wf_kriteria_bobot()),
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    print("Generating 4 Pristine Exact Wireframes for Super Admin...")
    for name, svg_content in diagrams:
        svg_file = os.path.join(OUT_DIR, f"{name}.svg")
        png_file = os.path.join(OUT_DIR, f"{name}.png")
        
        with open(svg_file, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"  [OK] Saved SVG: {svg_file}")
        
        # Rasterize with headless Chrome
        cmd = [
            chrome_path,
            "--headless=new",
            "--disable-gpu",
            "--force-device-scale-factor=2",
            f"--window-size={W},{H}",
            f"--screenshot={png_file}",
            os.path.abspath(svg_file)
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode == 0:
            print(f"  [OK] Rendered PNG: {png_file}")
            shutil.copy(svg_file, os.path.join(ARTIFACT_DIR, f"{name}.svg"))
            shutil.copy(png_file, os.path.join(ARTIFACT_DIR, f"{name}.png"))
        else:
            print(f"  [ERR] Chrome failed: {res.stderr.decode('utf-8')}")

if __name__ == "__main__":
    main()
