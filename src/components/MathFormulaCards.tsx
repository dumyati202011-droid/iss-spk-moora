import React from "react";

export function FormulaMatrixX() {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", background: "#f8fafc", border: "1px solid #e2e8f0", borderRadius: "16px", padding: "16px 24px", marginBottom: "20px", flexWrap: "wrap", gap: "16px" }}>
      <div>
        <div style={{ fontSize: "0.88rem", fontWeight: 800, color: "#0f172a", marginBottom: "4px" }}>
          Tahap 1: Pembentukan Matriks Keputusan Awal
        </div>
        <p style={{ fontSize: "0.78rem", color: "#64748b" }}>
          Matriks berukuran m alternatif (karyawan) × n kriteria, memuat seluruh nilai aktual kinerja lapangan (X_ij).
        </p>
      </div>

      {/* SVG Vector Formula */}
      <div style={{ background: "#ffffff", padding: "10px 20px", borderRadius: "12px", border: "1px solid #cbd5e1", boxShadow: "0 2px 8px rgba(0,0,0,0.04)" }}>
        <svg width="260" height="60" viewBox="0 0 260 60" fill="none" xmlns="http://www.w3.org/2000/svg">
          {/* Label X = */}
          <text x="10" y="36" fontFamily="Cambria Math, Times New Roman, serif" fontSize="22" fontWeight="bold" fontStyle="italic" fill="#0f172a">X =</text>
          
          {/* Left Bracket */}
          <path d="M 60 12 L 52 12 L 52 48 L 60 48" stroke="#3b5bfd" strokeWidth="2.5" fill="none" strokeLinecap="round" />
          
          {/* Matrix items */}
          <text x="68" y="26" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#334155">x₁₁</text>
          <text x="105" y="26" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#334155">x₁₂</text>
          <text x="142" y="26" fontFamily="Cambria Math, Times New Roman, serif" fontSize="14" fill="#94a3b8">⋯</text>
          <text x="175" y="26" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#334155">x₁ₙ</text>

          <text x="68" y="44" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#334155">xₘ₁</text>
          <text x="105" y="44" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#334155">xₘ₂</text>
          <text x="142" y="44" fontFamily="Cambria Math, Times New Roman, serif" fontSize="14" fill="#94a3b8">⋯</text>
          <text x="175" y="44" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#334155">xₘₙ</text>

          {/* Right Bracket */}
          <path d="M 205 12 L 213 12 L 213 48 L 205 48" stroke="#3b5bfd" strokeWidth="2.5" fill="none" strokeLinecap="round" />
          <text x="218" y="48" fontFamily="sans-serif" fontSize="10" fontWeight="600" fill="#64748b">m × n</text>
        </svg>
      </div>
    </div>
  );
}

export function FormulaVectorNormalization() {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", background: "#f8fafc", border: "1px solid #e2e8f0", borderRadius: "16px", padding: "16px 24px", marginBottom: "20px", flexWrap: "wrap", gap: "16px" }}>
      <div>
        <div style={{ fontSize: "0.88rem", fontWeight: 800, color: "#0f172a", marginBottom: "4px" }}>
          Tahap 2: Formula Normalisasi Rasio Vektor
        </div>
        <p style={{ fontSize: "0.78rem", color: "#64748b" }}>
          Setiap elemen dibagi dengan akar kuadrat dari penjumlahan seluruh kuadrat nilai pada kriteria yang sama.
        </p>
      </div>

      {/* SVG Vector Formula */}
      <div style={{ background: "#ffffff", padding: "10px 20px", borderRadius: "12px", border: "1px solid #cbd5e1", boxShadow: "0 2px 8px rgba(0,0,0,0.04)" }}>
        <svg width="270" height="66" viewBox="0 0 270 66" fill="none" xmlns="http://www.w3.org/2000/svg">
          {/* r_ij = */}
          <text x="10" y="38" fontFamily="Cambria Math, Times New Roman, serif" fontSize="22" fontStyle="italic" fontWeight="bold" fill="#0f172a">r</text>
          <text x="22" y="43" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#475569">ij</text>
          <text x="40" y="38" fontFamily="Cambria Math, Times New Roman, serif" fontSize="22" fontWeight="bold" fill="#0f172a">=</text>

          {/* Fraction Numerator: x_ij */}
          <text x="125" y="24" fontFamily="Cambria Math, Times New Roman, serif" fontSize="18" fontStyle="italic" fontWeight="bold" fill="#3b5bfd">x</text>
          <text x="135" y="28" fontFamily="Cambria Math, Times New Roman, serif" fontSize="12" fontStyle="italic" fill="#3b5bfd">ij</text>

          {/* Fraction Bar */}
          <line x1="68" y1="33" x2="250" y2="33" stroke="#0f172a" strokeWidth="2" strokeLinecap="round" />

          {/* Denominator: Square Root + Sum Sigma */}
          {/* Radical sign */}
          <path d="M 72 48 L 78 48 L 84 59 L 94 37 L 246 37" stroke="#0f172a" strokeWidth="1.8" fill="none" strokeLinecap="round" strokeLinejoin="round" />

          {/* Sigma symbol */}
          <text x="100" y="55" fontFamily="Cambria Math, Times New Roman, serif" fontSize="18" fontWeight="bold" fill="#0f172a">∑</text>
          <text x="96" y="63" fontFamily="sans-serif" fontSize="9" fill="#64748b">k=1</text>
          <text x="102" y="44" fontFamily="sans-serif" fontSize="9" fill="#64748b">m</text>

          {/* x_kj^2 */}
          <text x="124" y="54" fontFamily="Cambria Math, Times New Roman, serif" fontSize="17" fontStyle="italic" fontWeight="bold" fill="#0f172a">x</text>
          <text x="134" y="58" fontFamily="Cambria Math, Times New Roman, serif" fontSize="11" fontStyle="italic" fill="#475569">kj</text>
          <text x="144" y="46" fontFamily="sans-serif" fontSize="11" fontWeight="bold" fill="#0f172a">²</text>
        </svg>
      </div>
    </div>
  );
}

export function FormulaWeightedMatrix() {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", background: "#f8fafc", border: "1px solid #e2e8f0", borderRadius: "16px", padding: "16px 24px", marginBottom: "20px", flexWrap: "wrap", gap: "16px" }}>
      <div>
        <div style={{ fontSize: "0.88rem", fontWeight: 800, color: "#0f172a", marginBottom: "4px" }}>
          Tahap 3: Pembobotan Matriks Ternormalisasi
        </div>
        <p style={{ fontSize: "0.78rem", color: "#64748b" }}>
          Setiap elemen normalisasi dikalikan dengan bobot kriteria masing-masing (W_j), dengan total bobot = 1.00 (100%).
        </p>
      </div>

      {/* SVG Vector Formula */}
      <div style={{ background: "#ffffff", padding: "10px 20px", borderRadius: "12px", border: "1px solid #cbd5e1", boxShadow: "0 2px 8px rgba(0,0,0,0.04)" }}>
        <svg width="250" height="56" viewBox="0 0 250 56" fill="none" xmlns="http://www.w3.org/2000/svg">
          {/* v_ij = */}
          <text x="10" y="35" fontFamily="Cambria Math, Times New Roman, serif" fontSize="22" fontStyle="italic" fontWeight="bold" fill="#0f172a">v</text>
          <text x="22" y="40" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#475569">ij</text>
          <text x="40" y="35" fontFamily="Cambria Math, Times New Roman, serif" fontSize="22" fontWeight="bold" fill="#0f172a">=</text>

          {/* w_j */}
          <text x="68" y="35" fontFamily="Cambria Math, Times New Roman, serif" fontSize="22" fontStyle="italic" fontWeight="bold" fill="#f97316">w</text>
          <text x="86" y="40" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#f97316">j</text>

          {/* times dot */}
          <text x="105" y="35" fontFamily="sans-serif" fontSize="20" fontWeight="bold" fill="#475569">×</text>

          {/* r_ij */}
          <text x="130" y="35" fontFamily="Cambria Math, Times New Roman, serif" fontSize="22" fontStyle="italic" fontWeight="bold" fill="#3b5bfd">r</text>
          <text x="142" y="40" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#3b5bfd">ij</text>

          {/* Condition tag */}
          <rect x="175" y="16" width="65" height="24" rx="12" fill="#ecfdf5" stroke="#a7f3d0" />
          <text x="183" y="32" fontFamily="sans-serif" fontSize="10" fontWeight="bold" fill="#065f46">Σ W = 1.0</text>
        </svg>
      </div>
    </div>
  );
}

export function FormulaOptimizationYi() {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", background: "#f8fafc", border: "1px solid #e2e8f0", borderRadius: "16px", padding: "16px 24px", marginBottom: "20px", flexWrap: "wrap", gap: "16px" }}>
      <div>
        <div style={{ fontSize: "0.88rem", fontWeight: 800, color: "#0f172a", marginBottom: "4px" }}>
          Tahap 4: Optimasi Multiobjektif & Perangkingan
        </div>
        <p style={{ fontSize: "0.78rem", color: "#64748b" }}>
          Nilai akhir Yi diperoleh dari total nilai atribut Benefit dikurangi total nilai atribut Cost. Nilai tertinggi adalah Karyawan Terbaik.
        </p>
      </div>

      {/* SVG Vector Formula */}
      <div style={{ background: "#ffffff", padding: "10px 20px", borderRadius: "12px", border: "1px solid #cbd5e1", boxShadow: "0 2px 8px rgba(0,0,0,0.04)" }}>
        <svg width="300" height="58" viewBox="0 0 300 58" fill="none" xmlns="http://www.w3.org/2000/svg">
          {/* y_i = */}
          <text x="10" y="36" fontFamily="Cambria Math, Times New Roman, serif" fontSize="22" fontStyle="italic" fontWeight="bold" fill="#0f172a">y</text>
          <text x="22" y="41" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontStyle="italic" fill="#475569">i</text>
          <text x="36" y="36" fontFamily="Cambria Math, Times New Roman, serif" fontSize="22" fontWeight="bold" fill="#0f172a">=</text>

          {/* Sum Benefit */}
          <text x="60" y="36" fontFamily="Cambria Math, Times New Roman, serif" fontSize="20" fontWeight="bold" fill="#10b981">∑</text>
          <text x="56" y="48" fontFamily="sans-serif" fontSize="9" fill="#10b981">j=1</text>
          <text x="62" y="18" fontFamily="sans-serif" fontSize="9" fill="#10b981">g</text>

          <text x="78" y="36" fontFamily="Cambria Math, Times New Roman, serif" fontSize="18" fontStyle="italic" fontWeight="bold" fill="#10b981">v</text>
          <text x="88" y="40" fontFamily="Cambria Math, Times New Roman, serif" fontSize="11" fontStyle="italic" fill="#10b981">ij</text>

          {/* Minus sign */}
          <text x="110" y="36" fontFamily="sans-serif" fontSize="22" fontWeight="bold" fill="#ef4444">−</text>

          {/* Sum Cost */}
          <text x="135" y="36" fontFamily="Cambria Math, Times New Roman, serif" fontSize="20" fontWeight="bold" fill="#ef4444">∑</text>
          <text x="130" y="48" fontFamily="sans-serif" fontSize="8" fill="#ef4444">j=g+1</text>
          <text x="138" y="18" fontFamily="sans-serif" fontSize="9" fill="#ef4444">n</text>

          <text x="162" y="36" fontFamily="Cambria Math, Times New Roman, serif" fontSize="18" fontStyle="italic" fontWeight="bold" fill="#ef4444">v</text>
          <text x="172" y="40" fontFamily="Cambria Math, Times New Roman, serif" fontSize="11" fontStyle="italic" fill="#ef4444">ij</text>

          {/* Benefit - Cost Badge */}
          <rect x="195" y="18" width="96" height="22" rx="11" fill="#f0f9ff" stroke="#bae6fd" />
          <text x="202" y="33" fontFamily="sans-serif" fontSize="9" fontWeight="bold" fill="#0369a1">Benefit − Cost</text>
        </svg>
      </div>
    </div>
  );
}

export function MiniVectorDivisorBadge() {
  return (
    <div style={{ display: "inline-flex", alignItems: "center", gap: "10px" }}>
      <span style={{ fontWeight: 800, color: "#3b5bfd", fontSize: "0.8rem", letterSpacing: "0.02em" }}>
        NILAI PEMBAGI VEKTOR
      </span>
      <svg width="86" height="26" viewBox="0 0 86 26" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ verticalAlign: "middle" }}>
        <rect width="86" height="26" rx="6" fill="#eef2ff" stroke="#c7d2fe" />
        <path d="M 8 16 L 12 16 L 15 22 L 20 6 L 80 6" stroke="#3b5bfd" strokeWidth="1.6" fill="none" strokeLinecap="round" strokeLinejoin="round" />
        <text x="24" y="18" fontFamily="Cambria Math, Times New Roman, serif" fontSize="13" fontWeight="bold" fill="#3b5bfd">∑</text>
        <text x="40" y="18" fontFamily="Cambria Math, Times New Roman, serif" fontSize="12" fontStyle="italic" fontWeight="bold" fill="#1e293b">x</text>
        <text x="48" y="21" fontFamily="Cambria Math, Times New Roman, serif" fontSize="8" fontStyle="italic" fill="#64748b">kj</text>
        <text x="56" y="12" fontFamily="sans-serif" fontSize="8" fontWeight="bold" fill="#1e293b">²</text>
      </svg>
    </div>
  );
}

export function MiniVectorNormalizationBadge() {
  return (
    <span style={{ display: "inline-flex", alignItems: "center", verticalAlign: "middle" }}>
      <svg width="150" height="30" viewBox="0 0 150 30" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ display: "inline-block" }}>
        <rect width="150" height="30" rx="8" fill="#eff6ff" stroke="#bfdbfe" />
        
        {/* r_ij = */}
        <text x="10" y="20" fontFamily="Cambria Math, Times New Roman, serif" fontSize="14" fontStyle="italic" fontWeight="bold" fill="#1e3a8a">r</text>
        <text x="17" y="23" fontFamily="Cambria Math, Times New Roman, serif" fontSize="9" fontStyle="italic" fill="#3b82f6">ij</text>
        <text x="28" y="20" fontFamily="sans-serif" fontSize="13" fontWeight="bold" fill="#1e3a8a">=</text>
        
        {/* Pembilang x_ij */}
        <text x="48" y="13" fontFamily="Cambria Math, Times New Roman, serif" fontSize="12" fontStyle="italic" fontWeight="bold" fill="#1d4ed8">x</text>
        <text x="55" y="16" fontFamily="Cambria Math, Times New Roman, serif" fontSize="8" fontStyle="italic" fill="#3b82f6">ij</text>
        
        {/* Garis Pecahan */}
        <line x1="42" y1="17" x2="142" y2="17" stroke="#1e3a8a" strokeWidth="1.2" />
        
        {/* Akar dan Penyebut sqrt(sum(x_kj^2)) */}
        <path d="M 66 22 L 69 22 L 71 27 L 75 18 L 142 18" stroke="#dc2626" strokeWidth="1.3" fill="none" strokeLinecap="round" strokeLinejoin="round" />
        <text x="78" y="27" fontFamily="Cambria Math, Times New Roman, serif" fontSize="11" fontWeight="bold" fill="#dc2626">∑</text>
        <text x="92" y="26" fontFamily="Cambria Math, Times New Roman, serif" fontSize="11" fontStyle="italic" fontWeight="bold" fill="#1e293b">x</text>
        <text x="99" y="29" fontFamily="Cambria Math, Times New Roman, serif" fontSize="8" fontStyle="italic" fill="#64748b">kj</text>
        <text x="107" y="21" fontFamily="sans-serif" fontSize="8" fontWeight="bold" fill="#1e293b">²</text>
      </svg>
    </span>
  );
}


