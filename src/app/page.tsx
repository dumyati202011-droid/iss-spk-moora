"use client";

import React, { useState, useEffect, useMemo } from "react";
import {
  LayoutDashboard,
  Users,
  Scale,
  ClipboardCheck,
  Calculator,
  FileText,
  Award,
  Sparkles,
  ArrowRight,
  RefreshCw,
  Plus,
  Trash2,
  Printer,
  ShieldCheck,
  ShieldAlert,
  Building2,
  CheckCircle2,
  TrendingUp,
  AlertCircle,
  HelpCircle,
  LogOut,
  Lock,
  KeyRound,
  User as UserIcon,
  Search,
  Filter,
  Check,
  Calendar,
  Clock,
  Layers,
  ChevronRight,
  Info,
  Bell,
  Settings,
  Phone,
  Mail,
  Star,
  CheckCircle,
  MoreVertical,
  SlidersHorizontal,
  X,
  CheckCheck,
  Edit3,
} from "lucide-react";

import {
  FormulaMatrixX,
  FormulaVectorNormalization,
  FormulaWeightedMatrix,
  FormulaOptimizationYi,
  MiniVectorDivisorBadge,
  MiniVectorNormalizationBadge,
} from "@/components/MathFormulaCards";

interface AuthUser {
  id: string;
  username: string;
  fullName: string;
  role: string;
}

interface Employee {
  id: string;
  nip: string;
  fullName: string;
  division: string;
  placementUnit: string;
  isActive: boolean;
}

interface Criteria {
  id: string;
  code: string;
  name: string;
  type: string;
  weight: number;
  division: string;
  description?: string;
}

interface AssessmentPeriod {
  id: string;
  periodName: string;
  year: number;
  status: string;
}

interface MooraResultItem {
  id: string;
  periodId: string;
  employeeId: string;
  division: string;
  sumBenefit: number;
  sumCost: number;
  yScore: number;
  rankPosition: number;
  employee: Employee;
}

interface NotificationItem {
  id: string;
  title: string;
  message: string;
  time: string;
  read: boolean;
  category: "moora" | "incentive" | "assessment" | "system";
  targetMenu?: "dashboard" | "moora" | "assessment" | "reports";
}

export default function Home() {
  // Navigation & Category Tab
  const [activeMenu, setActiveMenu] = useState<
    "dashboard" | "moora" | "assessment" | "employees" | "criteria" | "reports"
  >("dashboard");
  const [selectedDivision, setSelectedDivision] = useState<"CLEANING_SERVICE" | "MESSENGER">("CLEANING_SERVICE");

  // State Data Database
  const [loading, setLoading] = useState(true);
  const [calculating, setCalculating] = useState(false);
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [criteria, setCriteria] = useState<Criteria[]>([]);
  const [periods, setPeriods] = useState<AssessmentPeriod[]>([]);
  const [assessments, setAssessments] = useState<any[]>([]);
  const [mooraResults, setMooraResults] = useState<MooraResultItem[]>([]);
  const [mooraStepData, setMooraStepData] = useState<any>(null);
  const [mathStepTab, setMathStepTab] = useState<1 | 2 | 3 | 4>(1);

  // Settings & Notification State
  const [showSettings, setShowSettings] = useState(false);
  const [showNotifications, setShowNotifications] = useState(false);
  const [yiThreshold, setYiThreshold] = useState<number>(0.2);
  const [autoSyncCalc, setAutoSyncCalc] = useState<boolean>(true);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const [notifications, setNotifications] = useState<NotificationItem[]>([
    {
      id: "notif-1",
      title: "Kalkulasi MOORA Q3-2026 Selesai",
      message: "Pemeringkatan otomatis selesai. Rendy Pratama memimpin dengan Yi = 0.2817.",
      time: "10 menit lalu",
      read: false,
      category: "moora",
      targetMenu: "moora",
    },
    {
      id: "notif-2",
      title: "Rekomendasi Insentif Siap SK",
      message: "Kandidat Top 3 Prodia Kebayoran memenuhi syarat penerbitan rekomendasi insentif.",
      time: "45 menit lalu",
      read: false,
      category: "incentive",
      targetMenu: "reports",
    },
    {
      id: "notif-3",
      title: "Data Penilaian 20 Karyawan Lengkap",
      message: "10 Cleaning Service & 10 Messenger telah dinilai oleh SPV Septo Aribowo.",
      time: "2 jam lalu",
      read: false,
      category: "assessment",
      targetMenu: "assessment",
    },
    {
      id: "notif-4",
      title: "Sinkronisasi Standar Mutu Prodia",
      message: "Parameter evaluasi operasional unit Prodia Kebayoran tervalidasi aktif.",
      time: "1 hari lalu",
      read: true,
      category: "system",
      targetMenu: "dashboard",
    },
  ]);

  const unreadCount = useMemo(() => notifications.filter((n) => !n.read).length, [notifications]);

  const markAllNotificationsAsRead = () => {
    setNotifications((prev) => prev.map((n) => ({ ...n, read: true })));
    showToast("Semua notifikasi telah ditandai sudah dibaca");
  };

  const handleNotificationClick = (item: NotificationItem) => {
    setNotifications((prev) =>
      prev.map((n) => (n.id === item.id ? { ...n, read: true } : n))
    );
    if (item.targetMenu) {
      setActiveMenu(item.targetMenu);
    }
    setShowNotifications(false);
  };

  // Search
  const [searchKeyword, setSearchKeyword] = useState("");

  // Form Penilaian
  const [selectedEmployeeForEval, setSelectedEmployeeForEval] = useState<string>("");
  const [evalScores, setEvalScores] = useState<Record<string, number>>({});
  const [evalSaving, setEvalSaving] = useState(false);
  const [toastMessage, setToastMessage] = useState<{ type: "success" | "error"; text: string } | null>(null);

  // Form Karyawan Baru
  const [showAddEmployeeForm, setShowAddEmployeeForm] = useState(false);
  const [newNip, setNewNip] = useState("");
  const [newName, setNewName] = useState("");
  const [newDivision, setNewDivision] = useState<"CLEANING_SERVICE" | "MESSENGER">("CLEANING_SERVICE");

  // Form Kriteria Baru & Edit (Khusus Admin HR)
  const [showAddCriteriaForm, setShowAddCriteriaForm] = useState(false);
  const [newCritCode, setNewCritCode] = useState("");
  const [newCritName, setNewCritName] = useState("");
  const [newCritType, setNewCritType] = useState<"BENEFIT" | "COST">("BENEFIT");
  const [newCritWeight, setNewCritWeight] = useState("0.20");
  const [newCritDesc, setNewCritDesc] = useState("");
  const [critSaving, setCritSaving] = useState(false);

  // Edit Kriteria Modal State
  const [editingCriteria, setEditingCriteria] = useState<Criteria | null>(null);
  const [editCritCode, setEditCritCode] = useState("");
  const [editCritName, setEditCritName] = useState("");
  const [editCritType, setEditCritType] = useState<"BENEFIT" | "COST">("BENEFIT");
  const [editCritWeight, setEditCritWeight] = useState("0.20");
  const [editCritDesc, setEditCritDesc] = useState("");

  // Custom Delete Confirmation Modal State
  const [deleteConfirmModal, setDeleteConfirmModal] = useState<{
    isOpen: boolean;
    title: string;
    message: string;
    subMessage?: string;
    onConfirm: () => Promise<void> | void;
  }>({
    isOpen: false,
    title: "",
    message: "",
    subMessage: "",
    onConfirm: () => {},
  });

  // Auth State
  const [currentUser, setCurrentUser] = useState<AuthUser | null>(null);
  const [authChecking, setAuthChecking] = useState(true);
  const [loginUsername, setLoginUsername] = useState("");
  const [loginPassword, setLoginPassword] = useState("");
  const [loginError, setLoginError] = useState("");
  const [loginSubmitting, setLoginSubmitting] = useState(false);

  // RBAC & Approval State
  const [skApproved, setSkApproved] = useState<boolean>(false);
  const userRole = currentUser?.role || "SUPERVISOR";
  const isSupervisor = userRole === "SUPERVISOR";
  const isAdmin = userRole === "SUPER_ADMIN";
  const isManager = userRole === "LAB_MANAGER";

  // Helper untuk Label & Badge Peran
  const getRoleLabel = (role?: string) => {
    if (role === "SUPERVISOR") return "Site Supervisor ISS";
    if (role === "SUPER_ADMIN") return "Super Admin (HRD ISS)";
    if (role === "LAB_MANAGER") return "Branch Manager Prodia";
    return role || "Pengguna";
  };

  const getRoleBadge = (role?: string) => {
    if (role === "SUPERVISOR") {
      return <span className="role-pill-badge supervisor">SPV ISS</span>;
    }
    if (role === "SUPER_ADMIN") {
      return <span className="role-pill-badge admin">Super Admin</span>;
    }
    if (role === "LAB_MANAGER") {
      return <span className="role-pill-badge manager">Manager Prodia</span>;
    }
    return null;
  };

  // Auto fallback menu jika role tidak berwenang
  useEffect(() => {
    if (currentUser) {
      if (isManager && (activeMenu === "assessment" || activeMenu === "employees")) {
        setActiveMenu("dashboard");
      } else if (isSupervisor && activeMenu === "employees") {
        setActiveMenu("dashboard");
      }
    }
  }, [currentUser?.role, activeMenu]);

  // Toast Notification
  const showToast = (text: string, type: "success" | "error" = "success") => {
    setToastMessage({ type, text });
    setTimeout(() => setToastMessage(null), 3800);
  };

  // Check Session
  const checkAuth = async () => {
    try {
      setAuthChecking(true);
      const res = await fetch("/api/auth/me");
      const json = await res.json();
      if (json.success && json.user) {
        setCurrentUser(json.user);
      } else {
        setCurrentUser(null);
      }
    } catch {
      setCurrentUser(null);
    } finally {
      setAuthChecking(false);
    }
  };

  // Fetch All Data
  const fetchData = async () => {
    try {
      setLoading(true);
      const res = await fetch("/api/data");
      const json = await res.json();
      if (json.success) {
        setEmployees(json.data.employees);
        setCriteria(json.data.criteria);
        setPeriods(json.data.periods);
        setAssessments(json.data.assessments);
        setMooraResults(json.data.mooraResults);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    checkAuth();
  }, []);

  useEffect(() => {
    if (currentUser) {
      fetchData();
    }
  }, [currentUser]);

  const currentPeriod = periods[0] || null;

  // Filter Data
  const filteredEmployees = useMemo(() => {
    return employees
      .filter((e) => e.division === selectedDivision)
      .filter((e) =>
        searchKeyword
          ? e.fullName.toLowerCase().includes(searchKeyword.toLowerCase()) ||
            e.nip.toLowerCase().includes(searchKeyword.toLowerCase())
          : true
      );
  }, [employees, selectedDivision, searchKeyword]);

  const filteredCriteria = useMemo(() => {
    return criteria.filter((c) => c.division === selectedDivision);
  }, [criteria, selectedDivision]);

  const filteredResults = useMemo(() => {
    return mooraResults
      .filter((r) => r.division === selectedDivision)
      .filter((r) =>
        searchKeyword
          ? r.employee.fullName.toLowerCase().includes(searchKeyword.toLowerCase()) ||
            r.employee.nip.toLowerCase().includes(searchKeyword.toLowerCase())
          : true
      );
  }, [mooraResults, selectedDivision, searchKeyword]);

  // MOORA Calculation Execution
  const runMooraCalculation = async (silent: boolean = false) => {
    if (!currentPeriod) return;
    try {
      setCalculating(true);
      const res = await fetch("/api/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          periodId: currentPeriod.id,
          division: selectedDivision,
        }),
      });
      const json = await res.json();
      if (json.success) {
        setMooraStepData(json.data);
        await fetchData();
        if (!silent) {
          showToast(`Kalkulasi MOORA kategori ${selectedDivision === "CLEANING_SERVICE" ? "CS" : "Messenger"} berhasil disinkronkan!`);
        }
      } else {
        if (!silent) {
          showToast(json.message || "Gagal menghitung MOORA", "error");
        }
      }
    } catch {
      if (!silent) {
        showToast("Gagal memproses perhitungan", "error");
      }
    } finally {
      setCalculating(false);
    }
  };

  useEffect(() => {
    if (currentPeriod && (activeMenu === "moora" || activeMenu === "dashboard")) {
      runMooraCalculation(true);
    }
  }, [selectedDivision, activeMenu]);

  // Prepare Assessment Form
  useEffect(() => {
    if (selectedEmployeeForEval) {
      const existing = assessments.find(
        (a) => a.employeeId === selectedEmployeeForEval && a.periodId === currentPeriod?.id
      );
      const initial: Record<string, number> = {};
      filteredCriteria.forEach((c) => {
        const found = existing?.scores?.find((s: any) => s.criteriaId === c.id);
        initial[c.id] = found ? found.rawScore : 85;
      });
      setEvalScores(initial);
    }
  }, [selectedEmployeeForEval, selectedDivision, filteredCriteria]);

  // Save Assessment
  const handleSaveAssessment = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedEmployeeForEval || !currentPeriod) return;
    try {
      setEvalSaving(true);
      const res = await fetch("/api/assessments", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          periodId: currentPeriod.id,
          employeeId: selectedEmployeeForEval,
          scores: evalScores,
          userId: currentUser?.id,
        }),
      });
      const json = await res.json();
      if (json.success) {
        showToast("Nilai penilaian berhasil disimpan ke database!");
        await fetchData();
        await runMooraCalculation(true);
      } else {
        showToast(json.message || "Gagal menyimpan penilaian", "error");
      }
    } catch {
      showToast("Kesalahan teknis saat menyimpan", "error");
    } finally {
      setEvalSaving(false);
    }
  };

  // Add Employee
  const handleAddEmployee = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newNip || !newName) return;
    try {
      const res = await fetch("/api/employees", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          nip: newNip,
          fullName: newName,
          division: newDivision,
          placementUnit: "Prodia Kebayoran",
        }),
      });
      const json = await res.json();
      if (json.success) {
        setNewNip("");
        setNewName("");
        setShowAddEmployeeForm(false);
        showToast(`Karyawan baru ${newName} berhasil ditambahkan!`);
        await fetchData();
      } else {
        showToast(json.message || "Gagal menambahkan karyawan", "error");
      }
    } catch {
      showToast("Gagal menghubungi server", "error");
    }
  };

  // Delete Employee (Custom Modal Dialog)
  const handleDeleteEmployee = (id: string, name: string) => {
    setDeleteConfirmModal({
      isOpen: true,
      title: "Hapus Data Personel",
      message: `Apakah Anda yakin ingin menghapus personel "${name}"?`,
      subMessage: "Seluruh riwayat penilaian, skor checklist, dan hasil pemeringkatan MOORA untuk personel ini akan dihapus permanen.",
      onConfirm: async () => {
        try {
          const res = await fetch(`/api/employees?id=${id}`, { method: "DELETE" });
          const json = await res.json();
          if (json.success) {
            showToast(`Personel ${name} berhasil dihapus.`);
            await fetchData();
            await runMooraCalculation(true);
          } else {
            showToast(json.message || "Gagal menghapus", "error");
          }
        } catch {
          showToast("Gagal menghapus personel", "error");
        } finally {
          setDeleteConfirmModal((prev) => ({ ...prev, isOpen: false }));
        }
      },
    });
  };

  // Criteria Handlers (Add, Edit, Delete)
  const openEditCriteriaModal = (c: Criteria) => {
    setEditingCriteria(c);
    setEditCritCode(c.code);
    setEditCritName(c.name);
    setEditCritType(c.type as "BENEFIT" | "COST");
    setEditCritWeight(c.weight.toString());
    setEditCritDesc(c.description || "");
  };

  const handleAddCriteria = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newCritName || !newCritWeight) {
      showToast("Nama dan bobot kriteria wajib diisi", "error");
      return;
    }
    const weightVal = parseFloat(newCritWeight);
    if (isNaN(weightVal) || weightVal <= 0) {
      showToast("Bobot kriteria harus lebih dari 0", "error");
      return;
    }

    try {
      setCritSaving(true);
      const res = await fetch("/api/criteria", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          code: newCritCode,
          name: newCritName,
          type: newCritType,
          weight: weightVal,
          division: selectedDivision,
          description: newCritDesc,
        }),
      });
      const json = await res.json();
      if (json.success) {
        setNewCritCode("");
        setNewCritName("");
        setNewCritDesc("");
        setNewCritWeight("0.20");
        setShowAddCriteriaForm(false);
        showToast(json.message || "Kriteria baru berhasil ditambahkan!");
        await fetchData();
        await runMooraCalculation(false);
      } else {
        showToast(json.message || "Gagal menambahkan kriteria", "error");
      }
    } catch {
      showToast("Gagal menghubungi server", "error");
    } finally {
      setCritSaving(false);
    }
  };

  const handleUpdateCriteria = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!editingCriteria || !editCritName || !editCritWeight) {
      showToast("Nama dan bobot kriteria wajib diisi", "error");
      return;
    }
    const weightVal = parseFloat(editCritWeight);
    if (isNaN(weightVal) || weightVal <= 0) {
      showToast("Bobot kriteria harus lebih dari 0", "error");
      return;
    }

    try {
      setCritSaving(true);
      const res = await fetch("/api/criteria", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          id: editingCriteria.id,
          code: editCritCode,
          name: editCritName,
          type: editCritType,
          weight: weightVal,
          description: editCritDesc,
        }),
      });
      const json = await res.json();
      if (json.success) {
        setEditingCriteria(null);
        showToast(json.message || "Kriteria & bobot berhasil diperbarui!");
        await fetchData();
        await runMooraCalculation(false);
      } else {
        showToast(json.message || "Gagal memperbarui kriteria", "error");
      }
    } catch {
      showToast("Gagal menghubungi server", "error");
    } finally {
      setCritSaving(false);
    }
  };

  // Delete Criteria (Custom Modal Dialog)
  const handleDeleteCriteria = (id: string, code: string, name: string) => {
    setDeleteConfirmModal({
      isOpen: true,
      title: "Hapus Kriteria Evaluasi",
      message: `Apakah Anda yakin ingin menghapus kriteria "${code} - ${name}"?`,
      subMessage: "Nilai penilaian karyawan yang terkait kriteria ini akan disesuaikan otomatis dan ranking matriks MOORA akan langsung dihitung ulang.",
      onConfirm: async () => {
        try {
          const res = await fetch(`/api/criteria?id=${id}`, { method: "DELETE" });
          const json = await res.json();
          if (json.success) {
            showToast(`Kriteria ${code} - ${name} berhasil dihapus.`);
            await fetchData();
            await runMooraCalculation(false);
          } else {
            showToast(json.message || "Gagal menghapus kriteria", "error");
          }
        } catch {
          showToast("Gagal menghapus kriteria", "error");
        } finally {
          setDeleteConfirmModal((prev) => ({ ...prev, isOpen: false }));
        }
      },
    });
  };

  // Auth Handlers
  const handleLogin = async (e?: React.FormEvent, customUser?: string, customPass?: string) => {
    if (e) e.preventDefault();
    const u = customUser || loginUsername;
    const p = customPass || loginPassword;
    if (!u || !p) {
      setLoginError("Masukkan username dan password");
      return;
    }
    try {
      setLoginSubmitting(true);
      setLoginError("");
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: u, password: p }),
      });
      const json = await res.json();
      if (json.success && json.user) {
        setCurrentUser(json.user);
        setLoginUsername("");
        setLoginPassword("");
        await fetchData();
      } else {
        setLoginError(json.message || "Kredensial tidak valid");
      }
    } catch (err: any) {
      setLoginError(err.message || "Gagal menghubungi server");
    } finally {
      setLoginSubmitting(false);
    }
  };

  const handleLogout = async () => {
    try {
      await fetch("/api/auth/logout", { method: "POST" });
    } finally {
      setCurrentUser(null);
    }
  };

  // Top 3 Winners
  const top1 = filteredResults.find((r) => r.rankPosition === 1);
  const top2 = filteredResults.find((r) => r.rankPosition === 2);
  const top3 = filteredResults.find((r) => r.rankPosition === 3);

  // Avatar Color Generator
  const getAvatarGradient = (idx: number) => {
    const gradients = [
      "linear-gradient(135deg, #3b5bfd 0%, #4f46e5 100%)",
      "linear-gradient(135deg, #f97316 0%, #ea580c 100%)",
      "linear-gradient(135deg, #ec4899 0%, #db2777 100%)",
      "linear-gradient(135deg, #06b6d4 0%, #0891b2 100%)",
      "linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)",
    ];
    return gradients[idx % gradients.length];
  };

  // Unified Candidate Avatar Color (Deterministic across vertical & horizontal lists)
  const getCandidateAvatarGradient = (candidate: MooraResultItem, fallbackIdx: number) => {
    if (candidate.rankPosition === 1) return "linear-gradient(135deg, #3b5bfd 0%, #4f46e5 100%)"; // Royal Blue (#3b5bfd)
    if (candidate.rankPosition === 2) return "linear-gradient(135deg, #f97316 0%, #ea580c 100%)"; // Vibrant Orange (#f97316)
    if (candidate.rankPosition === 3) return "linear-gradient(135deg, #ec4899 0%, #db2777 100%)"; // Pink / Magenta (#ec4899)
    return getAvatarGradient(fallbackIdx);
  };

  // =========================================================================
  // RENDER 1: AUTH LOADER
  // =========================================================================
  if (authChecking) {
    return (
      <div style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center" }}>
        <div style={{ textAlign: "center" }}>
          <RefreshCw size={36} className="animate-spin" style={{ color: "#3b5bfd", margin: "0 auto 12px" }} />
          <p style={{ fontWeight: 600, color: "#475569" }}>Memuat Sesi Sistem SPK MOORA...</p>
        </div>
      </div>
    );
  }

  // =========================================================================
  // RENDER 2: LOGIN SCREEN
  // =========================================================================
  if (!currentUser) {
    return (
      <div style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", background: "#f8fafc", padding: "20px" }}>
        <div style={{ width: "100%", maxWidth: "460px", background: "#ffffff", borderRadius: "24px", padding: "40px 36px", border: "1px solid #e2e8f0", boxShadow: "0 10px 30px rgba(0,0,0,0.05)" }}>
          <div style={{ textAlign: "center" }}>
            <div className="brand-badge-circle" style={{ width: "70px", height: "70px", margin: "0 auto 16px" }}>
              <img src="/logo-iss.png" alt="Logo ISS Indonesia" />
            </div>
          <h2 style={{ fontSize: "1.45rem", fontWeight: 800, color: "#0f172a" }}>SPK Kinerja Karyawan MOORA</h2>
          <p style={{ fontSize: "0.85rem", color: "#8c9bb0", marginTop: "4px", marginBottom: "26px" }}>
            PT ISS Indonesia - Evaluasi Mitra Laboratorium Prodia Kebayoran
          </p>

          {loginError && (
            <div style={{ background: "#fef2f2", border: "1px solid #fecaca", color: "#991b1b", padding: "10px 14px", borderRadius: "12px", marginBottom: "18px", fontSize: "0.84rem", display: "flex", alignItems: "center", gap: "8px", textAlign: "left" }}>
              <AlertCircle size={16} />
              <span>{loginError}</span>
            </div>
          )}

          <form onSubmit={(e) => handleLogin(e)} style={{ textAlign: "left" }}>
            <div style={{ marginBottom: "16px" }}>
              <label style={{ display: "block", fontSize: "0.84rem", fontWeight: 700, color: "#334155", marginBottom: "6px" }}>Username:</label>
              <input
                type="text"
                placeholder="Contoh: spv_iss"
                value={loginUsername}
                onChange={(e) => setLoginUsername(e.target.value)}
                style={{ width: "100%", padding: "11px 14px", borderRadius: "12px", border: "1px solid #e2e8f0", fontSize: "0.88rem", outline: "none" }}
                required
              />
            </div>

            <div style={{ marginBottom: "20px" }}>
              <label style={{ display: "block", fontSize: "0.84rem", fontWeight: 700, color: "#334155", marginBottom: "6px" }}>Password:</label>
              <input
                type="password"
                placeholder="••••••••"
                value={loginPassword}
                onChange={(e) => setLoginPassword(e.target.value)}
                style={{ width: "100%", padding: "11px 14px", borderRadius: "12px", border: "1px solid #e2e8f0", fontSize: "0.88rem", outline: "none" }}
                required
              />
            </div>

            <button
              type="submit"
              disabled={loginSubmitting}
              className="hireism-btn-primary"
              style={{ width: "100%", justifyContent: "center", padding: "12px" }}
            >
              <KeyRound size={16} />
              {loginSubmitting ? "Memverifikasi..." : "Masuk ke Sistem"}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

  // =========================================================================
  // RENDER 3: FULL HIREISM 3-COLUMN DASHBOARD WINDOW
  // =========================================================================
  return (
    <div className={`hireism-window ${activeMenu !== "dashboard" ? "no-right-panel" : ""}`}>
      {/* Toast Notification - Sleek, Centered, and Pixel-Perfect */}
      {toastMessage && (
        <div
          className={`app-toast-container ${
            toastMessage.type === "success" ? "toast-success" : "toast-error"
          }`}
          role="status"
          aria-live="polite"
        >
          <div className="app-toast-icon-wrap">
            {toastMessage.type === "success" ? (
              <CheckCircle2 size={18} strokeWidth={2.5} />
            ) : (
              <AlertCircle size={18} strokeWidth={2.5} />
            )}
          </div>

          <div className="app-toast-content">
            <div className="app-toast-title">
              {toastMessage.type === "success" ? "Sinkronisasi Berhasil" : "Perhatian"}
            </div>
            <div className="app-toast-desc">{toastMessage.text}</div>
          </div>

          <button
            type="button"
            className="app-toast-close"
            onClick={() => setToastMessage(null)}
            title="Tutup pemberitahuan"
            aria-label="Tutup"
          >
            <X size={15} />
          </button>
        </div>
      )}

      {/* ===================================================================== */}
      {/* 0. MOBILE TOP APP BAR (Hanya Tampil di Mobile/Tablet <= 1024px)       */}
      {/* ===================================================================== */}
      <header className="mobile-top-bar no-print">
        <div className="mobile-brand-wrap">
          <div className="brand-badge-circle" style={{ width: 34, height: 34, padding: 2 }}>
            <img src="/logo-iss.png" alt="Logo ISS Indonesia" />
          </div>
          <div>
            <div style={{ fontSize: "0.92rem", fontWeight: 800, color: "var(--text-main)", lineHeight: 1.1 }}>ISS Prodia</div>
            <span style={{ fontSize: "0.68rem", color: "var(--brand-blue)", fontWeight: 700 }}>SPK MOORA</span>
          </div>
        </div>

        <div className="mobile-top-actions">
          <button
            type="button"
            className="icon-action-bubble"
            title="Pengaturan Sistem"
            onClick={() => {
              setShowSettings(true);
              setShowNotifications(false);
            }}
          >
            <Settings size={16} />
          </button>

          <div style={{ position: "relative" }}>
            <button
              type="button"
              className="icon-action-bubble"
              title="Notifikasi"
              onClick={() => {
                setShowNotifications(!showNotifications);
                setShowSettings(false);
              }}
            >
              <Bell size={16} />
              {unreadCount > 0 && <span className="notif-badge-bubble">{unreadCount}</span>}
            </button>
          </div>

          <div className="user-portrait-circle" style={{ width: 34, height: 34, fontSize: "0.82rem" }}>
            {currentUser?.fullName?.charAt(0) || "U"}
          </div>
        </div>
      </header>

      {/* ===================================================================== */}
      {/* 1. LEFT SIDEBAR                                                       */}
      {/* ===================================================================== */}
      <aside className="hireism-sidebar no-print">
        {/* Brand Header */}
        <div className="hireism-brand-box">
          <div className="brand-badge-circle">
            <img src="/logo-iss.png" alt="Logo ISS Indonesia" />
          </div>
          <div className="brand-text">
            <h2>ISS Prodia</h2>
            <span>SPK MOORA</span>
          </div>
        </div>

        {/* Nav Items */}
        <nav className="hireism-nav-list">
          {/* Dashboard: Semua Role */}
          <button
            className={`hireism-nav-btn ${activeMenu === "dashboard" ? "active" : ""}`}
            onClick={() => setActiveMenu("dashboard")}
          >
            <LayoutDashboard size={18} />
            <span>Dashboard</span>
          </button>

          {/* Kalkulasi MOORA: Semua Role (Transparansi / Matrix Audit) */}
          <button
            className={`hireism-nav-btn ${activeMenu === "moora" ? "active" : ""}`}
            onClick={() => setActiveMenu("moora")}
          >
            <Calculator size={18} />
            <span>Kalkulasi MOORA</span>
          </button>

          {/* Input Nilai: Supervisor (Utama) & Admin */}
          {(isSupervisor || isAdmin) && (
            <button
              className={`hireism-nav-btn ${activeMenu === "assessment" ? "active" : ""}`}
              onClick={() => setActiveMenu("assessment")}
            >
              <ClipboardCheck size={18} />
              <span>Input Nilai</span>
              {isSupervisor && <span className="nav-role-badge">SPV</span>}
            </button>
          )}

          {/* Master Karyawan: Super Admin Only */}
          {isAdmin && (
            <button
              className={`hireism-nav-btn ${activeMenu === "employees" ? "active" : ""}`}
              onClick={() => setActiveMenu("employees")}
            >
              <Users size={18} />
              <span>Master Karyawan</span>
              <span className="nav-role-badge admin">HR</span>
            </button>
          )}

          {/* Kriteria & Bobot: Semua Role (Super Admin HR, Supervisor & Manager Read-Only) */}
          <button
            className={`hireism-nav-btn ${activeMenu === "criteria" ? "active" : ""}`}
            onClick={() => setActiveMenu("criteria")}
          >
            <Scale size={18} />
            <span>Kriteria & Bobot</span>
            {isAdmin ? (
              <span className="nav-role-badge admin">HR</span>
            ) : (
              <span className="nav-role-badge">Lihat</span>
            )}
          </button>

          {/* Laporan & SK: Semua Role (Khusus Manager ada label Approval) */}
          <button
            className={`hireism-nav-btn ${activeMenu === "reports" ? "active" : ""}`}
            onClick={() => setActiveMenu("reports")}
          >
            <FileText size={18} />
            <span>Laporan & SK</span>
            {isManager && <span className="nav-role-badge manager">Approval</span>}
          </button>
        </nav>

        {/* Logout Footer */}
        <div className="hireism-sidebar-footer">
          <button onClick={handleLogout} className="hireism-logout-btn">
            <LogOut size={16} />
            <span>Logout</span>
          </button>
        </div>
      </aside>

      {/* ===================================================================== */}
      {/* 2. MIDDLE CONTENT COLUMN                                              */}
      {/* ===================================================================== */}
      <main className="hireism-main-col">
        {/* Top Search & Action Bar */}
        <div className="hireism-top-toolbar no-print">
          <div className="hireism-search-pill">
            <Search size={16} color="#8c9bb0" />
            <input
              type="text"
              placeholder="Cari karyawan, NIP, atau indikator..."
              value={searchKeyword}
              onChange={(e) => setSearchKeyword(e.target.value)}
            />
          </div>

          <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
            <button
              onClick={() => runMooraCalculation(false)}
              disabled={calculating}
              className="hireism-btn-primary"
            >
              <RefreshCw size={15} className={calculating ? "animate-spin" : ""} />
              <span>{calculating ? "Menghitung..." : "Sinkronkan MOORA"}</span>
            </button>

            {/* Desktop User actions when right panel is hidden */}
            {activeMenu !== "dashboard" && (
              <div className="desktop-toolbar-user-strip" style={{ display: "flex", alignItems: "center", gap: "8px", marginLeft: "8px" }}>
                <button
                  type="button"
                  className="icon-action-bubble"
                  title="Pengaturan Sistem & MOORA"
                  onClick={() => {
                    setShowSettings(true);
                    setShowNotifications(false);
                  }}
                  aria-label="Pengaturan"
                >
                  <Settings size={16} />
                </button>

                <div style={{ position: "relative" }}>
                  <button
                    type="button"
                    className="icon-action-bubble"
                    title="Pusat Notifikasi"
                    onClick={() => {
                      setShowNotifications(!showNotifications);
                      setShowSettings(false);
                    }}
                    aria-label="Notifikasi"
                  >
                    <Bell size={16} />
                    {unreadCount > 0 && <span className="notif-badge-bubble">{unreadCount}</span>}
                  </button>
                </div>

                <div className="user-portrait-circle" style={{ width: 34, height: 34, fontSize: "0.82rem" }}>
                  {currentUser?.fullName?.charAt(0) || "U"}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Hero Welcome Banner (Reference Image "Good Morning Sara" Style) */}
        <div className="hireism-hero-banner no-print">
          <div className="hero-banner-content">
            <h2>Selamat Pagi, {currentUser?.fullName?.split(" ")[0]}!</h2>
            <p>
              Sistem evaluasi kinerja outsourcing PT ISS Indonesia di Laboratorium Klinik Prodia Kebayoran siap ditinjau.
            </p>
            <button
              className="hero-action-pill"
              onClick={() => setActiveMenu(activeMenu === "moora" ? "dashboard" : "moora")}
            >
              <Sparkles size={14} color="#3b5bfd" />
              <span>{activeMenu === "moora" ? "Kembali ke Dashboard" : "Audit Rumus MOORA"}</span>
            </button>
          </div>

          <div className="hero-banner-art">
            <div className="hero-art-glow">
              <Award size={64} color="#ffffff" style={{ filter: "drop-shadow(0 4px 12px rgba(0,0,0,0.15))" }} />
            </div>
          </div>
        </div>

        {/* =================================================================== */}
        {/* VIEW 1: DASHBOARD                                                   */}
        {/* =================================================================== */}
        {activeMenu === "dashboard" && (
          <div>
            {/* "You Need to hire" Metric Cards Section in Reference */}
            <div className="hireism-section-head no-print">
              <h3>Kategori Penilaian & Ringkasan</h3>
              <button
                className="hireism-pill-link"
                onClick={() =>
                  setSelectedDivision(
                    selectedDivision === "CLEANING_SERVICE" ? "MESSENGER" : "CLEANING_SERVICE"
                  )
                }
              >
                Ganti Kategori ({selectedDivision === "CLEANING_SERVICE" ? "CS Aktif" : "Messenger Aktif"})
              </button>
            </div>

            <div className="hireism-category-grid no-print">
              {/* Card 1: Cleaning Service */}
              <div
                className={`hireism-category-card ${selectedDivision === "CLEANING_SERVICE" ? "selected" : ""}`}
                onClick={() => setSelectedDivision("CLEANING_SERVICE")}
              >
                <div className="category-icon-bubble blue">
                  <Sparkles size={22} />
                </div>
                <div className="category-card-name">Cleaning Service</div>
                <div className="category-card-count">
                  ({employees.filter((e) => e.division === "CLEANING_SERVICE").length} Personel)
                </div>
              </div>

              {/* Card 2: Messenger */}
              <div
                className={`hireism-category-card ${selectedDivision === "MESSENGER" ? "selected" : ""}`}
                onClick={() => setSelectedDivision("MESSENGER")}
              >
                <div className="category-icon-bubble orange">
                  <Users size={22} />
                </div>
                <div className="category-card-name">Messenger Lab</div>
                <div className="category-card-count">
                  ({employees.filter((e) => e.division === "MESSENGER").length} Personel)
                </div>
              </div>

              {/* Card 3: Kriteria */}
              <div className="hireism-category-card" onClick={() => setActiveMenu("criteria")}>
                <div className="category-icon-bubble pink">
                  <Scale size={22} />
                </div>
                <div className="category-card-name">Kriteria Evaluasi</div>
                <div className="category-card-count">({filteredCriteria.length} Indikator)</div>
              </div>

              {/* Card 4: Periode */}
              <div className="hireism-category-card">
                <div className="category-icon-bubble teal">
                  <Calendar size={22} />
                </div>
                <div className="category-card-name">Periode Aktif</div>
                <div className="category-card-count">{currentPeriod?.periodName}</div>
              </div>

              {/* Card 5: Juara 1 */}
              <div className="hireism-category-card" onClick={() => setActiveMenu("moora")}>
                <div className="category-icon-bubble purple">
                  <Award size={22} />
                </div>
                <div className="category-card-name">Skor Yi Tertinggi</div>
                <div className="category-card-count" style={{ fontFamily: "var(--font-mono)", fontWeight: 700 }}>
                  {top1 ? top1.yScore.toFixed(4) : "0.0000"}
                </div>
              </div>
            </div>

            {/* "Recruitment Progress" Main Table in Reference with Signature Blue Row */}
            <div className="hireism-section-head">
              <h3>
                Klasemen Kinerja ({selectedDivision === "CLEANING_SERVICE" ? "Cleaning Service" : "Messenger"})
              </h3>
              <button className="hireism-pill-link" onClick={() => setActiveMenu("moora")}>
                Lihat Audit MOORA
              </button>
            </div>

            <div className="hireism-table-card" style={{ borderRadius: "12px", overflowX: "auto", WebkitOverflowScrolling: "touch", padding: 0 }}>
              <table className="hireism-table" style={{ width: "100%", minWidth: "560px", borderCollapse: "collapse", borderSpacing: 0, borderRadius: 0 }}>
                <thead>
                  <tr style={{ borderRadius: 0 }}>
                    <th style={{ borderRadius: 0 }}>NAMA PERSONEL</th>
                    <th style={{ borderRadius: 0 }}>JABATAN / DIVISI</th>
                    <th style={{ borderRadius: 0 }}>STATUS / PERINGKAT</th>
                    <th style={{ textAlign: "right", borderRadius: 0 }}>NILAI OPTIMASI (YI)</th>
                    <th style={{ textAlign: "center", width: "40px", borderRadius: 0 }}></th>
                  </tr>
                </thead>
                <tbody>
                  {filteredResults.length === 0 ? (
                    <tr>
                      <td colSpan={5} style={{ textAlign: "center", padding: "30px", color: "#8c9bb0", borderRadius: 0 }}>
                        Belum ada data nilai. Silakan klik tombol "Sinkronkan MOORA".
                      </td>
                    </tr>
                  ) : (
                    filteredResults.map((r) => {
                      const isChampion = r.rankPosition === 1;
                      return (
                        <tr key={r.id} className={isChampion ? "row-highlight" : ""} style={{ borderRadius: 0 }}>
                          <td style={{ borderRadius: 0 }}>
                            <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
                              <div
                                className="table-employee-avatar"
                                style={{
                                  width: "36px",
                                  height: "36px",
                                  minWidth: "36px",
                                  maxWidth: "36px",
                                  minHeight: "36px",
                                  maxHeight: "36px",
                                  flexShrink: 0,
                                  aspectRatio: "1 / 1",
                                  borderRadius: "50%",
                                  background: getCandidateAvatarGradient(r, r.rankPosition - 1),
                                  color: "#ffffff",
                                  display: "flex",
                                  alignItems: "center",
                                  justifyContent: "center",
                                  fontWeight: 800,
                                  fontSize: "0.82rem",
                                  boxSizing: "border-box",
                                }}
                              >
                                {r.employee.fullName.charAt(0)}
                              </div>
                              <div>
                                <strong style={{ fontSize: "0.88rem", color: isChampion ? "#1d4ed8" : "var(--text-main)" }}>
                                  {r.employee.fullName}
                                </strong>
                                <div style={{ fontSize: "0.72rem", color: isChampion ? "#3b82f6" : "#64748b" }}>
                                  <code>{r.employee.nip}</code> - {r.employee.placementUnit}
                                </div>
                              </div>
                            </div>
                          </td>

                          <td style={{ borderRadius: 0 }}>
                            <span style={{ fontWeight: isChampion ? 600 : 500, color: isChampion ? "#1e3a8a" : "inherit" }}>
                              {r.division === "CLEANING_SERVICE" ? "Cleaning Service" : "Messenger (Kurir Lab)"}
                            </span>
                          </td>

                          <td style={{ borderRadius: 0 }}>
                            <div className="status-dot-indicator">
                              {isChampion ? (
                                <span style={{
                                  display: "inline-flex",
                                  alignItems: "center",
                                  gap: "4px",
                                  padding: "3px 8px",
                                  borderRadius: "6px",
                                  background: "#dbeafe",
                                  color: "#1d4ed8",
                                  fontWeight: 800,
                                  fontSize: "0.76rem"
                                }}>
                                  ★ Karyawan Terbaik #1
                                </span>
                              ) : (
                                <>
                                  <span
                                    className={`dot-circle ${
                                      r.rankPosition === 2
                                        ? "dot-orange"
                                        : r.rankPosition === 3
                                        ? "dot-green"
                                        : "dot-blue"
                                    }`}
                                  ></span>
                                  <span>Peringkat #{r.rankPosition}</span>
                                </>
                              )}
                            </div>
                          </td>

                          <td style={{ textAlign: "right", fontFamily: "var(--font-mono)", fontWeight: 700, color: isChampion ? "#1d4ed8" : "inherit", borderRadius: 0 }}>
                            {r.yScore.toFixed(4)}
                          </td>

                          <td style={{ textAlign: "center", borderRadius: 0 }}>
                            <MoreVertical size={16} opacity={0.6} />
                          </td>
                        </tr>
                      );
                    })
                  )}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* =================================================================== */}
        {/* VIEW 2: KALKULASI MOORA (4 TABS AUDIT)                              */}
        {/* =================================================================== */}
        {activeMenu === "moora" && (
          <div className="hireism-form-card">
            <div className="hireism-section-head">
              <div>
                <h3>Transparansi 4 Tahap Komputasi MOORA</h3>
                <p style={{ fontSize: "0.82rem", color: "#8c9bb0", marginTop: "2px" }}>
                  Setiap matriks dihitung secara deterministik dan siap diaudit pada presentasi tugas akhir.
                </p>
              </div>
              <button
                className="hireism-btn-primary"
                onClick={() => runMooraCalculation(false)}
                disabled={calculating}
                style={{ padding: "8px 18px", fontSize: "0.82rem" }}
              >
                <RefreshCw size={14} className={calculating ? "animate-spin" : ""} />
                <span>{calculating ? "Menghitung..." : "Hitung Ulang"}</span>
              </button>
            </div>

            {/* Step Tabs Pill Bar */}
            <div className="hireism-tab-bar">
              <button
                className={`hireism-tab-pill ${mathStepTab === 1 ? "active" : ""}`}
                onClick={() => setMathStepTab(1)}
              >
                1. Matriks Keputusan (X)
              </button>
              <button
                className={`hireism-tab-pill ${mathStepTab === 2 ? "active" : ""}`}
                onClick={() => setMathStepTab(2)}
              >
                2. Normalisasi Rasio (R)
              </button>
              <button
                className={`hireism-tab-pill ${mathStepTab === 3 ? "active" : ""}`}
                onClick={() => setMathStepTab(3)}
              >
                3. Matriks Terbobot (V)
              </button>
              <button
                className={`hireism-tab-pill ${mathStepTab === 4 ? "active" : ""}`}
                onClick={() => setMathStepTab(4)}
              >
                4. Optimasi Nilai (Yi) & Peringkat
              </button>
            </div>

            {/* Tab 1: Matriks X */}
            {mathStepTab === 1 && (
              <div>
                <FormulaMatrixX />

                <div style={{ overflowX: "auto" }}>
                  <table className="hireism-table" style={{ width: "100%" }}>
                    <thead>
                      <tr>
                        <th>ALTERNATIF PERSONEL</th>
                        {filteredCriteria.map((c) => (
                          <th key={c.id} style={{ textAlign: "right" }}>
                            {c.code}: {c.name} ({(c.weight * 100).toFixed(0)}%)
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {mooraStepData?.decisionMatrix?.map((row: any) => (
                        <tr key={row.employee.id}>
                          <td><strong>{row.employee.fullName}</strong></td>
                          {filteredCriteria.map((c) => (
                            <td key={c.id} style={{ textAlign: "right", fontFamily: "var(--font-mono)" }}>
                              {row.scores[c.id]?.toFixed(2) || "0.00"}
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                    <tfoot>
                      <tr style={{ background: "#f1f5f9", fontWeight: 700 }}>
                        <td>
                          <MiniVectorDivisorBadge />
                        </td>
                        {filteredCriteria.map((c) => (
                          <td key={c.id} style={{ textAlign: "right", color: "#3b5bfd", fontFamily: "var(--font-mono)" }}>
                            {mooraStepData?.divisors?.[c.id]?.toFixed(4) || "0.0000"}
                          </td>
                        ))}
                      </tr>
                    </tfoot>
                  </table>
                </div>
              </div>
            )}

            {/* Tab 2: Matriks R */}
            {mathStepTab === 2 && (
              <div>
                <FormulaVectorNormalization />

                <div style={{ overflowX: "auto" }}>
                  <table className="hireism-table">
                    <thead>
                      <tr>
                        <th>ALTERNATIF PERSONEL</th>
                        {filteredCriteria.map((c) => (
                          <th key={c.id} style={{ textAlign: "right" }}>{c.code} ({c.type})</th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {mooraStepData?.normalizedMatrix?.map((row: any) => (
                        <tr key={row.employee.id}>
                          <td><strong>{row.employee.fullName}</strong></td>
                          {filteredCriteria.map((c) => (
                            <td key={c.id} style={{ textAlign: "right", fontFamily: "var(--font-mono)" }}>
                              {row.scores[c.id]?.toFixed(4) || "0.0000"}
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            )}

            {/* Tab 3: Matriks V */}
            {mathStepTab === 3 && (
              <div>
                <FormulaWeightedMatrix />

                <div style={{ overflowX: "auto" }}>
                  <table className="hireism-table">
                    <thead>
                      <tr>
                        <th>ALTERNATIF PERSONEL</th>
                        {filteredCriteria.map((c) => (
                          <th key={c.id} style={{ textAlign: "right" }}>{c.code} (W = {c.weight})</th>
                        ))}
                      </tr>
                    </thead>
                    <tbody>
                      {mooraStepData?.weightedMatrix?.map((row: any) => (
                        <tr key={row.employee.id}>
                          <td><strong>{row.employee.fullName}</strong></td>
                          {filteredCriteria.map((c) => (
                            <td key={c.id} style={{ textAlign: "right", fontFamily: "var(--font-mono)" }}>
                              {row.scores[c.id]?.toFixed(4) || "0.0000"}
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            )}

            {/* Tab 4: Nilai Akhir Yi */}
            {mathStepTab === 4 && (
              <div>
                <FormulaOptimizationYi />

                <div style={{ overflowX: "auto" }}>
                  <table className="hireism-table">
                    <thead>
                      <tr>
                        <th style={{ width: "90px" }}>PERINGKAT</th>
                        <th>NIP</th>
                        <th>NAMA PERSONEL</th>
                        <th style={{ textAlign: "right" }}>Σ BENEFIT (+)</th>
                        <th style={{ textAlign: "right" }}>Σ COST (-)</th>
                        <th style={{ textAlign: "right" }}>NILAI YI</th>
                      </tr>
                    </thead>
                    <tbody>
                      {mooraStepData?.rankingResults?.map((row: any) => {
                        const isWinner = row.rank === 1;
                        return (
                          <tr key={row.employee.id} className={isWinner ? "row-highlight" : ""}>
                            <td><strong>{isWinner ? "🏆 #1" : `#${row.rank}`}</strong></td>
                            <td><code>{row.employee.nip}</code></td>
                            <td><strong>{row.employee.fullName}</strong></td>
                            <td style={{ textAlign: "right", fontFamily: "var(--font-mono)", color: isWinner ? "#ffffff" : "#10b981" }}>
                              +{row.sumBenefit.toFixed(4)}
                            </td>
                            <td style={{ textAlign: "right", fontFamily: "var(--font-mono)", color: isWinner ? "#ffffff" : "#ef4444" }}>
                              -{row.sumCost.toFixed(4)}
                            </td>
                            <td style={{ textAlign: "right", fontFamily: "var(--font-mono)", fontWeight: 800 }}>
                              {row.yScore.toFixed(4)}
                            </td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              </div>
            )}
          </div>
        )}

        {/* =================================================================== */}
        {/* VIEW 3: INPUT NILAI PENILAIAN                                       */}
        {/* =================================================================== */}
        {activeMenu === "assessment" && (
          <div className="hireism-form-card">
            <div className="hireism-section-head">
              <div>
                <h3>Lembar Penilaian Karyawan</h3>
                <p style={{ fontSize: "0.82rem", color: "#8c9bb0", marginTop: "2px" }}>
                  Diisi oleh Supervisor ISS berdasarkan presensi harian dan kepatuhan SOP Prodia Kebayoran.
                </p>
              </div>
            </div>

            {!isSupervisor && (
              <div className="role-guard-banner">
                <ShieldAlert size={18} />
                <div>
                  <strong>Akses Peninjauan (Read-Only):</strong> Anda login sebagai <strong>{getRoleLabel(currentUser?.role)}</strong>. Berdasarkan pembagian wewenang sistem, pengisian nilai operasional lapangan hanya dapat dilakukan oleh <strong>Site Supervisor ISS Prodia (Septo Aribowo)</strong>.
                </div>
              </div>
            )}

            <form onSubmit={handleSaveAssessment}>
              <div style={{ maxWidth: "420px", marginBottom: "20px" }}>
                <label style={{ display: "block", fontSize: "0.84rem", fontWeight: 700, color: "#334155", marginBottom: "6px" }}>
                  Pilih Karyawan yang Dinilai:
                </label>
                <select
                  value={selectedEmployeeForEval}
                  onChange={(e) => setSelectedEmployeeForEval(e.target.value)}
                  style={{ width: "100%", padding: "10px 14px", borderRadius: "12px", border: "1px solid #e2e8f0", fontSize: "0.88rem", outline: "none" }}
                  required
                >
                  <option value="">-- Pilih Karyawan {selectedDivision === "CLEANING_SERVICE" ? "CS" : "Messenger"} --</option>
                  {filteredEmployees.map((emp) => (
                    <option key={emp.id} value={emp.id}>
                      {emp.nip} - {emp.fullName}
                    </option>
                  ))}
                </select>
              </div>

              {selectedEmployeeForEval && (
                <div>
                  <h4 style={{ fontSize: "0.95rem", fontWeight: 700, margin: "20px 0 14px", color: "#0f172a" }}>
                    Indikator Kriteria Evaluasi (Skala 1 - 100):
                  </h4>

                  <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))", gap: "16px" }}>
                    {filteredCriteria.map((c) => (
                      <div
                        key={c.id}
                        style={{
                          background: "#f8fafc",
                          border: "1px solid #e2e8f0",
                          borderRadius: "14px",
                          padding: "16px",
                        }}
                      >
                        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: "8px" }}>
                          <div>
                            <strong style={{ fontSize: "0.88rem", color: "#0f172a" }}>{c.code}: {c.name}</strong>
                            <div style={{ fontSize: "0.75rem", color: "#8c9bb0", marginTop: "2px" }}>{c.description}</div>
                          </div>
                          <span className="hireism-pill-link" style={c.type === "BENEFIT" ? { color: "#10b981", background: "#ecfdf5" } : { color: "#ef4444", background: "#fef2f2" }}>
                            {c.type}
                          </span>
                        </div>

                        <div style={{ display: "flex", alignItems: "center", gap: "12px", marginTop: "12px" }}>
                          <input
                            type="number"
                            min="0"
                            max="100"
                            disabled={!isSupervisor}
                            value={evalScores[c.id] ?? ""}
                            onChange={(e) => setEvalScores({ ...evalScores, [c.id]: Number(e.target.value) })}
                            style={{
                              width: "90px",
                              padding: "8px",
                              borderRadius: "10px",
                              border: "1px solid #cbd5e1",
                              textAlign: "center",
                              fontWeight: 700,
                              fontSize: "0.95rem",
                              background: !isSupervisor ? "#f1f5f9" : "#ffffff",
                              cursor: !isSupervisor ? "not-allowed" : "text",
                            }}
                            required
                          />
                          <span style={{ fontSize: "0.76rem", color: "#8c9bb0" }}>
                            {c.type === "COST" ? "Makin kecil makin bagus (komplain)" : "Makin besar makin bagus"}
                          </span>
                        </div>
                      </div>
                    ))}
                  </div>

                  <button
                    type="submit"
                    disabled={!isSupervisor || evalSaving}
                    className="hireism-btn-primary"
                    style={{
                      marginTop: "24px",
                      opacity: !isSupervisor ? 0.6 : 1,
                      cursor: !isSupervisor ? "not-allowed" : "pointer",
                    }}
                  >
                    <CheckCircle2 size={16} />
                    <span>
                      {!isSupervisor
                        ? "Akses Dibatasi (Wewenang Khusus Supervisor ISS)"
                        : evalSaving
                        ? "Menyimpan..."
                        : "Simpan & Hitung Ulang Ranking"}
                    </span>
                  </button>
                </div>
              )}
            </form>
          </div>
        )}

        {/* =================================================================== */}
        {/* VIEW 4: MASTER KARYAWAN                                            */}
        {/* =================================================================== */}
        {activeMenu === "employees" && (
          <div>
            {!isAdmin ? (
              <div className="role-guard-banner">
                <ShieldAlert size={18} />
                <div>
                  <strong>Hak Akses Dibatasi:</strong> Anda login sebagai <strong>{getRoleLabel(currentUser?.role)}</strong>. Pengelolaan dan penambahan data master personel merupakan wewenang eksklusif <strong>HRD ISS Pusat (Super Admin)</strong>.
                </div>
              </div>
            ) : (
              <div className="hireism-form-card" style={{ marginBottom: "20px" }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: "12px", marginBottom: showAddEmployeeForm ? "18px" : "0" }}>
                  <div>
                    <h3 style={{ fontSize: "1.05rem", fontWeight: 800, color: "#0f172a", margin: "0 0 4px" }}>
                      Master Data Personel
                    </h3>
                    <p style={{ fontSize: "0.82rem", color: "#64748b", margin: 0 }}>
                      Kelola data master seluruh personel outsourcing unit penempatan Laboratorium Klinik Prodia Kebayoran.
                    </p>
                  </div>

                  <button
                    type="button"
                    onClick={() => {
                      setShowAddEmployeeForm(!showAddEmployeeForm);
                      setNewDivision(selectedDivision);
                    }}
                    className="hireism-btn-primary"
                    style={{ fontSize: "0.82rem", padding: "8px 16px" }}
                  >
                    {showAddEmployeeForm ? <X size={15} /> : <Plus size={15} />}
                    <span>{showAddEmployeeForm ? "Tutup Form" : "Tambah Personel Baru"}</span>
                  </button>
                </div>

                {showAddEmployeeForm && (
                  <form onSubmit={handleAddEmployee} style={{ paddingTop: "18px", borderTop: "1px solid #e2e8f0" }}>
                    <div
                      style={{
                        display: "grid",
                        gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
                        gap: "14px",
                        marginBottom: "16px",
                      }}
                    >
                      <div>
                        <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "#334155", marginBottom: "6px" }}>
                          NIP:
                        </label>
                        <input
                          type="text"
                          placeholder={selectedDivision === "CLEANING_SERVICE" ? "CS-010" : "MSG-007"}
                          value={newNip}
                          onChange={(e) => setNewNip(e.target.value)}
                          style={{
                            width: "100%",
                            height: "44px",
                            padding: "0 14px",
                            borderRadius: "10px",
                            border: "1px solid #cbd5e1",
                            fontSize: "0.88rem",
                            boxSizing: "border-box",
                            backgroundColor: "#ffffff",
                            outline: "none",
                          }}
                          required
                        />
                      </div>

                      <div>
                        <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "#334155", marginBottom: "6px" }}>
                          Nama Lengkap:
                        </label>
                        <input
                          type="text"
                          placeholder="Nama Lengkap Personel"
                          value={newName}
                          onChange={(e) => setNewName(e.target.value)}
                          style={{
                            width: "100%",
                            height: "44px",
                            padding: "0 14px",
                            borderRadius: "10px",
                            border: "1px solid #cbd5e1",
                            fontSize: "0.88rem",
                            boxSizing: "border-box",
                            backgroundColor: "#ffffff",
                            outline: "none",
                          }}
                          required
                        />
                      </div>

                      <div>
                        <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "#334155", marginBottom: "6px" }}>
                          Divisi:
                        </label>
                        <select
                          value={newDivision}
                          onChange={(e) => setNewDivision(e.target.value as any)}
                          style={{
                            width: "100%",
                            height: "44px",
                            padding: "0 14px",
                            borderRadius: "10px",
                            border: "1px solid #cbd5e1",
                            fontSize: "0.88rem",
                            boxSizing: "border-box",
                            backgroundColor: "#ffffff",
                            outline: "none",
                            cursor: "pointer",
                          }}
                        >
                          <option value="CLEANING_SERVICE">Cleaning Service</option>
                          <option value="MESSENGER">Messenger Lab</option>
                        </select>
                      </div>
                    </div>

                    <div style={{ display: "flex", justifyContent: "flex-end", gap: "10px" }}>
                      <button
                        type="button"
                        onClick={() => setShowAddEmployeeForm(false)}
                        style={{
                          padding: "9px 18px",
                          borderRadius: "10px",
                          border: "1px solid #cbd5e1",
                          background: "#f8fafc",
                          color: "#475569",
                          fontWeight: 600,
                          fontSize: "0.85rem",
                          cursor: "pointer",
                        }}
                      >
                        Batal
                      </button>
                      <button
                        type="submit"
                        className="hireism-btn-primary"
                        style={{
                          height: "42px",
                          padding: "0 22px",
                          borderRadius: "10px",
                          fontSize: "0.85rem",
                          display: "flex",
                          alignItems: "center",
                          gap: "6px",
                          whiteSpace: "nowrap",
                        }}
                      >
                        <Plus size={16} />
                        <span>Simpan Personel</span>
                      </button>
                    </div>
                  </form>
                )}
              </div>
            )}

            {/* Switcher Tab Kategori Divisi: Cleaning Service & Messenger */}
            <div className="hireism-tab-bar" style={{ marginBottom: "18px" }}>
              <button
                type="button"
                className={`hireism-tab-pill ${selectedDivision === "CLEANING_SERVICE" ? "active" : ""}`}
                onClick={() => setSelectedDivision("CLEANING_SERVICE")}
                style={{ display: "flex", alignItems: "center", gap: "8px", padding: "10px 20px", fontSize: "0.85rem" }}
              >
                <Sparkles size={16} />
                <span>Cleaning Service ({employees.filter((e) => e.division === "CLEANING_SERVICE").length} Personel)</span>
              </button>
              <button
                type="button"
                className={`hireism-tab-pill ${selectedDivision === "MESSENGER" ? "active" : ""}`}
                onClick={() => setSelectedDivision("MESSENGER")}
                style={{ display: "flex", alignItems: "center", gap: "8px", padding: "10px 20px", fontSize: "0.85rem" }}
              >
                <Users size={16} />
                <span>Messenger Lab ({employees.filter((e) => e.division === "MESSENGER").length} Personel)</span>
              </button>
            </div>

            <div className="hireism-table-card">
              <div className="hireism-section-head" style={{ padding: "18px 24px", borderBottom: "1px solid #e2e8f0" }}>
                <div>
                  <h3 style={{ fontSize: "1.05rem", fontWeight: 800, color: "#0f172a", margin: 0 }}>
                    Daftar Personel ({selectedDivision === "CLEANING_SERVICE" ? "Cleaning Service" : "Messenger Lab"})
                  </h3>
                  <p style={{ fontSize: "0.82rem", color: "#64748b", margin: "4px 0 0" }}>
                    Total {filteredEmployees.length} personel terdaftar aktif pada kategori ini
                  </p>
                </div>
              </div>

              <table className="hireism-table">
                <thead>
                  <tr>
                    <th style={{ width: "140px" }}>NIP</th>
                    <th>NAMA PERSONEL</th>
                    <th style={{ width: "190px" }}>DIVISI</th>
                    <th style={{ width: "210px" }}>PENEMPATAN</th>
                    {isAdmin && <th style={{ textAlign: "center", width: "100px" }}>AKSI</th>}
                  </tr>
                </thead>
                <tbody>
                  {filteredEmployees.map((emp) => (
                    <tr key={emp.id}>
                      <td>
                        <span
                          style={{
                            fontFamily: "var(--font-mono)",
                            fontWeight: 700,
                            padding: "4px 10px",
                            borderRadius: "6px",
                            background: "#f1f5f9",
                            color: "#334155",
                            fontSize: "0.82rem",
                            border: "1px solid #e2e8f0",
                            display: "inline-block",
                          }}
                        >
                          {emp.nip}
                        </span>
                      </td>
                      <td>
                        <strong style={{ color: "#0f172a", fontSize: "0.9rem" }}>{emp.fullName}</strong>
                      </td>
                      <td>
                        <span
                          className="hireism-pill-link"
                          style={
                            emp.division === "CLEANING_SERVICE"
                              ? { color: "#2563eb", background: "#eff6ff", border: "1px solid #bfdbfe", padding: "4px 10px", fontWeight: 700 }
                              : { color: "#7c3aed", background: "#f5f3ff", border: "1px solid #ddd6fe", padding: "4px 10px", fontWeight: 700 }
                          }
                        >
                          {emp.division === "CLEANING_SERVICE" ? "Cleaning Service" : "Messenger Lab"}
                        </span>
                      </td>
                      <td>
                        <span style={{ color: "#475569", fontSize: "0.85rem", fontWeight: 500 }}>
                          {emp.placementUnit}
                        </span>
                      </td>
                      {isAdmin && (
                        <td style={{ textAlign: "center" }}>
                          <button
                            type="button"
                            onClick={() => handleDeleteEmployee(emp.id, emp.fullName)}
                            style={{
                              padding: "6px 10px",
                              background: "#fef2f2",
                              color: "#ef4444",
                              border: "1px solid #fecaca",
                              borderRadius: "8px",
                              cursor: "pointer",
                              display: "inline-flex",
                              alignItems: "center",
                              justifyContent: "center",
                              transition: "all 0.15s ease",
                            }}
                            title="Hapus Personel"
                          >
                            <Trash2 size={14} />
                          </button>
                        </td>
                      )}
                    </tr>
                  ))}
                  {filteredEmployees.length === 0 && (
                    <tr>
                      <td colSpan={isAdmin ? 5 : 4} style={{ textAlign: "center", padding: "36px", color: "#94a3b8" }}>
                        Tidak ada data personel pada kategori {selectedDivision === "CLEANING_SERVICE" ? "Cleaning Service" : "Messenger Lab"}.
                      </td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* =================================================================== */}
        {/* VIEW 5: KRITERIA & BOBOT                                           */}
        {/* =================================================================== */}
        {activeMenu === "criteria" && (
          <div>
            {!isAdmin ? (
              <div className="role-guard-banner">
                <ShieldAlert size={18} />
                <div>
                  <strong>Mode Peninjauan (Read-Only):</strong> Anda login sebagai <strong>{getRoleLabel(currentUser?.role)}</strong>. Berdasarkan kebijakan tata kelola SPK, penyesuaian bobot kriteria dan sifat Benefit/Cost hanya dapat diubah oleh <strong>Super Admin (HRD ISS Pusat)</strong>.
                </div>
              </div>
            ) : (
              <div className="hireism-form-card" style={{ marginBottom: "20px" }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: "10px" }}>
                  <div>
                    <h3 style={{ fontSize: "1.05rem", fontWeight: 800, color: "#0f172a", margin: 0 }}>
                      Kelola Kriteria &amp; Pembobotan ({selectedDivision === "CLEANING_SERVICE" ? "Cleaning Service" : "Messenger"})
                    </h3>
                    <p style={{ fontSize: "0.82rem", color: "#64748b", margin: "4px 0 0" }}>
                      Tambah indikator kriteria baru atau sesuaikan bobot preferensi penentu ranking MOORA.
                    </p>
                  </div>
                  <button
                    type="button"
                    onClick={() => setShowAddCriteriaForm(!showAddCriteriaForm)}
                    className="hireism-btn-primary"
                    style={{ fontSize: "0.82rem", padding: "8px 16px" }}
                  >
                    {showAddCriteriaForm ? <X size={15} /> : <Plus size={15} />}
                    <span>{showAddCriteriaForm ? "Tutup Form" : "Tambah Kriteria Baru"}</span>
                  </button>
                </div>

                {showAddCriteriaForm && (
                  <form onSubmit={handleAddCriteria} style={{ marginTop: "16px", paddingTop: "16px", borderTop: "1px solid #e2e8f0" }}>
                    <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(180px, 1fr))", gap: "12px", marginBottom: "12px" }}>
                      <div>
                        <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "#334155", marginBottom: "4px" }}>
                          Kode Kriteria:
                        </label>
                        <input
                          type="text"
                          placeholder={`C${filteredCriteria.length + 1}`}
                          value={newCritCode}
                          onChange={(e) => setNewCritCode(e.target.value)}
                          style={{ width: "100%", padding: "10px 14px", borderRadius: "12px", border: "1px solid #e2e8f0" }}
                        />
                        <span style={{ fontSize: "0.72rem", color: "#94a3b8" }}>Kosongkan untuk otomatis C{filteredCriteria.length + 1}</span>
                      </div>

                      <div style={{ gridColumn: "span 2" }}>
                        <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "#334155", marginBottom: "4px" }}>
                          Nama Indikator Kriteria:
                        </label>
                        <input
                          type="text"
                          placeholder="Contoh: Ketelitian Pemeriksaan / Penanganan Sampel"
                          value={newCritName}
                          onChange={(e) => setNewCritName(e.target.value)}
                          style={{ width: "100%", padding: "10px 14px", borderRadius: "12px", border: "1px solid #e2e8f0" }}
                          required
                        />
                      </div>

                      <div>
                        <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "#334155", marginBottom: "4px" }}>
                          Sifat Kriteria:
                        </label>
                        <select
                          value={newCritType}
                          onChange={(e) => setNewCritType(e.target.value as any)}
                          style={{ width: "100%", padding: "10px 14px", borderRadius: "12px", border: "1px solid #e2e8f0" }}
                        >
                          <option value="BENEFIT">BENEFIT (Semakin besar semakin baik)</option>
                          <option value="COST">COST (Semakin kecil semakin baik)</option>
                        </select>
                      </div>

                      <div>
                        <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "#334155", marginBottom: "4px" }}>
                          Bobot W (Contoh: 0.20 = 20%):
                        </label>
                        <input
                          type="number"
                          step="0.01"
                          min="0.01"
                          max="1.00"
                          placeholder="0.20"
                          value={newCritWeight}
                          onChange={(e) => setNewCritWeight(e.target.value)}
                          style={{ width: "100%", padding: "10px 14px", borderRadius: "12px", border: "1px solid #e2e8f0" }}
                          required
                        />
                      </div>
                    </div>

                    <div style={{ marginBottom: "16px" }}>
                      <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "#334155", marginBottom: "4px" }}>
                        Deskripsi Standar Operasional / Checklist:
                      </label>
                      <input
                        type="text"
                        placeholder="Uraian indikator penilaian checklist di unit Prodia Kebayoran"
                        value={newCritDesc}
                        onChange={(e) => setNewCritDesc(e.target.value)}
                        style={{ width: "100%", padding: "10px 14px", borderRadius: "12px", border: "1px solid #e2e8f0" }}
                      />
                    </div>

                    <div style={{ display: "flex", justifyContent: "flex-end", gap: "10px" }}>
                      <button
                        type="button"
                        onClick={() => setShowAddCriteriaForm(false)}
                        style={{ padding: "8px 16px", borderRadius: "10px", border: "1px solid #cbd5e1", background: "#f8fafc", color: "#475569", fontWeight: 600, cursor: "pointer" }}
                      >
                        Batal
                      </button>
                      <button
                        type="submit"
                        disabled={critSaving}
                        className="hireism-btn-primary"
                        style={{ padding: "8px 20px" }}
                      >
                        <Plus size={15} />
                        <span>{critSaving ? "Menyimpan..." : "Simpan Kriteria Baru"}</span>
                      </button>
                    </div>
                  </form>
                )}
              </div>
            )}

            <div className="hireism-table-card">
              <div className="hireism-section-head">
                <div>
                  <h3>Kriteria &amp; Pembobotan ({selectedDivision === "CLEANING_SERVICE" ? "Cleaning Service" : "Messenger"})</h3>
                  <p style={{ fontSize: "0.82rem", color: "#8c9bb0" }}>Total bobot seluruh kriteria wajib 1.00 (100%) agar kalkulasi MOORA deterministik.</p>
                </div>
              </div>

              <table className="hireism-table">
                <thead>
                  <tr>
                    <th>KODE</th>
                    <th>NAMA KRITERIA</th>
                    <th>SIFAT</th>
                    <th style={{ textAlign: "right" }}>BOBOT (W)</th>
                    <th style={{ textAlign: "right" }}>PERSENTASE</th>
                    <th>DESKRIPSI STANDAR</th>
                    {isAdmin && <th style={{ textAlign: "center", width: "130px" }}>AKSI</th>}
                  </tr>
                </thead>
                <tbody>
                  {filteredCriteria.map((c) => (
                    <tr key={c.id}>
                      <td><strong>{c.code}</strong></td>
                      <td><strong>{c.name}</strong></td>
                      <td>
                        <span className="hireism-pill-link" style={c.type === "BENEFIT" ? { color: "#10b981", background: "#ecfdf5" } : { color: "#ef4444", background: "#fef2f2" }}>
                          {c.type}
                        </span>
                      </td>
                      <td style={{ textAlign: "right", fontFamily: "var(--font-mono)" }}>{c.weight.toFixed(2)}</td>
                      <td style={{ textAlign: "right", fontWeight: 700, color: "#3b5bfd" }}>{(c.weight * 100).toFixed(0)}%</td>
                      <td style={{ fontSize: "0.82rem", color: "#64748b" }}>{c.description}</td>
                      {isAdmin && (
                        <td style={{ textAlign: "center" }}>
                          <div style={{ display: "flex", gap: "6px", justifyContent: "center" }}>
                            <button
                              type="button"
                              onClick={() => openEditCriteriaModal(c)}
                              style={{
                                padding: "6px 10px",
                                background: "#eff6ff",
                                color: "#2563eb",
                                border: "1px solid #bfdbfe",
                                borderRadius: "8px",
                                cursor: "pointer",
                                display: "flex",
                                alignItems: "center",
                                gap: "4px",
                                fontSize: "0.75rem",
                                fontWeight: 600,
                              }}
                              title="Edit Kriteria & Bobot"
                            >
                              <Edit3 size={13} />
                              <span>Edit</span>
                            </button>
                            <button
                              type="button"
                              onClick={() => handleDeleteCriteria(c.id, c.code, c.name)}
                              style={{
                                padding: "6px 8px",
                                background: "#fef2f2",
                                color: "#ef4444",
                                border: "1px solid #fecaca",
                                borderRadius: "8px",
                                cursor: "pointer",
                                display: "flex",
                                alignItems: "center",
                                gap: "4px",
                                fontSize: "0.75rem",
                                fontWeight: 600,
                              }}
                              title="Hapus Kriteria"
                            >
                              <Trash2 size={13} />
                            </button>
                          </div>
                        </td>
                      )}
                    </tr>
                  ))}
                </tbody>
                <tfoot style={{ borderTop: "2px solid #cbd5e1" }}>
                  {(() => {
                    const totalWeight = filteredCriteria.reduce((sum, c) => sum + c.weight, 0);
                    const isValidWeight = Math.abs(totalWeight - 1.0) < 0.001;
                    return (
                      <tr style={{ background: "#f8fafc", fontWeight: 800 }}>
                        <td colSpan={3} style={{ padding: "16px 20px", color: "#1e293b", fontSize: "0.85rem", letterSpacing: "0.5px" }}>
                          TOTAL AKUMULASI BOBOT:
                        </td>
                        <td style={{ textAlign: "right", padding: "16px 18px", color: isValidWeight ? "#059669" : "#d97706", fontFamily: "var(--font-mono)", fontSize: "0.95rem" }}>
                          {totalWeight.toFixed(2)}
                        </td>
                        <td style={{ textAlign: "right", padding: "16px 18px", color: isValidWeight ? "#059669" : "#d97706", fontSize: "0.95rem" }}>
                          {(totalWeight * 100).toFixed(0)}%
                        </td>
                        <td style={{ padding: "16px 20px" }}>
                          <div
                            style={{
                              display: "inline-flex",
                              alignItems: "center",
                              gap: "6px",
                              padding: "5px 12px",
                              borderRadius: "20px",
                              background: isValidWeight ? "#ecfdf5" : "#fef2f2",
                              color: isValidWeight ? "#059669" : "#dc2626",
                              border: `1px solid ${isValidWeight ? "#a7f3d0" : "#fecaca"}`,
                              fontSize: "0.78rem",
                              fontWeight: 700,
                            }}
                          >
                            {isValidWeight ? (
                              <>
                                <CheckCircle2 size={14} style={{ color: "#059669" }} />
                                <span>Valid (Total Bobot Sesuai 1.00 / 100%)</span>
                              </>
                            ) : (
                              <>
                                <AlertCircle size={14} style={{ color: "#dc2626" }} />
                                <span>Total Bobot {(totalWeight * 100).toFixed(1)}% (Wajib Tepat 100%)</span>
                              </>
                            )}
                          </div>
                        </td>
                        {isAdmin && (
                          <td style={{ textAlign: "center", padding: "16px", color: "#94a3b8" }}>
                            &mdash;
                          </td>
                        )}
                      </tr>
                    );
                  })()}
                </tfoot>
              </table>
            </div>
          </div>
        )}

        {/* =================================================================== */}
        {/* VIEW 6: LAPORAN & CETAK SK RESMI                                   */}
        {/* =================================================================== */}
        {activeMenu === "reports" && (
          <div>
            {/* Approval Banner Interaktif (Wewenang Khusus Branch Manager Prodia) */}
            <div className={`approval-action-card ${skApproved ? "approved" : "pending"} no-print`}>
              <div>
                <div style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "4px" }}>
                  <span className={`role-pill-badge ${skApproved ? "manager" : "supervisor"}`}>
                    {skApproved ? "STATUS: TELAH DISAHKAN" : "STATUS: MENUNGGU PENGESAHAN"}
                  </span>
                  <span style={{ fontSize: "0.82rem", fontWeight: 700, color: "#475569" }}>
                    SK Rekomendasi Insentif Kuartal III 2026
                  </span>
                </div>
                <p style={{ margin: 0, fontSize: "0.84rem", color: "#64748b" }}>
                  {skApproved
                    ? "Dokumen Berita Acara & SK telah divalidasi dan disahkan oleh Siska Darmayanti (Branch Manager Prodia). Siap dicairkan."
                    : "Hasil pemeringkatan MOORA memerlukan verifikasi dan persetujuan resmi dari Pimpinan Mitra Klien (Branch Manager Prodia)."}
                </p>
              </div>

              <div style={{ display: "flex", alignItems: "center", gap: "10px", flexWrap: "wrap" }}>
                {isManager ? (
                  !skApproved ? (
                    <button
                      type="button"
                      onClick={() => {
                        setSkApproved(true);
                        showToast("SK Penetapan Insentif berhasil disahkan & ditandatangani digital oleh Siska Darmayanti!", "success");
                      }}
                      className="hireism-btn-primary"
                      style={{ background: "#059669", borderColor: "#047857" }}
                    >
                      <CheckCircle2 size={16} />
                      <span>Sahkan &amp; Tandatangani SK Resmi</span>
                    </button>
                  ) : (
                    <button
                      type="button"
                      onClick={() => {
                        setSkApproved(false);
                        showToast("Status pengesahan SK dibatalkan untuk peninjauan kembali.", "error");
                      }}
                      style={{
                        padding: "8px 14px",
                        borderRadius: "10px",
                        border: "1px solid #fecaca",
                        background: "#fef2f2",
                        color: "#dc2626",
                        fontWeight: 700,
                        fontSize: "0.82rem",
                        cursor: "pointer",
                      }}
                    >
                      Batalkan Pengesahan (Revisi)
                    </button>
                  )
                ) : (
                  <div style={{ fontSize: "0.82rem", color: "#64748b", background: "#ffffff", padding: "8px 14px", borderRadius: "10px", border: "1px solid #e2e8f0" }}>
                    {skApproved ? (
                      <span style={{ color: "#059669", fontWeight: 700 }}>✓ Telah Disahkan Siska Darmayanti</span>
                    ) : (
                      <span>⏳ Menunggu Persetujuan Branch Manager Prodia</span>
                    )}
                  </div>
                )}

                <button
                  className="hireism-btn-primary"
                  onClick={() => window.print()}
                >
                  <Printer size={16} /> Cetak SK (PDF)
                </button>
              </div>
            </div>

            <div style={{ background: "#ffffff", padding: "40px", borderRadius: "20px", border: "1px solid #e2e8f0" }}>
              <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", borderBottom: "3px double #0f172a", paddingBottom: "18px", marginBottom: "24px" }}>
                <div style={{ display: "flex", alignItems: "center", gap: "18px" }}>
                  <img src="/logo-iss.png" alt="Logo ISS Indonesia" style={{ width: "65px", height: "65px", objectFit: "contain" }} />
                  <div>
                    <h2 style={{ fontSize: "1.3rem", fontWeight: 800, color: "#0f172a" }}>PT ISS INDONESIA - FACILITY SERVICES</h2>
                    <h4 style={{ fontSize: "0.92rem", fontWeight: 600, color: "#3b5bfd" }}>UNIT PENEMPATAN LABORATORIUM KLINIK PRODIA KEBAYORAN</h4>
                    <p style={{ fontSize: "0.78rem", color: "#64748b" }}>Jl. Kyai Maja No. 39, Kebayoran Baru, Jakarta Selatan - DKI Jakarta</p>
                  </div>
                </div>
                <div style={{ textAlign: "right", fontSize: "0.8rem", color: "#475569" }}>
                  <strong>NO:</strong> ISS-PRD/SPK-MOORA/{new Date().getFullYear()}/08<br />
                  <strong>TANGGAL:</strong> {new Date().toLocaleDateString("id-ID", { dateStyle: "long" })}
                </div>
              </div>

              <div style={{ textAlign: "center", marginBottom: "24px" }}>
                <h3 style={{ fontSize: "1.15rem", fontWeight: 800, textTransform: "uppercase" }}>
                  BERITA ACARA PENETAPAN KARYAWAN OUTSOURCING TERBAIK
                </h3>
                <p style={{ fontSize: "0.88rem", color: "#475569", marginTop: "4px" }}>
                  Kategori: <strong>{selectedDivision === "CLEANING_SERVICE" ? "CLEANING SERVICE" : "MESSENGER (KURIR LAB)"}</strong> - Periode: {currentPeriod?.periodName}
                </p>
              </div>

              {top1 && (
                <div style={{ border: "2px solid #3b5bfd", background: "#f0f4ff", borderRadius: "14px", padding: "18px", marginBottom: "26px", textAlign: "center" }}>
                  <div style={{ fontSize: "0.85rem", fontWeight: 700, color: "#3b5bfd", textTransform: "uppercase" }}>
                    ★ PREDIKAT KARYAWAN TERBAIK #1 ★
                  </div>
                  <div style={{ fontSize: "1.4rem", fontWeight: 800, color: "#0f172a", marginTop: "4px" }}>
                    {top1.employee.fullName}
                  </div>
                  <div style={{ fontSize: "0.85rem", color: "#475569" }}>
                    NIP: <strong>{top1.employee.nip}</strong> | Skor Optimasi (Yi): <strong>{top1.yScore.toFixed(4)}</strong>
                  </div>
                </div>
              )}

              <table className="hireism-table" style={{ marginBottom: "32px" }}>
                <thead>
                  <tr>
                    <th>PERINGKAT</th>
                    <th>NIP</th>
                    <th>NAMA KARYAWAN</th>
                    <th style={{ textAlign: "right" }}>TOTAL BENEFIT</th>
                    <th style={{ textAlign: "right" }}>TOTAL COST</th>
                    <th style={{ textAlign: "right" }}>NILAI YI</th>
                  </tr>
                </thead>
                <tbody>
                  {filteredResults.map((r) => (
                    <tr key={r.id}>
                      <td><strong>#{r.rankPosition}</strong></td>
                      <td><code>{r.employee.nip}</code></td>
                      <td><strong>{r.employee.fullName}</strong></td>
                      <td style={{ textAlign: "right", fontFamily: "var(--font-mono)" }}>{r.sumBenefit.toFixed(4)}</td>
                      <td style={{ textAlign: "right", fontFamily: "var(--font-mono)" }}>{r.sumCost.toFixed(4)}</td>
                      <td style={{ textAlign: "right", fontFamily: "var(--font-mono)", fontWeight: 700 }}>{r.yScore.toFixed(4)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>

              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "40px", marginTop: "40px", textAlign: "center", fontSize: "0.88rem" }}>
                <div>
                  <p style={{ color: "#64748b" }}>Mengetahui &amp; Menyetujui,</p>
                  <p style={{ fontWeight: 700, marginTop: "4px" }}>PT ISS INDONESIA</p>
                  <div style={{ height: "65px", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
                    <div style={{ fontSize: "0.72rem", color: "#0284c7", fontWeight: 700, border: "1px dashed #bae6fd", padding: "4px 10px", borderRadius: "8px", background: "#f0f9ff" }}>
                      SUBMITTED BY SUPERVISOR
                    </div>
                  </div>
                  <p style={{ fontWeight: 700, textDecoration: "underline" }}>Septo Aribowo</p>
                  <p style={{ fontSize: "0.8rem", color: "#64748b" }}>Site Supervisor Prodia Kebayoran</p>
                </div>

                <div>
                  <p style={{ color: "#64748b" }}>Mengesahkan Perwakilan Klien,</p>
                  <p style={{ fontWeight: 700, marginTop: "4px" }}>LABORATORIUM KLINIK PRODIA</p>
                  <div style={{ height: "65px", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
                    {skApproved ? (
                      <div className="digital-signature-seal">
                        <span>✓ VERIFIED &amp; APPROVED</span>
                        <span style={{ fontSize: "0.62rem", opacity: 0.85 }}>E-SIGNATURE PRODIA</span>
                      </div>
                    ) : (
                      <span style={{ fontSize: "0.78rem", color: "#94a3b8", fontStyle: "italic" }}>(Menunggu Pengesahan Resmi)</span>
                    )}
                  </div>
                  <p style={{ fontWeight: 700, textDecoration: "underline" }}>Siska Darmayanti</p>
                  <p style={{ fontSize: "0.8rem", color: "#64748b" }}>Branch Manager Prodia Kebayoran</p>
                </div>
              </div>
            </div>
          </div>
        )}
      </main>

      {/* ===================================================================== */}
      {/* 3. RIGHT PANEL (SCHEDULE, TOP APPLICANTS, QUICK ACTIONS)             */}
      {/* ===================================================================== */}
      {activeMenu === "dashboard" && (
        <aside className="hireism-right-panel no-print">
          {/* Top Profile Strip */}
          <div className="panel-user-header">
          <div className="user-quick-actions">
            {/* Tombol Pengaturan Interaktif */}
            <button
              type="button"
              className="icon-action-bubble"
              title="Pengaturan Sistem & MOORA"
              onClick={() => {
                setShowSettings(true);
                setShowNotifications(false);
              }}
              aria-label="Pengaturan"
            >
              <Settings size={16} />
            </button>

            {/* Tombol Notifikasi */}
            <div style={{ position: "relative" }}>
              <button
                type="button"
                className="icon-action-bubble"
                title="Pusat Notifikasi"
                onClick={() => {
                  setShowNotifications(!showNotifications);
                  setShowSettings(false);
                }}
                aria-label="Notifikasi"
              >
                <Bell size={16} />
                {unreadCount > 0 && (
                  <span className="notif-badge-bubble">{unreadCount}</span>
                )}
              </button>
            </div>
          </div>

          <div className="user-meta-strip">
            <div>
              <div className="user-profile-name">{currentUser?.fullName?.split(" ")[0]} {currentUser?.fullName?.split(" ")[1] || ""}</div>
              <div style={{ marginTop: "4px" }}>
                {getRoleBadge(currentUser?.role)}
              </div>
            </div>
            <div className="user-portrait-circle">
              {currentUser?.fullName?.charAt(0) || "U"}
            </div>
          </div>
        </div>

        {/* Schedule Calendar Widget (Exact style from Reference Image) */}
        <div className="hireism-calendar-widget">
          <div className="calendar-widget-head">
            <h4>Jadwal Penilaian &lt; &gt;</h4>
            <span className="calendar-month-pill">Oktober 2026</span>
          </div>

          <div className="calendar-days-row">
            <div className="day-slot-pill">
              <span>Sen</span>
              <strong>19</strong>
            </div>
            <div className="day-slot-pill">
              <span>Sel</span>
              <strong>20</strong>
            </div>
            <div className="day-slot-pill active">
              <span>Rab</span>
              <strong>21</strong>
            </div>
            <div className="day-slot-pill">
              <span>Kam</span>
              <strong>22</strong>
            </div>
            <div className="day-slot-pill">
              <span>Jum</span>
              <strong>23</strong>
            </div>
          </div>
        </div>

        {/* Top Applicants / Podium Widget (Reference Style "New Applicants") */}
        <div>
          <div className="hireism-section-head">
            <h4 style={{ fontSize: "0.95rem", fontWeight: 800 }}>Kandidat Unggul (Top 3)</h4>
            <button className="hireism-pill-link" onClick={() => setActiveMenu("dashboard")}>
              Lihat Semua
            </button>
          </div>

          <div className="hireism-applicants-list">
            {filteredResults.slice(0, 3).map((candidate, idx) => (
              <div key={candidate.id} className="applicant-card-row">
                <div className="applicant-bio">
                  <div
                    className="applicant-avatar"
                    style={{ background: getCandidateAvatarGradient(candidate, idx) }}
                  >
                    {candidate.employee.fullName.charAt(0)}
                  </div>
                  <div>
                    <div className="applicant-name">{candidate.employee.fullName}</div>
                    <div className="applicant-role">
                      Skor Yi: <strong>{candidate.yScore.toFixed(4)}</strong>
                    </div>
                  </div>
                </div>

                <div className="applicant-icon-actions">
                  <button
                    className="mini-icon-btn"
                    title="Beri Nilai"
                    onClick={() => {
                      setSelectedEmployeeForEval(candidate.employee.id);
                      setActiveMenu("assessment");
                    }}
                  >
                    <Star size={13} />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Ready For Training / Quick Actions Section in Reference */}
        <div>
          <div className="hireism-section-head">
            <h4 style={{ fontSize: "0.95rem", fontWeight: 800 }}>Rekomendasi Insentif</h4>
            <span style={{ fontSize: "0.72rem", color: "#8c9bb0" }}>Prodia Kebayoran</span>
          </div>

          <div className="mini-trainee-grid">
            {filteredResults.slice(0, 3).map((item, idx) => (
              <div key={item.id} className="mini-trainee-card">
                <div
                  className="mini-trainee-avatar"
                  style={{ background: getCandidateAvatarGradient(item, idx) }}
                >
                  {item.employee.fullName.charAt(0)}
                </div>
                <div className="mini-trainee-name">{item.employee.fullName.split(" ")[0]}</div>
                <div className="mini-trainee-sub">Rank #{item.rankPosition}</div>
                <button
                  className="mini-action-pill"
                  onClick={() => setActiveMenu("reports")}
                >
                  Pilih SK
                </button>
              </div>
            ))}
          </div>
        </div>
        </aside>
      )}

      {/* ===================================================================== */}
      {/* 4. MODAL PENGATURAN SPK MOORA INTERAKTIF                             */}
      {/* ===================================================================== */}
      {showSettings && (
        <div className="settings-modal-backdrop" onClick={() => setShowSettings(false)}>
          <div className="settings-modal-card" onClick={(e) => e.stopPropagation()}>
            <div className="settings-modal-header">
              <div className="settings-title-group">
                <div className="settings-header-icon">
                  <Settings size={22} />
                </div>
                <div>
                  <h3 style={{ fontSize: "1.05rem", fontWeight: 800, color: "var(--text-main)", margin: 0 }}>
                    Pengaturan SPK MOORA
                  </h3>
                  <p style={{ fontSize: "0.75rem", color: "var(--text-muted)", margin: 0 }}>
                    Konfigurasi parameter evaluasi unit PT ISS Indonesia - Prodia
                  </p>
                </div>
              </div>
              <button
                type="button"
                className="settings-close-btn"
                onClick={() => setShowSettings(false)}
                title="Tutup Pengaturan"
              >
                <X size={16} />
              </button>
            </div>

            <div className="settings-modal-body">
              {/* Section 1: Parameter MOORA */}
              <div className="settings-section-block">
                <div className="settings-section-title">
                  <SlidersHorizontal size={16} style={{ color: "var(--brand-blue)" }} />
                  Parameter Metode MOORA
                </div>

                <div className="settings-field-row">
                  <div>
                    <div className="settings-field-label">Ambang Batas Nilai Optimasi (Yi)</div>
                    <div className="settings-field-desc">
                      Nilai Yi minimal agar kandidat direkomendasikan mendapat insentif
                    </div>
                  </div>
                  <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                    <input
                      type="range"
                      min="0.100"
                      max="0.400"
                      step="0.005"
                      value={yiThreshold}
                      onChange={(e) => setYiThreshold(parseFloat(e.target.value))}
                      style={{ width: "110px", accentColor: "var(--brand-blue)" }}
                    />
                    <span style={{ fontWeight: 800, fontSize: "0.85rem", color: "var(--brand-blue)", minWidth: "46px" }}>
                      {yiThreshold.toFixed(4)}
                    </span>
                  </div>
                </div>

                <div className="settings-field-row">
                  <div>
                    <div className="settings-field-label">Normalisasi Vektor Otomatis</div>
                    <div className="settings-field-desc" style={{ display: "flex", alignItems: "center", gap: "8px", flexWrap: "wrap", marginTop: "5px" }}>
                      <span>Kalkulasi matriks real-time:</span>
                      <MiniVectorNormalizationBadge />
                    </div>
                  </div>
                  <label className="settings-toggle-switch">
                    <input
                      type="checkbox"
                      checked={autoSyncCalc}
                      onChange={(e) => setAutoSyncCalc(e.target.checked)}
                    />
                    <span className="settings-toggle-slider" />
                  </label>
                </div>
              </div>

              {/* Section 2: Info Unit & Periode */}
              <div className="settings-section-block">
                <div className="settings-section-title">
                  <Building2 size={16} style={{ color: "#10b981" }} />
                  Penempatan & Periode Penilaian
                </div>

                <div className="settings-field-row">
                  <div>
                    <div className="settings-field-label">Unit Penempatan Kerja</div>
                    <div className="settings-field-desc">Terkunci ke lokasi evaluasi aktif</div>
                  </div>
                  <span style={{ fontSize: "0.82rem", fontWeight: 700, color: "var(--text-main)", background: "#f1f5f9", padding: "4px 10px", borderRadius: "8px" }}>
                    Prodia Kebayoran
                  </span>
                </div>

                <div className="settings-field-row">
                  <div>
                    <div className="settings-field-label">Periode Penilaian Berjalan</div>
                    <div className="settings-field-desc">Tahun Anggaran 2026 Kuartal III</div>
                  </div>
                  <span style={{ fontSize: "0.82rem", fontWeight: 700, color: "var(--brand-blue)", background: "#eff6ff", padding: "4px 10px", borderRadius: "8px" }}>
                    Q3-2026 (Aktif)
                  </span>
                </div>
              </div>

              {/* Section 3: Akun Supervisor */}
              <div className="settings-section-block">
                <div className="settings-section-title">
                  <UserIcon size={16} style={{ color: "#f97316" }} />
                  Informasi Supervisor
                </div>

                <div className="settings-field-row">
                  <div>
                    <div className="settings-field-label">Penilai Resmi</div>
                    <div className="settings-field-desc">{currentUser?.fullName} ({currentUser?.role})</div>
                  </div>
                  <span style={{ fontSize: "0.78rem", fontWeight: 700, color: "#10b981", display: "flex", alignItems: "center", gap: 4 }}>
                    <CheckCircle2 size={14} /> Terverifikasi
                  </span>
                </div>
              </div>
            </div>

            <div className="settings-modal-footer">
              <button
                type="button"
                className="hireism-pill-link"
                onClick={() => setShowSettings(false)}
                style={{ background: "#ffffff", border: "1px solid var(--border-default)", color: "var(--text-muted)" }}
              >
                Batal
              </button>
              <button
                type="button"
                className="hireism-pill-link"
                onClick={() => {
                  setShowSettings(false);
                  showToast("Pengaturan sistem & ambang batas MOORA berhasil disimpan!");
                }}
                style={{ background: "var(--brand-blue)", color: "#ffffff", border: "none" }}
              >
                Simpan Pengaturan
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ===================================================================== */}
      {/* 4.2 MODAL EDIT KRITERIA & PEMBOBOTAN MOORA                           */}
      {/* ===================================================================== */}
      {editingCriteria && (
        <div className="settings-modal-backdrop" onClick={() => setEditingCriteria(null)}>
          <div className="settings-modal-card" onClick={(e) => e.stopPropagation()} style={{ maxWidth: "560px" }}>
            <div className="settings-modal-header">
              <div className="settings-title-group">
                <div className="settings-header-icon" style={{ background: "#eff6ff", color: "#2563eb" }}>
                  <Scale size={22} />
                </div>
                <div>
                  <h3 style={{ fontSize: "1.05rem", fontWeight: 800, color: "var(--text-main)", margin: 0 }}>
                    Edit Kriteria ({editingCriteria.code})
                  </h3>
                  <p style={{ fontSize: "0.75rem", color: "var(--text-muted)", margin: 0 }}>
                    Perbarui nama indikator, sifat Benefit/Cost, dan bobot preferensi MOORA
                  </p>
                </div>
              </div>
              <button
                type="button"
                className="settings-close-btn"
                onClick={() => setEditingCriteria(null)}
                title="Tutup Form Edit"
              >
                <X size={16} />
              </button>
            </div>

            <form onSubmit={handleUpdateCriteria}>
              <div className="settings-modal-body" style={{ display: "flex", flexDirection: "column", gap: "16px" }}>
                <div style={{ display: "grid", gridTemplateColumns: "1fr 2fr", gap: "12px" }}>
                  <div>
                    <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "var(--text-main)", marginBottom: "4px" }}>
                      Kode Kriteria:
                    </label>
                    <input
                      type="text"
                      value={editCritCode}
                      onChange={(e) => setEditCritCode(e.target.value)}
                      style={{ width: "100%", padding: "10px 12px", borderRadius: "10px", border: "1px solid var(--border-default)" }}
                      required
                    />
                  </div>
                  <div>
                    <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "var(--text-main)", marginBottom: "4px" }}>
                      Nama Indikator:
                    </label>
                    <input
                      type="text"
                      value={editCritName}
                      onChange={(e) => setEditCritName(e.target.value)}
                      style={{ width: "100%", padding: "10px 12px", borderRadius: "10px", border: "1px solid var(--border-default)" }}
                      required
                    />
                  </div>
                </div>

                <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "12px" }}>
                  <div>
                    <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "var(--text-main)", marginBottom: "4px" }}>
                      Sifat Kriteria:
                    </label>
                    <select
                      value={editCritType}
                      onChange={(e) => setEditCritType(e.target.value as any)}
                      style={{ width: "100%", padding: "10px 12px", borderRadius: "10px", border: "1px solid var(--border-default)" }}
                    >
                      <option value="BENEFIT">BENEFIT (Semakin besar semakin baik)</option>
                      <option value="COST">COST (Semakin kecil semakin baik)</option>
                    </select>
                  </div>
                  <div>
                    <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "var(--text-main)", marginBottom: "4px" }}>
                      Bobot W (Contoh: 0.20 = 20%):
                    </label>
                    <input
                      type="number"
                      step="0.01"
                      min="0.01"
                      max="1.00"
                      value={editCritWeight}
                      onChange={(e) => setEditCritWeight(e.target.value)}
                      style={{ width: "100%", padding: "10px 12px", borderRadius: "10px", border: "1px solid var(--border-default)" }}
                      required
                    />
                  </div>
                </div>

                <div>
                  <label style={{ display: "block", fontSize: "0.82rem", fontWeight: 700, color: "var(--text-main)", marginBottom: "4px" }}>
                    Deskripsi Standar Evaluasi:
                  </label>
                  <textarea
                    rows={3}
                    value={editCritDesc}
                    onChange={(e) => setEditCritDesc(e.target.value)}
                    placeholder="Uraian checklist mutu operasional Prodia Kebayoran..."
                    style={{ width: "100%", padding: "10px 12px", borderRadius: "10px", border: "1px solid var(--border-default)", resize: "vertical" }}
                  />
                </div>
              </div>

              <div className="settings-modal-footer">
                <button
                  type="button"
                  className="hireism-pill-link"
                  onClick={() => setEditingCriteria(null)}
                  style={{ background: "#ffffff", border: "1px solid var(--border-default)", color: "var(--text-muted)" }}
                >
                  Batal
                </button>
                <button
                  type="submit"
                  disabled={critSaving}
                  className="hireism-pill-link"
                  style={{ background: "var(--brand-blue)", color: "#ffffff", border: "none", display: "flex", alignItems: "center", gap: "6px" }}
                >
                  <Check size={16} />
                  <span>{critSaving ? "Menyimpan..." : "Simpan Perubahan"}</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* ===================================================================== */}
      {/* 4.3 MODAL KONFIRMASI HAPUS INTERAKTIF (MODERN DIALOG)               */}
      {/* ===================================================================== */}
      {deleteConfirmModal.isOpen && (
        <div
          className="settings-modal-backdrop"
          style={{ zIndex: 1200 }}
          onClick={() => setDeleteConfirmModal((prev) => ({ ...prev, isOpen: false }))}
        >
          <div
            className="settings-modal-card"
            onClick={(e) => e.stopPropagation()}
            style={{ maxWidth: "460px", padding: 0, overflow: "hidden", borderRadius: "18px", border: "1px solid #fecaca" }}
          >
            {/* Header Dialog */}
            <div
              style={{
                background: "linear-gradient(135deg, #fff1f2 0%, #fee2e2 100%)",
                padding: "20px 24px 16px",
                borderBottom: "1px solid #fecaca",
                display: "flex",
                alignItems: "flex-start",
                gap: "14px",
              }}
            >
              <div
                style={{
                  width: "44px",
                  height: "44px",
                  borderRadius: "12px",
                  background: "#ffffff",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  color: "#ef4444",
                  boxShadow: "0 4px 12px rgba(239, 68, 68, 0.15)",
                  flexShrink: 0,
                  border: "1px solid #fecaca",
                }}
              >
                <Trash2 size={22} />
              </div>
              <div style={{ flex: 1 }}>
                <h3 style={{ fontSize: "1.05rem", fontWeight: 800, color: "#991b1b", margin: 0 }}>
                  {deleteConfirmModal.title}
                </h3>
                <p style={{ fontSize: "0.8rem", color: "#b91c1c", margin: "3px 0 0" }}>
                  Konfirmasi tindakan penghapusan data permanen
                </p>
              </div>
              <button
                type="button"
                onClick={() => setDeleteConfirmModal((prev) => ({ ...prev, isOpen: false }))}
                style={{
                  background: "transparent",
                  border: "none",
                  cursor: "pointer",
                  color: "#991b1b",
                  padding: "4px",
                  borderRadius: "6px",
                }}
              >
                <X size={18} />
              </button>
            </div>

            {/* Isi Dialog */}
            <div style={{ padding: "20px 24px" }}>
              <p style={{ fontSize: "0.95rem", color: "#0f172a", fontWeight: 600, lineHeight: 1.5, margin: "0 0 12px" }}>
                {deleteConfirmModal.message}
              </p>
              {deleteConfirmModal.subMessage && (
                <div
                  style={{
                    background: "#fefce8",
                    border: "1px solid #fef08a",
                    borderLeft: "4px solid #eab308",
                    padding: "10px 14px",
                    borderRadius: "8px",
                    fontSize: "0.82rem",
                    color: "#854d0e",
                    lineHeight: 1.45,
                  }}
                >
                  <span style={{ fontWeight: 700 }}>Catatan Sistem: </span>
                  {deleteConfirmModal.subMessage}
                </div>
              )}
            </div>

            {/* Tombol Aksi */}
            <div
              style={{
                padding: "14px 24px",
                background: "#f8fafc",
                borderTop: "1px solid #e2e8f0",
                display: "flex",
                justifyContent: "flex-end",
                gap: "10px",
              }}
            >
              <button
                type="button"
                onClick={() => setDeleteConfirmModal((prev) => ({ ...prev, isOpen: false }))}
                style={{
                  padding: "9px 18px",
                  borderRadius: "10px",
                  border: "1px solid #cbd5e1",
                  background: "#ffffff",
                  color: "#475569",
                  fontWeight: 600,
                  fontSize: "0.85rem",
                  cursor: "pointer",
                }}
              >
                Batal
              </button>
              <button
                type="button"
                onClick={deleteConfirmModal.onConfirm}
                style={{
                  padding: "9px 20px",
                  borderRadius: "10px",
                  border: "none",
                  background: "#ef4444",
                  color: "#ffffff",
                  fontWeight: 700,
                  fontSize: "0.85rem",
                  cursor: "pointer",
                  display: "flex",
                  alignItems: "center",
                  gap: "6px",
                  boxShadow: "0 4px 12px rgba(239, 68, 68, 0.25)",
                }}
              >
                <Trash2 size={15} />
                <span>Ya, Hapus Data</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ===================================================================== */}
      {/* 4.5 NOTIFICATION CENTER MODAL (Global: Berfungsi di Mobile & Desktop) */}
      {/* ===================================================================== */}
      {showNotifications && (
        <div className="notif-modal-backdrop" onClick={() => setShowNotifications(false)}>
          <div className="notif-modal-card" onClick={(e) => e.stopPropagation()}>
            <div className="notif-popover-header">
              <div className="notif-header-title">
                <h4>Notifikasi</h4>
                {unreadCount > 0 && (
                  <span className="notif-count-badge">{unreadCount} Baru</span>
                )}
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: "8px" }}>
                {unreadCount > 0 && (
                  <button
                    type="button"
                    className="notif-mark-read-btn"
                    onClick={markAllNotificationsAsRead}
                  >
                    Tandai dibaca
                  </button>
                )}
                <button
                  type="button"
                  className="settings-modal-close"
                  style={{ width: 28, height: 28 }}
                  onClick={() => setShowNotifications(false)}
                  title="Tutup notifikasi"
                  aria-label="Tutup"
                >
                  <X size={15} />
                </button>
              </div>
            </div>

            <div className="notif-list-container">
              {notifications.length === 0 ? (
                <div className="notif-empty-state">Tidak ada notifikasi saat ini.</div>
              ) : (
                notifications.map((n) => (
                  <div
                    key={n.id}
                    className={`notif-item-card ${!n.read ? "unread" : ""}`}
                    onClick={() => {
                      handleNotificationClick(n);
                      setShowNotifications(false);
                    }}
                  >
                    <div
                      className="notif-icon-circle"
                      style={{
                        background:
                          n.category === "moora"
                            ? "#eff6ff"
                            : n.category === "incentive"
                            ? "#ecfdf5"
                            : n.category === "assessment"
                            ? "#fff7ed"
                            : "#f1f5f9",
                        color:
                          n.category === "moora"
                            ? "#3b5bfd"
                            : n.category === "incentive"
                            ? "#10b981"
                            : n.category === "assessment"
                            ? "#f97316"
                            : "#64748b",
                      }}
                    >
                      {n.category === "moora" && <Calculator size={15} />}
                      {n.category === "incentive" && <Award size={15} />}
                      {n.category === "assessment" && <ClipboardCheck size={15} />}
                      {n.category === "system" && <Building2 size={15} />}
                    </div>
                    <div className="notif-content-wrap">
                      <div className="notif-item-title">{n.title}</div>
                      <div className="notif-item-text">{n.message}</div>
                      <div className="notif-item-time">{n.time}</div>
                    </div>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      )}

      {/* ===================================================================== */}
      {/* 5. MOBILE BOTTOM NAVIGATION DOCK (Hanya Layar <= 1024px)              */}
      {/* ===================================================================== */}
      <nav className="mobile-bottom-dock no-print">
        <button
          type="button"
          className={`dock-btn ${activeMenu === "dashboard" ? "active" : ""}`}
          onClick={() => setActiveMenu("dashboard")}
        >
          <LayoutDashboard size={20} />
          <span>Beranda</span>
        </button>

        <button
          type="button"
          className={`dock-btn ${activeMenu === "moora" ? "active" : ""}`}
          onClick={() => setActiveMenu("moora")}
        >
          <Calculator size={20} />
          <span>MOORA</span>
        </button>

        {/* Khusus Supervisor: Tombol Nilai */}
        {isSupervisor && (
          <button
            type="button"
            className={`dock-btn ${activeMenu === "assessment" ? "active" : ""}`}
            onClick={() => setActiveMenu("assessment")}
          >
            <ClipboardCheck size={20} />
            <span>Nilai</span>
          </button>
        )}

        {/* Khusus Admin: Tombol Karyawan */}
        {isAdmin && (
          <button
            type="button"
            className={`dock-btn ${activeMenu === "employees" ? "active" : ""}`}
            onClick={() => setActiveMenu("employees")}
          >
            <Users size={20} />
            <span>Karyawan</span>
          </button>
        )}

        {/* Kriteria: Semua Role */}
        <button
          type="button"
          className={`dock-btn ${activeMenu === "criteria" ? "active" : ""}`}
          onClick={() => setActiveMenu("criteria")}
        >
          <Scale size={20} />
          <span>Kriteria</span>
        </button>

        {/* Khusus Manager & Supervisor: Tombol Laporan / Pengesahan SK */}
        {(isManager || isSupervisor) && (
          <button
            type="button"
            className={`dock-btn ${activeMenu === "reports" ? "active" : ""}`}
            onClick={() => setActiveMenu("reports")}
          >
            <FileText size={20} />
            <span>{isManager ? "SK Insentif" : "Laporan"}</span>
          </button>
        )}

        <button
          type="button"
          className="dock-btn"
          onClick={() => setMobileMenuOpen(true)}
        >
          <SlidersHorizontal size={20} />
          <span>Menu</span>
        </button>
      </nav>

      {/* MOBILE DRAWER SHEET (Menu Tambahan) */}
      {mobileMenuOpen && (
        <div className="mobile-drawer-backdrop" onClick={() => setMobileMenuOpen(false)}>
          <div className="mobile-drawer-sheet" onClick={(e) => e.stopPropagation()}>
            <div className="mobile-drawer-handle" />
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 14 }}>
              <div>
                <h4 style={{ fontSize: "1rem", fontWeight: 800, margin: 0, color: "var(--text-main)" }}>Menu Sistem SPK</h4>
                <div style={{ marginTop: "3px" }}>{getRoleBadge(currentUser?.role)}</div>
              </div>
              <button
                type="button"
                className="settings-close-btn"
                onClick={() => setMobileMenuOpen(false)}
              >
                <X size={16} />
              </button>
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
              {/* Tambahan untuk Admin jika ingin akses Laporan dari menu */}
              {isAdmin && (
                <button
                  type="button"
                  className={`mobile-drawer-item ${activeMenu === "reports" ? "active" : ""}`}
                  onClick={() => { setActiveMenu("reports"); setMobileMenuOpen(false); }}
                >
                  <FileText size={18} />
                  <span>Laporan Berita Acara &amp; SK</span>
                </button>
              )}

              <button
                type="button"
                className="mobile-drawer-item"
                onClick={() => { setShowSettings(true); setMobileMenuOpen(false); }}
              >
                <Settings size={18} />
                <span>Pengaturan Sistem &amp; Parameter Yi</span>
              </button>

              <div style={{ height: 1, background: "var(--border-light)", margin: "8px 0" }} />

              <button
                type="button"
                className="mobile-drawer-item danger"
                onClick={() => { setMobileMenuOpen(false); handleLogout(); }}
              >
                <LogOut size={18} />
                <span>Keluar dari Akun</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
