import { NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { periodId, employeeId, scores, userId } = body;

    if (!periodId || !employeeId || !scores) {
      return NextResponse.json(
        { success: false, message: "Field periodId, employeeId, dan scores wajib disertakan" },
        { status: 400 }
      );
    }

    // Default evaluator jika tidak disertakan
    const evaluatorUser = userId
      ? userId
      : (await prisma.user.findFirst({ where: { role: "SUPERVISOR" } }))?.id ||
        (await prisma.user.findFirst())?.id;

    if (!evaluatorUser) {
      return NextResponse.json(
        { success: false, message: "User evaluator tidak ditemukan" },
        { status: 400 }
      );
    }

    // Upsert assessment
    let assessment = await prisma.assessment.findUnique({
      where: {
        periodId_employeeId: {
          periodId,
          employeeId,
        },
      },
    });

    if (!assessment) {
      assessment = await prisma.assessment.create({
        data: {
          periodId,
          employeeId,
          userId: evaluatorUser,
        },
      });
    }

    // Simpan masing-masing nilai kriteria
    for (const [criteriaId, rawScore] of Object.entries(scores)) {
      const scoreNum = Number(rawScore);
      await prisma.assessmentScore.upsert({
        where: {
          assessmentId_criteriaId: {
            assessmentId: assessment.id,
            criteriaId,
          },
        },
        create: {
          assessmentId: assessment.id,
          criteriaId,
          rawScore: scoreNum,
        },
        update: {
          rawScore: scoreNum,
        },
      });
    }

    return NextResponse.json({
      success: true,
      message: "Data penilaian berhasil disimpan.",
    });
  } catch (error: any) {
    console.error("Error saving assessment:", error);
    return NextResponse.json(
      { success: false, message: error.message || "Gagal menyimpan penilaian" },
      { status: 500 }
    );
  }
}
