import { NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";

export async function GET() {
  try {
    const [employees, criteria, periods, assessments, mooraResults, users] = await Promise.all([
      prisma.employee.findMany({
        orderBy: [{ division: "asc" }, { nip: "asc" }],
      }),
      prisma.criteria.findMany({
        orderBy: [{ division: "asc" }, { code: "asc" }],
      }),
      prisma.assessmentPeriod.findMany({
        orderBy: { createdAt: "desc" },
      }),
      prisma.assessment.findMany({
        include: {
          scores: true,
          employee: true,
        },
      }),
      prisma.mooraResult.findMany({
        include: {
          employee: true,
        },
        orderBy: { rankPosition: "asc" },
      }),
      prisma.user.findMany({
        select: { id: true, username: true, fullName: true, role: true },
      }),
    ]);

    return NextResponse.json({
      success: true,
      data: {
        employees,
        criteria,
        periods,
        assessments,
        mooraResults,
        users,
      },
    });
  } catch (error: any) {
    console.error("Error fetching data:", error);
    return NextResponse.json(
      { success: false, message: error.message || "Gagal memuat data dari database" },
      { status: 500 }
    );
  }
}
