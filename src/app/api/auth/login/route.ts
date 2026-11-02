import { NextResponse } from "next/server";
import { prisma } from "@/lib/prisma";
import bcrypt from "bcryptjs";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { username, password } = body;

    if (!username || !password) {
      return NextResponse.json(
        { success: false, message: "Username dan password wajib diisi" },
        { status: 400 }
      );
    }

    const user = await prisma.user.findUnique({
      where: { username },
    });

    if (!user) {
      return NextResponse.json(
        { success: false, message: "Username atau password salah" },
        { status: 401 }
      );
    }

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return NextResponse.json(
        { success: false, message: "Username atau password salah" },
        { status: 401 }
      );
    }

    const safeUser = {
      id: user.id,
      username: user.username,
      fullName: user.fullName,
      role: user.role,
    };

    const response = NextResponse.json({
      success: true,
      message: "Login berhasil",
      user: safeUser,
    });

    // Simpan cookie auth sederhana
    response.cookies.set("spk_session", JSON.stringify(safeUser), {
      httpOnly: false, // agar bisa dibaca client-side jika diperlukan
      path: "/",
      maxAge: 60 * 60 * 24 * 7, // 7 hari
    });

    return response;
  } catch (error: any) {
    console.error("Login error:", error);
    return NextResponse.json(
      { success: false, message: error.message || "Terjadi kesalahan saat login" },
      { status: 500 }
    );
  }
}
