import { NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import { calculateMoora } from "@/lib/moora";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { periodId, division } = body;

    if (!periodId || !division) {
      return NextResponse.json(
        { success: false, message: "Parameter periodId dan division wajib diisi" },
        { status: 400 }
      );
    }

    // 1. Ambil Kriteria untuk divisi ini
    const criteria = await prisma.criteria.findMany({
      where: { division },
      orderBy: { code: "asc" },
    });

    if (criteria.length === 0) {
      return NextResponse.json(
        { success: false, message: `Belum ada kriteria untuk kategori ${division}` },
        { status: 400 }
      );
    }

    // 2. Ambil Karyawan aktif di divisi ini
    const employees = await prisma.employee.findMany({
      where: { division, isActive: true },
      orderBy: { nip: "asc" },
    });

    if (employees.length === 0) {
      return NextResponse.json(
        { success: false, message: `Belum ada karyawan aktif untuk kategori ${division}` },
        { status: 400 }
      );
    }

    // 3. Ambil data penilaian yang sudah diinput
    const assessments = await prisma.assessment.findMany({
      where: {
        periodId,
        employeeId: { in: employees.map((e) => e.id) },
      },
      include: {
        scores: true,
      },
    });

    // Susun Map nilai X_ij
    const rawScoresMap: Record<string, Record<string, number>> = {};
    for (const a of assessments) {
      if (!rawScoresMap[a.employeeId]) {
        rawScoresMap[a.employeeId] = {};
      }
      for (const s of a.scores) {
        rawScoresMap[a.employeeId][s.criteriaId] = s.rawScore;
      }
    }

    // 4. Jalankan komputasi MOORA
    const alternatives = employees.map((e) => ({
      id: e.id,
      nip: e.nip,
      fullName: e.fullName,
      division: e.division,
    }));

    const mooraOutput = calculateMoora(alternatives, criteria, rawScoresMap);

    // 5. Simpan snapshot hasil ranking ke tabel MooraResult secara transaksional
    await prisma.$transaction(async (tx) => {
      // Hapus hasil lama untuk divisi dan periode ini
      await tx.mooraResult.deleteMany({
        where: {
          periodId,
          division,
        },
      });

      // Simpan hasil baru
      for (const item of mooraOutput.rankingResults) {
        await tx.mooraResult.create({
          data: {
            periodId,
            employeeId: item.employee.id,
            division,
            sumBenefit: item.sumBenefit,
            sumCost: item.sumCost,
            yScore: item.yScore,
            rankPosition: item.rank,
          },
        });
      }
    });

    return NextResponse.json({
      success: true,
      message: `Perhitungan MOORA untuk kategori ${division} berhasil diselesaikan.`,
      data: mooraOutput,
    });
  } catch (error: any) {
    console.error("Error calculating MOORA:", error);
    return NextResponse.json(
      { success: false, message: error.message || "Terjadi kesalahan saat memproses MOORA" },
      { status: 500 }
    );
  }
}
