import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <title>Panduan Praktis Menjalankan Aplikasi SPK MOORA di Windows</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    @page {
      size: A4 portrait;
      margin: 12mm 12mm 12mm 12mm;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      color: #1e293b;
      background: #ffffff;
      font-size: 9.5pt;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }

    .container {
      max-width: 100%;
      margin: 0 auto;
    }

    /* Header Banner */
    .header-card {
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 18px 22px;
      background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 60%, #312e81 100%);
      color: #ffffff;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .header-title h1 {
      font-size: 16pt;
      font-weight: 800;
      letter-spacing: -0.5px;
      margin-bottom: 4px;
      color: #ffffff;
    }

    .header-title p {
      font-size: 9pt;
      color: #cbd5e1;
    }

    .badge-doc {
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.3);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 8.5pt;
      font-weight: 600;
      color: #f8fafc;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* Grid Section */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 14px;
    }

    .card {
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 14px 16px;
      background: #ffffff;
    }

    .card-highlight {
      background: #f8fafc;
      border-left: 4px solid #3b82f6;
    }

    .card-title {
      font-size: 11pt;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Step boxes */
    .step-item {
      display: flex;
      gap: 12px;
      margin-bottom: 14px;
      align-items: flex-start;
    }

    .step-number {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #3b82f6;
      color: white;
      font-weight: 700;
      font-size: 10pt;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 2px 4px rgba(59, 130, 246, 0.3);
    }

    .step-content {
      flex: 1;
    }

    .step-content h3 {
      font-size: 10pt;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 4px;
    }

    .step-content p {
      font-size: 9pt;
      color: #475569;
      margin-bottom: 6px;
    }

    .code-block {
      background: #0f172a;
      color: #38bdf8;
      font-family: 'JetBrains Mono', Consolas, monospace;
      font-size: 8.5pt;
      padding: 7px 12px;
      border-radius: 6px;
      margin-top: 4px;
      word-break: break-all;
      border: 1px solid #1e293b;
    }

    .inline-code {
      background: #f1f5f9;
      color: #0f172a;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', Consolas, monospace;
      font-size: 8.5pt;
      font-weight: 600;
      border: 1px solid #e2e8f0;
    }

    /* Table */
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 8px;
      font-size: 8.8pt;
    }

    th {
      background: #f1f5f9;
      color: #334155;
      font-weight: 700;
      text-align: left;
      padding: 8px 10px;
      border-bottom: 2px solid #cbd5e1;
    }

    td {
      padding: 7px 10px;
      border-bottom: 1px solid #e2e8f0;
      color: #1e293b;
    }

    .role-badge {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 7.8pt;
      font-weight: 700;
      letter-spacing: 0.3px;
    }

    .badge-admin { background: #fee2e2; color: #991b1b; }
    .badge-spv { background: #e0e7ff; color: #3730a3; }
    .badge-mgr { background: #dcfce7; color: #166534; }

    /* Notice callout */
    .callout {
      border-radius: 8px;
      padding: 10px 14px;
      margin-top: 10px;
      font-size: 8.8pt;
      display: flex;
      gap: 10px;
      align-items: flex-start;
    }

    .callout-warning {
      background: #fffbeb;
      border-left: 4px solid #f59e0b;
      color: #92400e;
    }

    .callout-info {
      background: #eff6ff;
      border-left: 4px solid #3b82f6;
      color: #1e40af;
    }

    /* Footer */
    .footer {
      margin-top: 14px;
      padding-top: 10px;
      border-top: 1px solid #e2e8f0;
      display: flex;
      justify-content: space-between;
      font-size: 8pt;
      color: #64748b;
    }
  </style>
</head>
<body>

  <div class="container">
    <!-- Header -->
    <div class="header-card">
      <div class="header-title">
        <h1>Panduan Praktis Menjalankan Aplikasi</h1>
        <p>Sistem Pendukung Keputusan (SPK) MOORA &bull; ISS Indonesia & Mitra Prodia</p>
      </div>
      <div class="badge-doc">Quick Reference &bull; Windows</div>
    </div>

    <!-- 4 Langkah Utama -->
    <div class="card" style="margin-bottom: 14px;">
      <div class="card-title">
        <span>🚀 4 Langkah Mudah Membuka Aplikasi di Windows</span>
      </div>

      <!-- Step 1 -->
      <div class="step-item">
        <div class="step-number">1</div>
        <div class="step-content">
          <h3>Buka Terminal / Command Prompt</h3>
          <p>Buka <b>Command Prompt (CMD)</b> atau terminal <b>VS Code</b>, lalu arahkan ke folder project:</p>
          <div class="code-block">cd "C:\\Users\\Thinkpad T460s\\Documents\\iss-spk-moora"</div>
        </div>
      </div>

      <!-- Step 2 -->
      <div class="step-item">
        <div class="step-number">2</div>
        <div class="step-content">
          <h3>Nyalakan Server Aplikasi</h3>
          <p>Ketik perintah berikut untuk menjalankan server Next.js lokal:</p>
          <div class="code-block">npm run dev</div>
          <p style="margin-top: 5px; color: #475569;">
            <i>Jika muncul konfirmasi upgrade: tekan tombol <b>Panah Bawah (↓)</b> ke arah <b>Skip</b> lalu tekan <b>Enter</b>.</i>
          </p>
        </div>
      </div>

      <!-- Step 3 -->
      <div class="step-item">
        <div class="step-number">3</div>
        <div class="step-content">
          <h3>Buka di Browser</h3>
          <p>Buka browser (Google Chrome, Microsoft Edge, dll.), lalu ketikkan alamat:</p>
          <div class="code-block" style="color: #4ade80;">http://localhost:3000</div>
        </div>
      </div>

      <!-- Step 4 -->
      <div class="step-item">
        <div class="step-number">4</div>
        <div class="step-content">
          <h3>Login Sesuai Kebutuhan</h3>
          <p>Gunakan salah satu akun yang tersedia pada tabel akun di bawah ini.</p>
        </div>
      </div>
    </div>

    <!-- Dua Kolom: Akun & Tips -->
    <div class="grid-2">
      <!-- Tabel Akun -->
      <div class="card">
        <div class="card-title">
          <span>🔑 Kredensial Akun Login</span>
        </div>
        <table>
          <thead>
            <tr>
              <th>Role</th>
              <th>Username</th>
              <th>Password</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="role-badge badge-admin">SUPER_ADMIN</span><br><small style="color:#64748b;">HRD ISS</small></td>
              <td><span class="inline-code">admin</span></td>
              <td><span class="inline-code">password123</span></td>
            </tr>
            <tr>
              <td><span class="role-badge badge-spv">SUPERVISOR</span><br><small style="color:#64748b;">Spv ISS Prodia</small></td>
              <td><span class="inline-code">spv_iss</span></td>
              <td><span class="inline-code">password123</span></td>
            </tr>
            <tr>
              <td><span class="role-badge badge-mgr">LAB_MANAGER</span><br><small style="color:#64748b;">Branch Manager</small></td>
              <td><span class="inline-code">manager_prodia</span></td>
              <td><span class="inline-code">password123</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Kontrol & Troubleshooting -->
      <div class="card card-highlight">
        <div class="card-title">
          <span>⚡ Tips & Kontrol Pintas</span>
        </div>
        
        <div style="font-size: 8.8pt; color: #334155; margin-bottom: 8px;">
          <b>🛑 Cara Mematikan Server:</b><br>
          Klik jendela CMD yang sedang menyala, tekan shortcut <span class="inline-code">Ctrl + C</span>, ketik <span class="inline-code">Y</span> lalu tekan <b>Enter</b>.
        </div>

        <div style="font-size: 8.8pt; color: #334155; margin-bottom: 8px;">
          <b>📂 Buka Cepat di VS Code:</b><br>
          Jika berada di terminal folder project, ketik <span class="inline-code">code .</span> lalu tekan <b>Enter</b>.
        </div>

        <div class="callout callout-warning" style="margin-top: 6px;">
          <span>⚠️ <b>Jika database belum terbaca:</b> Cukup pastikan file <span class="inline-code">.env</span> berisi <span class="inline-code">DATABASE_URL="file:./dev.db"</span> dan jalankan <span class="inline-code">npx prisma generate</span>.</span>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer">
      <span>Dokumentasi Teknis Implementasi Windows &bull; PT ISS Indonesia x Laboratorium Klinik Prodia</span>
      <span>Halaman 1 dari 1</span>
    </div>

  </div>

</body>
</html>
"""

html_path = "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/documents/PANDUAN_BUKA_APLIKASI_WINDOWS.html"
pdf_path = "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/documents/PANDUAN_BUKA_APLIKASI_WINDOWS.pdf"
artifact_pdf_path = "/Users/mr.rnvrs/.gemini/antigravity/brain/4861760a-b797-4d82-9786-3381fde01e51/PANDUAN_BUKA_APLIKASI_WINDOWS.pdf"

os.makedirs(os.path.dirname(html_path), exist_ok=True)
os.makedirs(os.path.dirname(artifact_pdf_path), exist_ok=True)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML saved to {html_path}")

# Run Chrome Headless to generate PDF
chrome_cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={pdf_path}",
    "--no-pdf-header-footer",
    html_path
]

res = subprocess.run(chrome_cmd, capture_output=True, text=True)
print("Chrome return code:", res.returncode)

if os.path.exists(pdf_path):
    size = os.path.getsize(pdf_path)
    print(f"PDF successfully generated: {pdf_path} ({size} bytes)")
    subprocess.run(["cp", pdf_path, artifact_pdf_path])
    print(f"PDF copied to artifact: {artifact_pdf_path}")
else:
    print("PDF generation failed!")
