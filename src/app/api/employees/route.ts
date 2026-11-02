import { NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";

export async function GET() {
  try {
    const employees = await prisma.employee.findMany({
      orderBy: [{ division: "asc" }, { nip: "asc" }],
    });
    return NextResponse.json({ success: true, data: employees });
  } catch (error: any) {
    return NextResponse.json({ success: false, message: error.message }, { status: 500 });
  }
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { nip, fullName, division, placementUnit } = body;

    if (!nip || !fullName || !division) {
      return NextResponse.json(
        { success: false, message: "Field NIP, Nama Lengkap, dan Divisi wajib diisi" },
        { status: 400 }
      );
    }

    const existing = await prisma.employee.findUnique({
      where: { nip },
    });

    if (existing) {
      return NextResponse.json(
        { success: false, message: `Karyawan dengan NIP ${nip} sudah terdaftar` },
        { status: 400 }
      );
    }

    const newEmployee = await prisma.employee.create({
      data: {
        nip,
        fullName,
        division,
        placementUnit: placementUnit || "Prodia Kebayoran",
        isActive: true,
      },
    });

    return NextResponse.json({
      success: true,
      message: "Karyawan baru berhasil ditambahkan",
      data: newEmployee,
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
      return NextResponse.json({ success: false, message: "ID karyawan wajib disertakan" }, { status: 400 });
    }

    await prisma.employee.delete({
      where: { id },
    });

    return NextResponse.json({ success: true, message: "Karyawan berhasil dihapus" });
  } catch (error: any) {
    return NextResponse.json({ success: false, message: error.message }, { status: 500 });
  }
}
