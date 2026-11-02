export interface AlternativeItem {
  id: string;
  nip: string;
  fullName: string;
  division: string;
}

export interface CriteriaItem {
  id: string;
  code: string;
  name: string;
  type: "BENEFIT" | "COST" | string;
  weight: number;
  division: string;
}

export interface RawScoresMap {
  [employeeId: string]: {
    [criteriaId: string]: number;
  };
}

export interface MooraCalculationOutput {
  alternatives: AlternativeItem[];
  criteria: CriteriaItem[];
  decisionMatrix: {
    employee: AlternativeItem;
    scores: Record<string, number>;
  }[];
  divisors: Record<string, number>; // sqrt(sum(x^2)) per kriteria
  normalizedMatrix: {
    employee: AlternativeItem;
    scores: Record<string, number>;
  }[];
  weightedMatrix: {
    employee: AlternativeItem;
    scores: Record<string, number>;
  }[];
  rankingResults: {
    rank: number;
    employee: AlternativeItem;
    sumBenefit: number;
    sumCost: number;
    yScore: number;
  }[];
}

/**
 * Engine Perhitungan MOORA (Multi-Objective Optimization on the basis of Ratio Analysis)
 * 100% Deterministik, akurat, dan transparan untuk audit akademis.
 */
export function calculateMoora(
  alternatives: AlternativeItem[],
  criteriaList: CriteriaItem[],
  rawScores: RawScoresMap
): MooraCalculationOutput {
  if (alternatives.length === 0 || criteriaList.length === 0) {
    return {
      alternatives,
      criteria: criteriaList,
      decisionMatrix: [],
      divisors: {},
      normalizedMatrix: [],
      weightedMatrix: [],
      rankingResults: [],
    };
  }

  // 1. Matriks Keputusan Awal (X)
  const decisionMatrix = alternatives.map((alt) => {
    const scores: Record<string, number> = {};
    for (const c of criteriaList) {
      scores[c.id] = rawScores[alt.id]?.[c.id] ?? 0;
    }
    return { employee: alt, scores };
  });

  // 2. Hitung Pembagi Vektor Tiap Kriteria: sqrt(sum(x_kj^2))
  const divisors: Record<string, number> = {};
  for (const c of criteriaList) {
    let sumOfSquares = 0;
    for (const alt of alternatives) {
      const val = rawScores[alt.id]?.[c.id] ?? 0;
      sumOfSquares += val * val;
    }
    // Proteksi pembagian nol jika seluruh nilai 0
    divisors[c.id] = sumOfSquares > 0 ? Math.sqrt(sumOfSquares) : 1e-9;
  }

  // 3. Matriks Ternormalisasi (R): r_ij = x_ij / divisor_j
  const normalizedMatrix = alternatives.map((alt) => {
    const scores: Record<string, number> = {};
    for (const c of criteriaList) {
      const x = rawScores[alt.id]?.[c.id] ?? 0;
      scores[c.id] = x / divisors[c.id];
    }
    return { employee: alt, scores };
  });

  // 4. Matriks Ternormalisasi Terbobot (V): v_ij = w_j * r_ij
  const weightedMatrix = alternatives.map((alt) => {
    const scores: Record<string, number> = {};
    for (const c of criteriaList) {
      const r = normalizedMatrix.find((item) => item.employee.id === alt.id)?.scores[c.id] ?? 0;
      scores[c.id] = r * c.weight;
    }
    return { employee: alt, scores };
  });

  // 5. Optimasi Nilai Multiobjektif (y_i = sum(Benefit) - sum(Cost))
  const calculatedRows = alternatives.map((alt) => {
    const wRow = weightedMatrix.find((item) => item.employee.id === alt.id)?.scores ?? {};
    let sumBenefit = 0;
    let sumCost = 0;

    for (const c of criteriaList) {
      const v = wRow[c.id] ?? 0;
      if (c.type === "BENEFIT") {
        sumBenefit += v;
      } else {
        sumCost += v;
      }
    }

    const yScore = sumBenefit - sumCost;

    return {
      employee: alt,
      sumBenefit,
      sumCost,
      yScore,
    };
  });

  // 6. Urutkan Ranking (yScore terbesar -> Peringkat 1)
  calculatedRows.sort((a, b) => b.yScore - a.yScore);

  const rankingResults = calculatedRows.map((row, index) => ({
    rank: index + 1,
    ...row,
  }));

  return {
    alternatives,
    criteria: criteriaList,
    decisionMatrix,
    divisors,
    normalizedMatrix,
    weightedMatrix,
    rankingResults,
  };
}
