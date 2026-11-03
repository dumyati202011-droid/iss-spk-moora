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

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { code, name, type, weight, division, description } = body;

    if (!name || weight === undefined || !division) {
      return NextResponse.json(
        { success: false, message: "Nama, bobot, dan divisi kriteria wajib diisi" },
        { status: 400 }
      );
    }

    // Auto-generate code C1, C2, dst jika tidak diisi
    let finalCode = code?.trim().toUpperCase();
    if (!finalCode) {
      const existing = await prisma.criteria.findMany({
        where: { division },
        select: { code: true },
      });
      const numbers = existing
        .map((c) => parseInt(c.code.replace(/\D/g, "") || "0", 10))
        .filter((n) => !isNaN(n));
      const nextNum = numbers.length > 0 ? Math.max(...numbers) + 1 : 1;
      finalCode = `C${nextNum}`;
    }

    // Pastikan kode unik per divisi
    const existingSame = await prisma.criteria.findFirst({
      where: { code: finalCode, division },
    });
    if (existingSame) {
      return NextResponse.json(
        { success: false, message: `Kode kriteria ${finalCode} sudah ada pada divisi ini.` },
        { status: 400 }
      );
    }

    const created = await prisma.criteria.create({
      data: {
        code: finalCode,
        name,
        type: type === "COST" ? "COST" : "BENEFIT",
        weight: parseFloat(Number(weight).toFixed(4)),
        division,
        description: description || "",
      },
    });

    return NextResponse.json({
      success: true,
      message: `Kriteria ${finalCode} - ${name} berhasil ditambahkan`,
      data: created,
    });
  } catch (error: any) {
    return NextResponse.json({ success: false, message: error.message }, { status: 500 });
  }
}

export async function PUT(request: Request) {
  try {
    const body = await request.json();
    const { id, code, name, type, weight, description } = body;

    if (!id) {
      return NextResponse.json(
        { success: false, message: "ID kriteria wajib disertakan" },
        { status: 400 }
      );
    }

    const updated = await prisma.criteria.update({
      where: { id },
      data: {
        ...(code && { code: code.trim().toUpperCase() }),
        ...(name && { name }),
        ...(type && { type: type === "COST" ? "COST" : "BENEFIT" }),
        ...(weight !== undefined && { weight: parseFloat(Number(weight).toFixed(4)) }),
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

export async function DELETE(request: Request) {
  try {
    const { searchParams } = new URL(request.url);
    const id = searchParams.get("id");

    if (!id) {
      return NextResponse.json(
        { success: false, message: "ID kriteria wajib disertakan" },
        { status: 400 }
      );
    }

    // Hapus nilai assessment score yang terkait kriteria ini terlebih dahulu
    await prisma.assessmentScore.deleteMany({
      where: { criteriaId: id },
    });

    // Hapus kriteria
    const deleted = await prisma.criteria.delete({
      where: { id },
    });

    return NextResponse.json({
      success: true,
      message: `Kriteria ${deleted.code} - ${deleted.name} berhasil dihapus`,
      data: deleted,
    });
  } catch (error: any) {
    return NextResponse.json({ success: false, message: error.message }, { status: 500 });
  }
}
