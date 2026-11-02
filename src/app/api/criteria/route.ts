import { NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";

export async function GET() {
  try {
    const criteria = await prisma.criteria.findMany({
      orderBy: [{ division: "asc" }, { code: "asc" }],
    });
    return NextResponse.json({ success: true, data: criteria });
  } catch (error: any) {
    return NextResponse.json({ success: false, message: error.message }, { status: 500 });
  }
}

export async function PUT(request: Request) {
  try {
    const body = await request.json();
    const { id, weight, name, type, description } = body;

    if (!id || weight === undefined) {
      return NextResponse.json(
        { success: false, message: "ID dan bobot kriteria wajib disertakan" },
        { status: 400 }
      );
    }

    const updated = await prisma.criteria.update({
      where: { id },
      data: {
        weight: Number(weight),
        ...(name && { name }),
        ...(type && { type }),
        ...(description !== undefined && { description }),
      },
    });

    return NextResponse.json({
      success: true,
      message: "Kriteria berhasil diperbarui",
      data: updated,
    });
  } catch (error: any) {
    return NextResponse.json({ success: false, message: error.message }, { status: 500 });
  }
}
