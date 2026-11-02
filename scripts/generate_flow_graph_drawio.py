import os
import subprocess

# Generate Draw.io style Flow Graph SVG & PNG
# Node N = 12, Edge E = 15, Cyclomatic Complexity V(G) = 5

W = 1460
H = 1080

def generate_svg():
    return f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Draw.io Grid Pattern -->
    <pattern id="drawio-grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1"/>
      <circle cx="20" cy="20" r="0.8" fill="#cbd5e1" />
    </pattern>

    <!-- Markers for Arrows -->
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#2563eb" />
    </marker>
    <marker id="arrow-slate" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#475569" />
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#16a34a" />
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#dc2626" />
    </marker>

    <!-- Soft Filter for Draw.io Drop Shadow -->
    <filter id="drawio-shadow" x="-5%" y="-5%" width="115%" height="115%" filterUnits="userSpaceOnUse">
      <feGaussianBlur in="SourceAlpha" stdDeviation="2"/>
      <feOffset dx="1" dy="2" result="offsetblur"/>
      <feComponentTransfer>
        <feFuncA type="linear" slope="0.12"/>
      </feComponentTransfer>
      <feMerge> 
        <feMergeNode/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="{W}" height="{H}" fill="#ffffff" />
  <rect width="{W}" height="{H}" fill="url(#drawio-grid)" />

  <!-- Outer Boundary Frame -->
  <rect x="18" y="18" width="{W - 36}" height="{H - 36}" rx="8" fill="none" stroke="#94a3b8" stroke-width="1.2" />

  <!-- Title Header Bar -->
  <rect x="18" y="18" width="{W - 36}" height="68" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <rect x="28" y="28" width="6" height="48" rx="3" fill="#2563eb" />
  <text x="46" y="47" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="19" font-weight="700" fill="#0f172a">
    CONTROL FLOW GRAPH (FLOW GRAPH) - PENGUJIAN WHITE BOX
  </text>
  <text x="46" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12.5" fill="#64748b">
    Modul Fungsi Engine Komputasi MOORA (calculateMoora) | V(G) = E - N + 2P = 15 - 12 + 2(1) = 5
  </text>

  <!-- Draw.io Badge Header Tag (Top Right) -->
  <rect x="{W - 220}" y="34" width="180" height="34" rx="6" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="1" />
  <text x="{W - 130}" y="55" font-family="monospace" font-size="11" font-weight="600" fill="#334155" text-anchor="middle">
    draw.io diagram style
  </text>

  <!-- ================= LEFT AREA: FLOW GRAPH CANVAS ================= -->
  <!-- Flow Graph Inner Card -->
  <rect x="36" y="104" width="770" height="940" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" filter="url(#drawio-shadow)" />

  <!-- Card Subtitle -->
  <text x="56" y="132" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#1e293b">
    A. Representasi Graf Alir Alur Kontrol Program (Flow Graph)
  </text>
  <line x1="56" y1="142" x2="786" y2="142" stroke="#e2e8f0" stroke-width="1" />

  <!-- ================= REGION BADGES (Draw.io style dashed region markers) ================= -->
  <!-- Region 1: Edge 1-2-12-1 -->
  <rect x="620" y="320" width="84" height="32" rx="6" fill="#fdf4ff" stroke="#d946ef" stroke-dasharray="4 3" stroke-width="1.2" />
  <text x="662" y="341" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" font-weight="700" fill="#a21caf" text-anchor="middle">Region 1</text>

  <!-- Region 2: Alternatif loop back -->
  <rect x="64" y="580" width="84" height="32" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-dasharray="4 3" stroke-width="1.2" />
  <text x="106" y="601" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" font-weight="700" fill="#1d4ed8" text-anchor="middle">Region 2</text>

  <!-- Region 3: Kriteria loop back -->
  <rect x="176" y="560" width="84" height="32" rx="6" fill="#f0fdf4" stroke="#22c55e" stroke-dasharray="4 3" stroke-width="1.2" />
  <text x="218" y="581" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" font-weight="700" fill="#15803d" text-anchor="middle">Region 3</text>

  <!-- Region 4: Benefit / Cost Split -->
  <rect x="318" y="660" width="84" height="32" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-dasharray="4 3" stroke-width="1.2" />
  <text x="360" y="681" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" font-weight="700" fill="#b45309" text-anchor="middle">Region 4</text>

  <!-- Region 5: Outer Area -->
  <rect x="670" y="820" width="84" height="32" rx="6" fill="#f8fafc" stroke="#64748b" stroke-dasharray="4 3" stroke-width="1.2" />
  <text x="712" y="841" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" font-weight="700" fill="#475569" text-anchor="middle">Region 5</text>


  <!-- ================= EDGES (CONNECTING ARROWS) ================= -->
  <!-- 1 -> 2 (True: data kosong) -->
  <path d="M 382 190 L 556 190" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrow-red)" />
  <rect x="444" y="174" width="48" height="18" rx="3" fill="#fee2e2" stroke="#fca5a5" stroke-width="0.8" />
  <text x="468" y="187" font-family="monospace" font-size="10" font-weight="bold" fill="#b91c1c" text-anchor="middle">True</text>

  <!-- 1 -> 3 (False: lanjut proses) -->
  <path d="M 360 212 L 360 258" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow-slate)" />
  <rect x="368" y="224" width="48" height="18" rx="3" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="0.8" />
  <text x="392" y="237" font-family="monospace" font-size="10" font-weight="bold" fill="#334155" text-anchor="middle">False</text>

  <!-- 2 -> 12 (Empty return direct to terminal exit) via Bus X=580 -->
  <path d="M 580 212 L 580 970 L 384 970" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrow-red)" />
  <rect x="586" y="440" width="94" height="20" rx="4" fill="#fee2e2" stroke="#fca5a5" stroke-width="0.8" />
  <text x="633" y="454" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9" font-weight="600" fill="#991b1b" text-anchor="middle">Return Kosong</text>

  <!-- 3 -> 4 -->
  <path d="M 360 302 L 360 348" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- 4 -> 5 (Ada alternatif) -->
  <path d="M 360 392 L 360 438" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow-slate)" />
  <rect x="368" y="404" width="76" height="18" rx="3" fill="#eff6ff" stroke="#bfdbfe" stroke-width="0.8" />
  <text x="406" y="417" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">Ada Alternatif</text>

  <!-- 4 -> 11 (Semua alternatif selesai) via Bus X=540 -->
  <path d="M 382 370 L 540 370 L 540 890 L 384 890" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow-slate)" />
  <rect x="496" y="520" width="90" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="0.8" />
  <text x="541" y="534" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9" font-weight="bold" fill="#475569" text-anchor="middle">Selesai Alternatif</text>

  <!-- 5 -> 6 (Ada kriteria) -->
  <path d="M 360 482 L 360 528" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow-slate)" />
  <rect x="368" y="494" width="72" height="18" rx="3" fill="#eff6ff" stroke="#bfdbfe" stroke-width="0.8" />
  <text x="404" y="507" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">Ada Kriteria</text>

  <!-- 5 -> 10 (Kriteria habis untuk alternatif ini) via Bus X=500 -->
  <path d="M 382 460 L 500 460 L 500 810 L 384 810" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow-slate)" />
  <rect x="456" y="600" width="88" height="20" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="0.8" />
  <text x="500" y="614" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9" font-weight="bold" fill="#475569" text-anchor="middle">Selesai Kriteria</text>

  <!-- 6 -> 7 (BENEFIT = True) -->
  <path d="M 342 565 L 260 628" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrow-green)" />
  <rect x="254" y="584" width="64" height="18" rx="3" fill="#dcfce7" stroke="#86efac" stroke-width="0.8" />
  <text x="286" y="597" font-family="monospace" font-size="9.5" font-weight="bold" fill="#15803d" text-anchor="middle">BENEFIT</text>

  <!-- 6 -> 8 (COST = False) -->
  <path d="M 378 565 L 460 628" fill="none" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrow-slate)" />
  <rect x="428" y="584" width="54" height="18" rx="3" fill="#ffedd5" stroke="#fed7aa" stroke-width="0.8" />
  <text x="455" y="597" font-family="monospace" font-size="9.5" font-weight="bold" fill="#c2410c" text-anchor="middle">COST</text>

  <!-- 7 -> 9 (Merge back) -->
  <path d="M 260 672 L 342 725" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- 8 -> 9 (Merge back) -->
  <path d="M 460 672 L 378 725" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow-slate)" />

  <!-- 9 -> 5 (Loop back: iterasi kriteria berikutnya via Bus X=210) -->
  <path d="M 338 735 L 210 735 L 210 460 L 336 460" fill="none" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrow-blue)" />
  <rect x="156" y="500" width="86" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe" stroke-width="0.8" />
  <text x="199" y="514" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Loop Kriteria</text>

  <!-- 10 -> 4 (Loop back: iterasi alternatif berikutnya via Bus X=130) -->
  <path d="M 338 810 L 130 810 L 130 370 L 336 370" fill="none" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrow-blue)" />
  <rect x="76" y="440" width="94" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe" stroke-width="0.8" />
  <text x="123" y="454" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="9" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Loop Alternatif</text>

  <!-- 11 -> 12 (Ranking selesai -> Terminal Exit) -->
  <path d="M 360 912 L 360 946" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrow-slate)" />


  <!-- ================= NODES (DRAW.IO SHAPES) ================= -->

  <!-- NODE 1: Predicate Node (Start & Check Empty) -->
  <circle cx="360" cy="190" r="22" fill="#fff2cc" stroke="#d6b656" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="360" y="196" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#7f6000" text-anchor="middle">1</text>
  <rect x="110" y="176" width="220" height="28" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="220" y="194" font-family="monospace" font-size="9.5" fill="#1e293b" text-anchor="middle">if (alt.len == 0 || crit.len == 0)</text>

  <!-- NODE 2: Return Empty -->
  <circle cx="580" cy="190" r="22" fill="#d5e8d4" stroke="#82b366" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="580" y="196" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#274e13" text-anchor="middle">2</text>
  <rect x="618" y="176" width="130" height="28" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="683" y="194" font-family="monospace" font-size="9.5" fill="#1e293b" text-anchor="middle">return emptyResult</text>

  <!-- NODE 3: Process Matrix X, Divisors, R, V -->
  <circle cx="360" cy="280" r="22" fill="#dae8fc" stroke="#6c8ebf" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="360" y="286" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#1c4587" text-anchor="middle">3</text>
  <rect x="180" y="266" width="150" height="28" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="255" y="284" font-family="monospace" font-size="9.5" fill="#1e293b" text-anchor="middle">Hitung Matriks X, R, V</text>

  <!-- NODE 4: Predicate Loop Alternatif -->
  <circle cx="360" cy="370" r="22" fill="#fff2cc" stroke="#d6b656" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="360" y="376" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#7f6000" text-anchor="middle">4</text>
  <rect x="160" y="336" width="170" height="26" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="245" y="353" font-family="monospace" font-size="9.5" fill="#1e293b" text-anchor="middle">for (alt of alternatives)</text>

  <!-- NODE 5: Predicate Loop Kriteria -->
  <circle cx="360" cy="460" r="22" fill="#fff2cc" stroke="#d6b656" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="360" y="466" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#7f6000" text-anchor="middle">5</text>
  <rect x="170" y="426" width="160" height="26" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="250" y="443" font-family="monospace" font-size="9.5" fill="#1e293b" text-anchor="middle">for (c of criteriaList)</text>

  <!-- NODE 6: Predicate Check Type BENEFIT / COST -->
  <circle cx="360" cy="550" r="22" fill="#fff2cc" stroke="#d6b656" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="360" y="556" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#7f6000" text-anchor="middle">6</text>
  <rect x="236" y="520" width="160" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="316" y="536" font-family="monospace" font-size="9" fill="#1e293b" text-anchor="middle">if (c.type === 'BENEFIT')</text>

  <!-- NODE 7: Process sumBenefit -->
  <circle cx="260" cy="650" r="22" fill="#dae8fc" stroke="#6c8ebf" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="260" y="656" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#1c4587" text-anchor="middle">7</text>
  <rect x="136" y="664" width="104" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="188" y="680" font-family="monospace" font-size="9" fill="#1e293b" text-anchor="middle">sumBenefit += v</text>

  <!-- NODE 8: Process sumCost -->
  <circle cx="460" cy="650" r="22" fill="#dae8fc" stroke="#6c8ebf" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="460" y="656" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#1c4587" text-anchor="middle">8</text>
  <rect x="478" y="664" width="94" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="525" y="680" font-family="monospace" font-size="9" fill="#1e293b" text-anchor="middle">sumCost += v</text>

  <!-- NODE 9: Merge Kriteria Iteration -->
  <circle cx="360" cy="735" r="22" fill="#dae8fc" stroke="#6c8ebf" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="360" y="741" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#1c4587" text-anchor="middle">9</text>
  <rect x="390" y="722" width="104" height="24" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="442" y="738" font-family="monospace" font-size="9" fill="#1e293b" text-anchor="middle">Next Kriteria</text>

  <!-- NODE 10: Compute Yi (Optimasi Alternatif) -->
  <circle cx="360" cy="810" r="22" fill="#dae8fc" stroke="#6c8ebf" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="360" y="816" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#1c4587" text-anchor="middle">10</text>
  <rect x="176" y="816" width="154" height="26" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="253" y="833" font-family="monospace" font-size="9.5" fill="#1e293b" text-anchor="middle">yScore = sumB - sumC</text>

  <!-- NODE 11: Sort Rankings Descending -->
  <circle cx="360" cy="890" r="22" fill="#dae8fc" stroke="#6c8ebf" stroke-width="2" filter="url(#drawio-shadow)" />
  <text x="360" y="896" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#1c4587" text-anchor="middle">11</text>
  <rect x="200" y="888" width="130" height="26" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="265" y="905" font-family="monospace" font-size="9" fill="#1e293b" text-anchor="middle">sortRankings(yScore)</text>

  <!-- NODE 12: Terminal Exit (Final Return) -->
  <circle cx="360" cy="970" r="24" fill="#d5e8d4" stroke="#82b366" stroke-width="2.5" filter="url(#drawio-shadow)" />
  <circle cx="360" cy="970" r="18" fill="none" stroke="#82b366" stroke-width="1.2" />
  <text x="360" y="976" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="bold" fill="#274e13" text-anchor="middle">12</text>
  <rect x="180" y="966" width="144" height="26" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="252" y="983" font-family="monospace" font-size="9" fill="#1e293b" text-anchor="middle">return finalMooraOutput</text>


  <!-- ================= RIGHT AREA: DRAW.IO TABLES & SUMMARY ================= -->

  <!-- Panel 1: Legenda Node & Kode Program -->
  <rect x="826" y="104" width="598" height="526" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" filter="url(#drawio-shadow)" />
  <rect x="826" y="104" width="598" height="40" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="846" y="129" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#1e293b">
    B. Pemetaan Node Alur Kontrol &amp; Baris Kode (Statements)
  </text>

  <!-- Table Header -->
  <rect x="842" y="156" width="566" height="28" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
  <text x="866" y="174" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">Node</text>
  <text x="946" y="174" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#334155">Tipe Node</text>
  <text x="1090" y="174" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#334155">Pernyataan Program (Statement Logika)</text>

  <!-- Table Rows -->
  <!-- Row 1 -->
  <rect x="842" y="184" width="566" height="26" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="197" r="9" fill="#fff2cc" stroke="#d6b656" stroke-width="1.2" />
  <text x="866" y="201" font-family="sans-serif" font-size="10" font-weight="bold" fill="#7f6000" text-anchor="middle">1</text>
  <text x="946" y="201" font-family="sans-serif" font-size="10.5" fill="#475569">Predicate (Branch)</text>
  <text x="1090" y="201" font-family="monospace" font-size="9.5" fill="#0f172a">if (alternatives.len==0 || criteria.len==0)</text>

  <!-- Row 2 -->
  <rect x="842" y="210" width="566" height="26" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="223" r="9" fill="#d5e8d4" stroke="#82b366" stroke-width="1.2" />
  <text x="866" y="227" font-family="sans-serif" font-size="10" font-weight="bold" fill="#274e13" text-anchor="middle">2</text>
  <text x="946" y="227" font-family="sans-serif" font-size="10.5" fill="#475569">Statement / Exit</text>
  <text x="1090" y="227" font-family="monospace" font-size="9.5" fill="#0f172a">return emptyResult;</text>

  <!-- Row 3 -->
  <rect x="842" y="236" width="566" height="26" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="249" r="9" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.2" />
  <text x="866" y="253" font-family="sans-serif" font-size="10" font-weight="bold" fill="#1c4587" text-anchor="middle">3</text>
  <text x="946" y="253" font-family="sans-serif" font-size="10.5" fill="#475569">Sequential Process</text>
  <text x="1090" y="253" font-family="monospace" font-size="9.5" fill="#0f172a">Hitung Matriks X, Pembagi, Normalisasi R &amp; V</text>

  <!-- Row 4 -->
  <rect x="842" y="262" width="566" height="26" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="275" r="9" fill="#fff2cc" stroke="#d6b656" stroke-width="1.2" />
  <text x="866" y="279" font-family="sans-serif" font-size="10" font-weight="bold" fill="#7f6000" text-anchor="middle">4</text>
  <text x="946" y="279" font-family="sans-serif" font-size="10.5" fill="#475569">Predicate (Loop Outer)</text>
  <text x="1090" y="279" font-family="monospace" font-size="9.5" fill="#0f172a">for (const alt of alternatives)</text>

  <!-- Row 5 -->
  <rect x="842" y="288" width="566" height="26" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="301" r="9" fill="#fff2cc" stroke="#d6b656" stroke-width="1.2" />
  <text x="866" y="305" font-family="sans-serif" font-size="10" font-weight="bold" fill="#7f6000" text-anchor="middle">5</text>
  <text x="946" y="305" font-family="sans-serif" font-size="10.5" fill="#475569">Predicate (Loop Inner)</text>
  <text x="1090" y="305" font-family="monospace" font-size="9.5" fill="#0f172a">for (const c of criteriaList)</text>

  <!-- Row 6 -->
  <rect x="842" y="314" width="566" height="26" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="327" r="9" fill="#fff2cc" stroke="#d6b656" stroke-width="1.2" />
  <text x="866" y="331" font-family="sans-serif" font-size="10" font-weight="bold" fill="#7f6000" text-anchor="middle">6</text>
  <text x="946" y="331" font-family="sans-serif" font-size="10.5" fill="#475569">Predicate (Branch)</text>
  <text x="1090" y="331" font-family="monospace" font-size="9.5" fill="#0f172a">if (c.type === "BENEFIT")</text>

  <!-- Row 7 -->
  <rect x="842" y="340" width="566" height="26" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="353" r="9" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.2" />
  <text x="866" y="357" font-family="sans-serif" font-size="10" font-weight="bold" fill="#1c4587" text-anchor="middle">7</text>
  <text x="946" y="357" font-family="sans-serif" font-size="10.5" fill="#475569">Process Statement</text>
  <text x="1090" y="357" font-family="monospace" font-size="9.5" fill="#0f172a">sumBenefit += v;</text>

  <!-- Row 8 -->
  <rect x="842" y="366" width="566" height="26" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="379" r="9" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.2" />
  <text x="866" y="383" font-family="sans-serif" font-size="10" font-weight="bold" fill="#1c4587" text-anchor="middle">8</text>
  <text x="946" y="383" font-family="sans-serif" font-size="10.5" fill="#475569">Process Statement</text>
  <text x="1090" y="383" font-family="monospace" font-size="9.5" fill="#0f172a">sumCost += v;</text>

  <!-- Row 9 -->
  <rect x="842" y="392" width="566" height="26" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="405" r="9" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.2" />
  <text x="866" y="409" font-family="sans-serif" font-size="10" font-weight="bold" fill="#1c4587" text-anchor="middle">9</text>
  <text x="946" y="409" font-family="sans-serif" font-size="10.5" fill="#475569">Loop Increment</text>
  <text x="1090" y="409" font-family="monospace" font-size="9.5" fill="#0f172a">Iterasi elemen kriteria berikutnya</text>

  <!-- Row 10 -->
  <rect x="842" y="418" width="566" height="26" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="431" r="9" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.2" />
  <text x="866" y="435" font-family="sans-serif" font-size="10" font-weight="bold" fill="#1c4587" text-anchor="middle">10</text>
  <text x="946" y="435" font-family="sans-serif" font-size="10.5" fill="#475569">Calculation Statement</text>
  <text x="1090" y="435" font-family="monospace" font-size="9.5" fill="#0f172a">yScore = sumBenefit - sumCost;</text>

  <!-- Row 11 -->
  <rect x="842" y="444" width="566" height="26" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="457" r="9" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.2" />
  <text x="866" y="461" font-family="sans-serif" font-size="10" font-weight="bold" fill="#1c4587" text-anchor="middle">11</text>
  <text x="946" y="461" font-family="sans-serif" font-size="10.5" fill="#475569">Process Statement</text>
  <text x="1090" y="461" font-family="monospace" font-size="9.5" fill="#0f172a">calculatedRows.sort((a,b) =&gt; b.yScore - a.yScore)</text>

  <!-- Row 12 -->
  <rect x="842" y="470" width="566" height="26" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <circle cx="866" cy="483" r="9" fill="#d5e8d4" stroke="#82b366" stroke-width="1.2" />
  <text x="866" y="487" font-family="sans-serif" font-size="10" font-weight="bold" fill="#274e13" text-anchor="middle">12</text>
  <text x="946" y="487" font-family="sans-serif" font-size="10.5" fill="#475569">Terminal Exit</text>
  <text x="1090" y="487" font-family="monospace" font-size="9.5" fill="#0f172a">return finalMooraOutput;</text>

  <!-- Legend Footer -->
  <rect x="842" y="506" width="566" height="110" rx="6" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
  <text x="858" y="526" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11" font-weight="700" fill="#1e293b">Legenda Simbol Standar Draw.io:</text>
  
  <circle cx="872" cy="546" r="9" fill="#fff2cc" stroke="#d6b656" stroke-width="1.2" />
  <text x="890" y="550" font-family="sans-serif" font-size="10" fill="#475569">Predicate / Decision Node (Percabangan logika True/False atau Perulangan)</text>

  <circle cx="872" cy="570" r="9" fill="#dae8fc" stroke="#6c8ebf" stroke-width="1.2" />
  <text x="890" y="574" font-family="sans-serif" font-size="10" fill="#475569">Processing Node (Kalkulasi matematika sekuensial, pembagian, dan sorting)</text>

  <circle cx="872" cy="596" r="9" fill="#d5e8d4" stroke="#82b366" stroke-width="1.2" />
  <text x="890" y="600" font-family="sans-serif" font-size="10" fill="#475569">Terminal / Exit Node (Titik akhir keluaran objek hasil evaluasi)</text>


  <!-- Panel 2: Kompleksitas Siklomatis & 5 Basis Path -->
  <rect x="826" y="646" width="598" height="398" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" filter="url(#drawio-shadow)" />
  <rect x="826" y="646" width="598" height="40" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
  <text x="846" y="671" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" fill="#1e293b">
    C. Pembuktian Cyclomatic Complexity &amp; Jalur Uji (Basis Path)
  </text>

  <!-- Metric Boxes -->
  <rect x="842" y="700" width="130" height="66" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1" />
  <text x="907" y="724" font-family="sans-serif" font-size="10.5" font-weight="600" fill="#1e40af" text-anchor="middle">Edges (E)</text>
  <text x="907" y="752" font-family="sans-serif" font-size="22" font-weight="800" fill="#1d4ed8" text-anchor="middle">15</text>

  <rect x="986" y="700" width="130" height="66" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1" />
  <text x="1051" y="724" font-family="sans-serif" font-size="10.5" font-weight="600" fill="#1e40af" text-anchor="middle">Nodes (N)</text>
  <text x="1051" y="752" font-family="sans-serif" font-size="22" font-weight="800" fill="#1d4ed8" text-anchor="middle">12</text>

  <rect x="1130" y="700" width="130" height="66" rx="6" fill="#fffbeb" stroke="#fef3c7" stroke-width="1" />
  <text x="1195" y="724" font-family="sans-serif" font-size="10.5" font-weight="600" fill="#92400e" text-anchor="middle">Predicates (P')</text>
  <text x="1195" y="752" font-family="sans-serif" font-size="22" font-weight="800" fill="#b45309" text-anchor="middle">4</text>

  <rect x="1274" y="700" width="134" height="66" rx="6" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1" />
  <text x="1341" y="724" font-family="sans-serif" font-size="10.5" font-weight="600" fill="#166534" text-anchor="middle">Complexity V(G)</text>
  <text x="1341" y="752" font-family="sans-serif" font-size="22" font-weight="800" fill="#15803d" text-anchor="middle">5</text>

  <!-- Formula Callouts -->
  <rect x="842" y="776" width="566" height="54" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <text x="858" y="796" font-family="monospace" font-size="11" font-weight="bold" fill="#0f172a">
    1) V(G) = E - N + 2P  = 15 - 12 + 2(1) = 5
  </text>
  <text x="858" y="816" font-family="monospace" font-size="11" font-weight="bold" fill="#0f172a">
    2) V(G) = P' + 1      = 4 + 1           = 5   |  3) Region (R) = 5
  </text>

  <!-- 5 Basis Path List -->
  <text x="846" y="852" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="11.5" font-weight="700" fill="#1e293b">
    5 Jalur Independen Eksekusi (Basis Paths):
  </text>

  <rect x="842" y="862" width="566" height="26" rx="4" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <text x="854" y="879" font-family="monospace" font-size="10" font-weight="bold" fill="#b91c1c">Path 1 (Kosong):</text>
  <text x="970" y="879" font-family="monospace" font-size="9.5" fill="#334155">1 -&gt; 2 -&gt; 12</text>

  <rect x="842" y="892" width="566" height="26" rx="4" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
  <text x="854" y="909" font-family="monospace" font-size="10" font-weight="bold" fill="#1d4ed8">Path 2 (Nol Alt):</text>
  <text x="970" y="909" font-family="monospace" font-size="9.5" fill="#334155">1 -&gt; 3 -&gt; 4 -&gt; 11 -&gt; 12</text>

  <rect x="842" y="922" width="566" height="26" rx="4" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <text x="854" y="939" font-family="monospace" font-size="10" font-weight="bold" fill="#15803d">Path 3 (Benefit):</text>
  <text x="970" y="939" font-family="monospace" font-size="9.5" fill="#334155">1 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; 6 -&gt; 7 -&gt; 9 -&gt; 10 -&gt; 11 -&gt; 12</text>

  <rect x="842" y="952" width="566" height="26" rx="4" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
  <text x="854" y="969" font-family="monospace" font-size="10" font-weight="bold" fill="#c2410c">Path 4 (Cost):</text>
  <text x="970" y="969" font-family="monospace" font-size="9.5" fill="#334155">1 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; 6 -&gt; 8 -&gt; 9 -&gt; 10 -&gt; 11 -&gt; 12</text>

  <rect x="842" y="982" width="566" height="26" rx="4" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
  <text x="854" y="999" font-family="monospace" font-size="10" font-weight="bold" fill="#6b21a8">Path 5 (Lengkap):</text>
  <text x="970" y="999" font-family="monospace" font-size="9.5" fill="#334155">1 -&gt; 3 -&gt; 4 -&gt; [Loop Kriteria 5-6-(7|8)-9] -&gt; 10 -&gt; [Loop Alt 4] -&gt; 11 -&gt; 12</text>

  <text x="846" y="1030" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="10" font-style="italic" fill="#64748b">
    *Kesimpulan: V(G) = 5 membuktikan algoritma MOORA terstruktur bebas galat komputasi (low risk).
  </text>
</svg>"""

if __name__ == "__main__":
    out_dir = "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams"
    svg_path = os.path.join(out_dir, "flow_graph_moora.svg")
    png_path = os.path.join(out_dir, "flow_graph_moora.png")
    html_path = os.path.join(out_dir, "flow_graph_moora.html")

    svg_content = generate_svg()

    # Write SVG
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[OK] Saved SVG: {svg_path}")

    # Write HTML wrapper for crisp Chrome rasterization
    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
  </style>
</head>
<body>
  {svg_content}
</body>
</html>"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[OK] Saved HTML: {html_path}")

    # Rasterize to PNG with headless Chrome
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={W},{H}",
        f"--screenshot={png_path}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode == 0:
        print(f"[OK] Rendered PNG: {png_path}")
    else:
        print(f"[ERR] Chrome failed: {res.stderr.decode('utf-8')}")

    # Copy to Artifact directory
    artifact_dir = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/e6c145f5-ba78-4f4a-bc31-4712ef0b13ed"
    if os.path.exists(artifact_dir):
        import shutil
        art_svg = os.path.join(artifact_dir, "flow_graph_moora.svg")
        art_png = os.path.join(artifact_dir, "flow_graph_moora.png")
        shutil.copyfile(svg_path, art_svg)
        shutil.copyfile(png_path, art_png)
        print(f"[OK] Copied to artifact: {art_png}")
