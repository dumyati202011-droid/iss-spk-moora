import { NextResponse } from "next/server";
import { cookies } from "next/headers";

export async function GET() {
  try {
    const cookieStore = await cookies();
    const sessionCookie = cookieStore.get("spk_session");

    if (!sessionCookie?.value) {
      return NextResponse.json({ success: false, user: null });
    }

    const user = JSON.parse(sessionCookie.value);
    return NextResponse.json({ success: true, user });
  } catch (err) {
    return NextResponse.json({ success: false, user: null });
  }
}
