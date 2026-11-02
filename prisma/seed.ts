import { PrismaClient } from "@prisma/client";
import bcrypt from "bcryptjs";
import { calculateMoora } from "../src/lib/moora";

const prisma = new PrismaClient();

async function main() {
  console.log("🌱 Memulai seeding data awal SPK MOORA (10 CS & 10 Messenger)...");

  // 1. Bersihkan data lama
  await prisma.mooraResult.deleteMany();
  await prisma.assessmentScore.deleteMany();
  await prisma.assessment.deleteMany();
  await prisma.criteria.deleteMany();
  await prisma.employee.deleteMany();
  await prisma.assessmentPeriod.deleteMany();
  await prisma.user.deleteMany();

  // 2. Seed Pengguna (Users)
  const salt = await bcrypt.genSalt(10);
  const defaultPassword = await bcrypt.hash("password123", salt);

  const admin = await prisma.user.create({
    data: {
      username: "admin",
      password: defaultPassword,
      fullName: "Agung Permadi (HRD ISS)",
      role: "SUPER_ADMIN",
    },
  });

  const supervisor = await prisma.user.create({
    data: {
      username: "spv_iss",
      password: defaultPassword,
      fullName: "Septo Aribowo (Supervisor ISS Prodia)",
      role: "SUPERVISOR",
    },
  });

  const manager = await prisma.user.create({
    data: {
      username: "manager_prodia",
      password: defaultPassword,
      fullName: "Siska Darmayanti (Branch Manager Prodia)",
      role: "LAB_MANAGER",
    },
  });

  console.log("✓ Akun pengguna berhasil dibuat.");

  // 3. Seed Periode Penilaian
  const period = await prisma.assessmentPeriod.create({
    data: {
      periodName: "Kuartal III 2026",
      year: 2026,
      status: "ACTIVE",
      startDate: new Date("2026-07-01"),
      endDate: new Date("2026-09-30"),
    },
  });

  console.log("✓ Periode penilaian berhasil dibuat.");

  // 4. Seed Kriteria Cleaning Service (Total Bobot = 1.0)
  const csCriteria = [
    {
      code: "C1",
      name: "Kedisiplinan & Presensi Kehadiran",
      type: "BENEFIT",
      weight: 0.2,
      division: "CLEANING_SERVICE",
      description: "Tingkat kehadiran, ketepatan waktu jam kerja dan absensi harian",
    },
    {
      code: "C2",
      name: "Kualitas Kebersihan & Kerapihan Area",
      type: "BENEFIT",
      weight: 0.25,
      division: "CLEANING_SERVICE",
      description: "Hasil checklist harian kebersihan ruang lab, poliklinik, dan toilet",
    },
    {
      code: "C3",
      name: "Kepatuhan SOP APD & Penanganan Limbah Medis",
      type: "BENEFIT",
      weight: 0.25,
      division: "CLEANING_SERVICE",
      description: "Disiplin penggunaan sarung tangan, masker, dan pemilahan safety box limbah B3",
    },
    {
      code: "C4",
      name: "Sikap & Kerjasama Tim (Attitude)",
      type: "BENEFIT",
      weight: 0.15,
      division: "CLEANING_SERVICE",
      description: "Kesopanan terhadap pasien/staf lab dan inisiatif saling membantu rekan",
    },
    {
      code: "C5",
      name: "Jumlah Komplain / Teguran Klien",
      type: "COST",
      weight: 0.15,
      division: "CLEANING_SERVICE",
      description: "Jumlah catatan teguran atau ketidaksesuaian kerja dari pihak Prodia Kebayoran",
    },
  ];

  for (const c of csCriteria) {
    await prisma.criteria.create({ data: c });
  }

  // 5. Seed Kriteria Messenger (Total Bobot = 1.0)
  const msgCriteria = [
    {
      code: "C1",
      name: "Kedisiplinan & Presensi Kehadiran",
      type: "BENEFIT",
      weight: 0.2,
      division: "MESSENGER",
      description: "Ketepatan jam stand-by dan presensi pengiriman sampel",
    },
    {
      code: "C2",
      name: "Ketepatan Waktu Pengantaran Sampel (TAT)",
      type: "BENEFIT",
      weight: 0.3,
      division: "MESSENGER",
      description: "Kecepatan dan ketepatan rute pengantaran spesimen darah/hasil tes",
    },
    {
      code: "C3",
      name: "Integritas & Keamanan Sampel Lab",
      type: "BENEFIT",
      weight: 0.2,
      division: "MESSENGER",
      description: "Penjagaan suhu coolbox, tidak ada sampel tumpah/rusak/tertukar",
    },
    {
      code: "C4",
      name: "Sikap & Komunikasi Layanan",
      type: "BENEFIT",
      weight: 0.15,
      division: "MESSENGER",
      description: "Keramahan kepada dokter/perawat/faskes pengirim rujukan sampel",
    },
    {
      code: "C5",
      name: "Jumlah Keterlambatan / Komplain Rute",
      type: "COST",
      weight: 0.15,
      division: "MESSENGER",
      description: "Jumlah insiden keterlambatan serah-terima sampel atau komplain klien",
    },
  ];

  for (const c of msgCriteria) {
    await prisma.criteria.create({ data: c });
  }

  console.log("✓ Kriteria Cleaning Service dan Messenger berhasil dibuat.");

  // 6. Seed Karyawan (9 CS & 6 Messenger, Total 15 Orang)
  const employeesData = [
    // 9 Cleaning Service Personel
    { nip: "CS-001", fullName: "Ahmad Fauzi", division: "CLEANING_SERVICE" },
    { nip: "CS-002", fullName: "Siti Rahmawati", division: "CLEANING_SERVICE" },
    { nip: "CS-003", fullName: "Bambang Hermanto", division: "CLEANING_SERVICE" },
    { nip: "CS-004", fullName: "Dewi Anggraini", division: "CLEANING_SERVICE" },
    { nip: "CS-005", fullName: "Eko Prasetyo", division: "CLEANING_SERVICE" },
    { nip: "CS-006", fullName: "Nurul Hidayah", division: "CLEANING_SERVICE" },
    { nip: "CS-007", fullName: "Agus Setiawan", division: "CLEANING_SERVICE" },
    { nip: "CS-008", fullName: "Sri Wahyuni", division: "CLEANING_SERVICE" },
    { nip: "CS-009", fullName: "Hendra Saputra", division: "CLEANING_SERVICE" },

    // 6 Messenger (Kurir Lab) Personel
    { nip: "MSG-001", fullName: "Rendy Pratama", division: "MESSENGER" },
    { nip: "MSG-002", fullName: "Dodi Kurniawan", division: "MESSENGER" },
    { nip: "MSG-003", fullName: "Gilang Ramadhan", division: "MESSENGER" },
    { nip: "MSG-004", fullName: "Fajar Hidayat", division: "MESSENGER" },
    { nip: "MSG-005", fullName: "Ilham Maulana", division: "MESSENGER" },
    { nip: "MSG-006", fullName: "Bagas Wicaksono", division: "MESSENGER" },
  ];

  const createdEmployees: Record<string, any> = {};
  for (const emp of employeesData) {
    const created = await prisma.employee.create({
      data: {
        nip: emp.nip,
        fullName: emp.fullName,
        division: emp.division,
        placementUnit: "Prodia Kebayoran",
        joinDate: new Date("2023-01-15"),
        isActive: true,
      },
    });
    createdEmployees[emp.nip] = created;
  }

  console.log("✓ 15 Data karyawan Prodia Kebayoran (9 CS & 6 MSG) berhasil dibuat.");

  // 7. Ambil kriteria terdaftar
  const allCsCriteria = await prisma.criteria.findMany({
    where: { division: "CLEANING_SERVICE" },
    orderBy: { code: "asc" },
  });

  const allMsgCriteria = await prisma.criteria.findMany({
    where: { division: "MESSENGER" },
    orderBy: { code: "asc" },
  });

  // 8. Skor Penilaian Riil untuk 9 Cleaning Service (C1..C4 Benefit, C5 Cost)
  const csScores: Record<string, number[]> = {
    "CS-001": [92, 90, 88, 85, 10], // Ahmad Fauzi
    "CS-002": [94, 98, 96, 92, 4],  // Siti Rahmawati (Unggul #1)
    "CS-003": [80, 82, 85, 78, 25], // Bambang Hermanto
    "CS-004": [88, 89, 90, 88, 10], // Dewi Anggraini
    "CS-005": [75, 78, 80, 82, 30], // Eko Prasetyo
    "CS-006": [90, 93, 94, 89, 6],  // Nurul Hidayah (Unggul #2)
    "CS-007": [82, 84, 86, 80, 20], // Agus Setiawan
    "CS-008": [89, 92, 91, 88, 9],  // Sri Wahyuni (Unggul #3)
    "CS-009": [78, 80, 79, 81, 28], // Hendra Saputra
  };

  const csRawScoresMap: Record<string, Record<string, number>> = {};
  for (const [nip, scores] of Object.entries(csScores)) {
    const emp = createdEmployees[nip];
    csRawScoresMap[emp.id] = {};

    const assessment = await prisma.assessment.create({
      data: {
        periodId: period.id,
        employeeId: emp.id,
        userId: supervisor.id,
      },
    });

    for (let i = 0; i < allCsCriteria.length; i++) {
      await prisma.assessmentScore.create({
        data: {
          assessmentId: assessment.id,
          criteriaId: allCsCriteria[i].id,
          rawScore: scores[i],
        },
      });
      csRawScoresMap[emp.id][allCsCriteria[i].id] = scores[i];
    }
  }

  // 9. Skor Penilaian Riil untuk 6 Messenger (C1..C4 Benefit, C5 Cost)
  const msgScores: Record<string, number[]> = {
    "MSG-001": [93, 97, 96, 91, 4],  // Rendy Pratama (Unggul #1)
    "MSG-002": [85, 86, 88, 85, 15], // Dodi Kurniawan
    "MSG-003": [90, 92, 93, 90, 8],  // Gilang Ramadhan (Unggul #3)
    "MSG-004": [78, 80, 82, 80, 30], // Fajar Hidayat
    "MSG-005": [88, 89, 90, 87, 10], // Ilham Maulana
    "MSG-006": [82, 85, 86, 84, 20], // Bagas Wicaksono
  };

  const msgRawScoresMap: Record<string, Record<string, number>> = {};
  for (const [nip, scores] of Object.entries(msgScores)) {
    const emp = createdEmployees[nip];
    msgRawScoresMap[emp.id] = {};

    const assessment = await prisma.assessment.create({
      data: {
        periodId: period.id,
        employeeId: emp.id,
        userId: supervisor.id,
      },
    });

    for (let i = 0; i < allMsgCriteria.length; i++) {
      await prisma.assessmentScore.create({
        data: {
          assessmentId: assessment.id,
          criteriaId: allMsgCriteria[i].id,
          rawScore: scores[i],
        },
      });
      msgRawScoresMap[emp.id][allMsgCriteria[i].id] = scores[i];
    }
  }

  console.log("✓ Sesi penilaian dan skor matriks X_ij untuk 20 karyawan berhasil diisi.");

  // 10. Pre-kalkulasi Hasil MOORA untuk CS
  const csEmployees = employeesData
    .filter((e) => e.division === "CLEANING_SERVICE")
    .map((e) => createdEmployees[e.nip]);

  const csMoora = calculateMoora(csEmployees, allCsCriteria, csRawScoresMap);
  for (const r of csMoora.rankingResults) {
    await prisma.mooraResult.create({
      data: {
        periodId: period.id,
        employeeId: r.employee.id,
        division: "CLEANING_SERVICE",
        sumBenefit: r.sumBenefit,
        sumCost: r.sumCost,
        yScore: r.yScore,
        rankPosition: r.rank,
      },
    });
  }

  // 11. Pre-kalkulasi Hasil MOORA untuk Messenger
  const msgEmployees = employeesData
    .filter((e) => e.division === "MESSENGER")
    .map((e) => createdEmployees[e.nip]);

  const msgMoora = calculateMoora(msgEmployees, allMsgCriteria, msgRawScoresMap);
  for (const r of msgMoora.rankingResults) {
    await prisma.mooraResult.create({
      data: {
        periodId: period.id,
        employeeId: r.employee.id,
        division: "MESSENGER",
        sumBenefit: r.sumBenefit,
        sumCost: r.sumCost,
        yScore: r.yScore,
        rankPosition: r.rank,
      },
    });
  }

  console.log("🚀 Ranking MOORA otomatis terisi untuk 10 CS & 10 Messenger!");
}

main()
  .catch((e) => {
    console.error("❌ Error saat seeding:", e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
