#!/usr/bin/env python3
"""
Generate exact B&W Wireframes for Branch Manager (Pimpinan Mitra Klien Prodia):
1. Wireframe Dashboard Branch Manager
2. Wireframe Kalkulasi MOORA (Branch Manager)
3. Wireframe Pengesahan SK & Berita Acara (Branch Manager - with Sahkan & Tandatangani Button)

Using standard initial placeholders like Nama 1, Nama 2, NIP-001, [Nama Pimpinan], [0.0000].
"""

import os
import subprocess
import shutil

OUT_DIR = "public/diagrams"
ARTIFACT_DIR = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/e6c145f5-ba78-4f4a-bc31-4712ef0b13ed"

W = 1280
H = 820

# -------------------------------------------------------------------------
# Base Frame with Branch Manager Sidebar (Dashboard, Kalkulasi, Laporan & SK with APPROVAL badge)
# -------------------------------------------------------------------------
def get_bm_base_frame(active_nav, inner_content, is_dashboard=False):
    navs = [
        ("dashboard", "Dashboard", "▦", 115, None),
        ("moora", "Kalkulasi MOORA", "📄", 155, None),
        ("reports", "Laporan &amp; SK", "📑", 195, "APPROVAL"),
    ]

    sidebar_items = []
    for key, label, icon, y, badge in navs:
        is_active = (key == active_nav)
        if is_active:
            sidebar_items.append(f'''    <!-- Active Nav: {key} -->
    <rect x="15" y="{y}" width="160" height="34" rx="8" fill="#111827"/>
    <text x="32" y="{y+21}" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#ffffff">{icon}  {label}</text>''')
            if badge:
                sidebar_items.append(f'<rect x="120" y="{y+9}" width="50" height="16" rx="4" fill="#ffffff"/><text x="145" y="{y+21}" font-family="Arial" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#111827">{badge}</text>')
        else:
            sidebar_items.append(f'''    <!-- Nav: {key} -->
    <text x="32" y="{y+21}" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#4b5563">{icon}  {label}</text>''')
            if badge:
                sidebar_items.append(f'<rect x="120" y="{y+9}" width="50" height="16" rx="4" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/><text x="145" y="{y+21}" font-family="Arial" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#4b5563">{badge}</text>')

    sidebar_svg = "\n".join(sidebar_items)

    if is_dashboard:
        top_bar_right = '''  <!-- Right Actions (Dashboard Branch Manager) -->
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
    <text x="1145" y="38" font-size="11" font-weight="bold" text-anchor="end" fill="#111827">[Nama Branch Manager]</text>
    <rect x="1065" y="44" width="80" height="15" rx="3" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/>
    <text x="1105" y="55" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#111827">MANAGER PRODIA</text>
  </g>

  <circle cx="1175" cy="43" r="16" fill="#111827"/>
  <text x="1175" y="48" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">S</text>'''
    else:
        top_bar_right = '''  <!-- Right Actions (Full Width layout Branch Manager) -->
  <rect x="840" y="25" width="165" height="36" rx="18" fill="#111827"/>
  <text x="922" y="48" font-family="Arial, Helvetica, sans-serif" font-size="11.5" font-weight="bold" text-anchor="middle" fill="#ffffff">🔄  Sinkronkan MOORA</text>

  <circle cx="1030" cy="43" r="15" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="1030" y="47" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">⚙</text>

  <circle cx="1070" cy="43" r="15" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="1070" y="47" font-family="Arial" font-size="11" text-anchor="middle" fill="#111827">🔔</text>
  <circle cx="1080" cy="35" r="5" fill="#111827"/>
  <text x="1080" y="38" font-family="Arial" font-size="7" font-weight="bold" text-anchor="middle" fill="#ffffff">3</text>

  <circle cx="1115" cy="43" r="16" fill="#111827"/>
  <text x="1115" y="48" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">S</text>'''

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
# 1. WIREFRAME DASHBOARD BRANCH MANAGER
# -------------------------------------------------------------------------
def build_wf_dashboard_bm():
    inner = f'''
  <!-- Hero Banner (Y: 80 - 220, W: 690) -->
  <rect x="210" y="80" width="690" height="140" rx="16" fill="#f3f4f6" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow)"/>
  <text x="240" y="125" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="bold" fill="#111827">Selamat Datang, [Nama Pimpinan]!</text>
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
    return get_bm_base_frame("dashboard", inner, is_dashboard=True)

# -------------------------------------------------------------------------
# 2. WIREFRAME KALKULASI MOORA (BRANCH MANAGER)
# -------------------------------------------------------------------------
def build_wf_kalkulasi_bm():
    inner = f'''
  <!-- Hero Banner (Y: 80 - 220, W: 1040) -->
  <rect x="210" y="80" width="1040" height="140" rx="16" fill="#f3f4f6" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow)"/>
  <text x="240" y="125" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="bold" fill="#111827">Selamat Datang, [Nama Pimpinan]!</text>
  <text x="240" y="150" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">Sistem evaluasi kinerja outsourcing PT ISS Indonesia di</text>
  <text x="240" y="167" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">[Unit Kerja / Laboratorium Klinik Prodia] siap ditinjau.</text>

  <!-- Button Kembali ke Dashboard in Hero -->
  <rect x="240" y="180" width="170" height="28" rx="14" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="325" y="198" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle" fill="#111827">✨  Kembali ke Dashboard</text>

  <!-- Medal Icon Graphic on right of Hero -->
  <circle cx="1180" cy="150" r="38" fill="#e5e7eb" stroke="#111827" stroke-width="1.4"/>
  <circle cx="1180" cy="144" r="14" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  <path d="M 1172 156 L 1166 178 L 1180 170 L 1194 178 L 1188 156 Z" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>

  <!-- ================= MAIN AUDIT CARD ================= -->
  <rect x="210" y="240" width="1040" height="540" rx="16" fill="#ffffff" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow)"/>
  
  <!-- Header Title inside Card -->
  <text x="240" y="275" font-family="Arial, Helvetica, sans-serif" font-size="15" font-weight="bold" fill="#111827">Transparansi 4 Tahap Komputasi MOORA</text>
  <text x="240" y="293" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#6b7280">Setiap matriks dihitung secara deterministik dan siap diaudit pada presentasi tugas akhir.</text>

  <!-- Hitung Ulang Button -->
  <rect x="1120" y="260" width="105" height="28" rx="14" fill="#111827"/>
  <text x="1172" y="278" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="bold" text-anchor="middle" fill="#ffffff">🔄  Hitung Ulang</text>

  <!-- 4 Step Tabs -->
  <g font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold">
    <!-- Tab 1 (Active) -->
    <rect x="240" y="315" width="165" height="30" rx="15" fill="#111827"/>
    <text x="322" y="334" text-anchor="middle" fill="#ffffff">1. Matriks Keputusan (X)</text>

    <!-- Tab 2 -->
    <rect x="415" y="315" width="165" height="30" rx="15" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
    <text x="497" y="334" text-anchor="middle" fill="#4b5563">2. Normalisasi Rasio (R)</text>

    <!-- Tab 3 -->
    <rect x="590" y="315" width="155" height="30" rx="15" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
    <text x="667" y="334" text-anchor="middle" fill="#4b5563">3. Matriks Terbobot (V)</text>

    <!-- Tab 4 -->
    <rect x="755" y="315" width="195" height="30" rx="15" fill="#ffffff" stroke="#9ca3af" stroke-width="1"/>
    <text x="852" y="334" text-anchor="middle" fill="#4b5563">4. Optimasi Nilai (Yi) &amp; Peringkat</text>
  </g>

  <!-- Step 1 Explanatory Card with Formula -->
  <rect x="240" y="365" width="980" height="90" rx="12" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="265" y="398" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">Tahap 1: Pembentukan Matriks Keputusan Awal</text>
  <text x="265" y="420" font-family="Arial, Helvetica, sans-serif" font-size="10.5" fill="#4b5563">Matriks berukuran m alternatif (karyawan) × n kriteria, memuat seluruh nilai aktual kinerja lapangan (X_ij).</text>

  <!-- Formula Matrix graphic on right -->
  <rect x="910" y="378" width="280" height="64" rx="8" fill="#f9fafb" stroke="#9ca3af" stroke-width="1"/>
  <text x="1050" y="415" font-family="'Times New Roman', Georgia, serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#111827">X = [ x_ij ]_m×n</text>

  <!-- Matrix Data Table -->
  <rect x="240" y="475" width="980" height="280" rx="8" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  
  <!-- Table Header -->
  <rect x="240" y="475" width="980" height="42" rx="8 8 0 0" fill="#f3f4f6" stroke="#111827" stroke-width="1"/>
  <g font-family="Arial, Helvetica, sans-serif" font-size="9" font-weight="bold" fill="#374151">
    <text x="260" y="493">ALTERNATIF</text>
    <text x="260" y="505">PERSONEL</text>

    <text x="430" y="493" text-anchor="middle">C1: KEDISIPLINAN &amp;</text>
    <text x="430" y="505" text-anchor="middle">PRESENSI (20%)</text>

    <text x="580" y="493" text-anchor="middle">C2: KUALITAS</text>
    <text x="580" y="505" text-anchor="middle">KEBERSIHAN (25%)</text>

    <text x="740" y="493" text-anchor="middle">C3: SOP APD &amp; LIMBAH</text>
    <text x="740" y="505" text-anchor="middle">MEDIS (25%)</text>

    <text x="890" y="493" text-anchor="middle">C4: SIKAP &amp; KERJASAMA</text>
    <text x="890" y="505" text-anchor="middle">(ATTITUDE) (15%)</text>

    <text x="1070" y="493" text-anchor="middle">C5: KOMPLAIN /</text>
    <text x="1070" y="505" text-anchor="middle">TEGURAN (15%)</text>
  </g>

  <!-- Table Rows -->
  <g font-family="Arial, Helvetica, sans-serif" font-size="11" fill="#111827">
    <!-- Row 1 -->
    <rect x="240" y="517" width="980" height="45" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="260" y="544" font-weight="bold">Nama 1</text>
    <text x="430" y="544" text-anchor="middle" fill="#4b5563">[x_11]</text>
    <text x="580" y="544" text-anchor="middle" fill="#4b5563">[x_12]</text>
    <text x="740" y="544" text-anchor="middle" fill="#4b5563">[x_13]</text>
    <text x="890" y="544" text-anchor="middle" fill="#4b5563">[x_14]</text>
    <text x="1070" y="544" text-anchor="middle" fill="#4b5563">[x_15]</text>

    <!-- Row 2 -->
    <rect x="240" y="562" width="980" height="45" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="260" y="589" font-weight="bold">Nama 2</text>
    <text x="430" y="589" text-anchor="middle" fill="#4b5563">[x_21]</text>
    <text x="580" y="589" text-anchor="middle" fill="#4b5563">[x_22]</text>
    <text x="740" y="589" text-anchor="middle" fill="#4b5563">[x_23]</text>
    <text x="890" y="589" text-anchor="middle" fill="#4b5563">[x_24]</text>
    <text x="1070" y="589" text-anchor="middle" fill="#4b5563">[x_25]</text>

    <!-- Row 3 -->
    <rect x="240" y="607" width="980" height="45" fill="#ffffff" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="260" y="634" font-weight="bold">Nama 3</text>
    <text x="430" y="634" text-anchor="middle" fill="#4b5563">[x_31]</text>
    <text x="580" y="634" text-anchor="middle" fill="#4b5563">[x_32]</text>
    <text x="740" y="634" text-anchor="middle" fill="#4b5563">[x_33]</text>
    <text x="890" y="634" text-anchor="middle" fill="#4b5563">[x_34]</text>
    <text x="1070" y="634" text-anchor="middle" fill="#4b5563">[x_35]</text>

    <!-- Row 4 -->
    <rect x="240" y="652" width="980" height="45" fill="#f9fafb" stroke="#e5e7eb" stroke-width="0.8"/>
    <text x="260" y="679" font-weight="bold" fill="#6b7280">[Nama Personel ...]</text>
    <text x="430" y="679" text-anchor="middle" fill="#9ca3af">[x_m1]</text>
    <text x="580" y="679" text-anchor="middle" fill="#9ca3af">[x_m2]</text>
    <text x="740" y="679" text-anchor="middle" fill="#9ca3af">[x_m3]</text>
    <text x="890" y="679" text-anchor="middle" fill="#9ca3af">[x_m4]</text>
    <text x="1070" y="679" text-anchor="middle" fill="#9ca3af">[x_m5]</text>
  </g>
'''
    return get_bm_base_frame("moora", inner)

# -------------------------------------------------------------------------
# 3. WIREFRAME PENGESAHAN LAPORAN & SK (BRANCH MANAGER APPROVAL)
# -------------------------------------------------------------------------
def build_wf_laporan_approval_bm():
    inner = f'''
  <!-- Hero Banner (Y: 80 - 220, W: 1040) -->
  <rect x="210" y="80" width="1040" height="140" rx="16" fill="#f3f4f6" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow)"/>
  <text x="240" y="125" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="bold" fill="#111827">Selamat Datang, [Nama Pimpinan]!</text>
  <text x="240" y="150" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">Sistem evaluasi kinerja outsourcing PT ISS Indonesia di</text>
  <text x="240" y="167" font-family="Arial, Helvetica, sans-serif" font-size="11.5" fill="#4b5563">[Unit Kerja / Laboratorium Klinik Prodia] siap ditinjau.</text>

  <!-- Button Audit Rumus MOORA in Hero -->
  <rect x="240" y="180" width="160" height="28" rx="14" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="320" y="198" font-family="Arial, Helvetica, sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle" fill="#111827">✨ Audit Rumus MOORA</text>

  <!-- Medal Icon Graphic on right of Hero -->
  <circle cx="1180" cy="150" r="38" fill="#e5e7eb" stroke="#111827" stroke-width="1.4"/>
  <circle cx="1180" cy="144" r="14" fill="#ffffff" stroke="#111827" stroke-width="1.4"/>
  <path d="M 1172 156 L 1166 178 L 1180 170 L 1194 178 L 1188 156 Z" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>

  <!-- ================= STATUS NOTIFICATION / APPROVAL CARD ================= -->
  <rect x="210" y="240" width="1040" height="100" rx="12" fill="#ffffff" stroke="#111827" stroke-width="1.4" filter="url(#wf-shadow)"/>
  
  <rect x="235" y="255" width="165" height="18" rx="4" fill="#f3f4f6" stroke="#9ca3af" stroke-width="0.8"/>
  <text x="317" y="268" font-family="Arial, Helvetica, sans-serif" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#111827">STATUS: MENUNGGU PENGESAHAN</text>
  
  <text x="415" y="269" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="bold" fill="#111827">SK Rekomendasi Insentif Kuartal III 2026</text>
  <text x="235" y="293" font-family="Arial, Helvetica, sans-serif" font-size="10.5" fill="#4b5563">Hasil pemeringkatan MOORA memerlukan verifikasi dan persetujuan resmi dari Pimpinan Mitra Klien (Branch Manager Prodia).</text>

  <!-- Button 1: Sahkan & Tandatangani SK Resmi (Branch Manager Action) -->
  <rect x="235" y="308" width="220" height="28" rx="14" fill="#111827"/>
  <text x="345" y="326" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#ffffff">✓ Sahkan &amp; Tandatangani SK Resmi</text>

  <!-- Button 2: Cetak SK PDF -->
  <rect x="465" y="308" width="130" height="28" rx="14" fill="#ffffff" stroke="#111827" stroke-width="1.2"/>
  <text x="530" y="326" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#111827">🖨️ Cetak SK (PDF)</text>

  <!-- ================= DOKUMEN BERITA ACARA CONTAINER ================= -->
  <rect x="210" y="360" width="1040" height="420" rx="14" fill="#ffffff" stroke="#111827" stroke-width="1.5" filter="url(#wf-shadow)"/>
  
  <!-- Kop Surat -->
  <circle cx="265" cy="405" r="22" fill="#ffffff" stroke="#111827" stroke-width="1.8"/>
  <text x="265" y="411" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#111827">ISS</text>
  
  <text x="300" y="400" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="bold" fill="#111827">PT ISS INDONESIA – FACILITY SERVICES</text>
  <text x="300" y="415" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" fill="#4b5563">UNIT PENEMPATAN LABORATORIUM KLINIK PRODIA KEBAYORAN</text>
  <text x="300" y="428" font-family="Arial, Helvetica, sans-serif" font-size="9.5" fill="#6b7280">Jl. Kyai Maja No. 39, Kebayoran Baru, Jakarta Selatan - DKI Jakarta</text>

  <!-- Right Meta in Kop -->
  <text x="1220" y="400" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="end" fill="#111827">NO: ISS-PRD/SPK-MOORA/2026/08</text>
  <text x="1220" y="415" font-family="Arial, Helvetica, sans-serif" font-size="9.5" font-weight="bold" text-anchor="end" fill="#111827">TANGGAL: 23 Oktober 2026</text>

  <!-- Divider Line -->
  <line x1="240" y1="445" x2="1220" y2="445" stroke="#111827" stroke-width="1.5"/>

  <!-- Berita Acara Title -->
  <text x="730" y="475" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="bold" text-anchor="middle" fill="#111827">BERITA ACARA PENETAPAN KARYAWAN OUTSOURCING TERBAIK</text>
  <text x="730" y="493" font-family="Arial, Helvetica, sans-serif" font-size="11" text-anchor="middle" fill="#4b5563">Kategori: <tspan font-weight="bold" fill="#111827">CLEANING SERVICE</tspan> – Periode: Kuartal III 2026</text>

  <!-- Highlight Box Winner -->
  <rect x="240" y="515" width="980" height="90" rx="8" fill="#f9fafb" stroke="#111827" stroke-width="1.4"/>
  <text x="730" y="542" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="bold" text-anchor="middle" fill="#111827">★ [PREDIKAT KARYAWAN TERBAIK #1] ★</text>
  <text x="730" y="568" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="bold" text-anchor="middle" fill="#111827">Nama 1</text>
  <text x="730" y="588" font-family="Arial, Helvetica, sans-serif" font-size="11.5" text-anchor="middle" fill="#4b5563">NIP: <tspan font-weight="bold" fill="#111827">NIP-001</tspan> | Skor Optimasi (Yi): <tspan font-weight="bold" fill="#111827">[0.0000]</tspan></text>
'''
    return get_bm_base_frame("reports", inner)

# -------------------------------------------------------------------------
# Main Runner & Chrome Rasterizer
# -------------------------------------------------------------------------
diagrams = [
    ("wireframe_bm_01_dashboard_exact", build_wf_dashboard_bm()),
    ("wireframe_bm_02_kalkulasi_exact", build_wf_kalkulasi_bm()),
    ("wireframe_bm_03_laporan_approval_exact", build_wf_laporan_approval_bm()),
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    print("Generating 3 Pristine Exact Wireframes for Branch Manager...")
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
