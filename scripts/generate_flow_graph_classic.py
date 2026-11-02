import os
import subprocess

# Generate Flow Graph with EXACT visual style as user's reference image:
# - Minimalist academic textbook style (Pressman / Sommerville)
# - Circles with solid black offset drop shadow (+4.5px, +4.5px)
# - Light gray fill (#e2e4e6) with solid black stroke (1.8px)
# - Italic serif numbering (*1*, *2*, *3*...)
# - Pure black connector lines (1.6px) with crisp triangular arrowheads
# - Smooth curved return loop arrows
# - Clean white background, no clutter, perfectly cropped for Word document

W = 540
H = 960

# Spine centered at X = 280
nodes = {
    1:  (280, 60),    # Entry / Check Data Kosong
    2:  (140, 160),   # Return Kosong (Left branch)
    3:  (280, 160),   # Hitung Matriks X, Divisors, R, V
    4:  (280, 260),   # Loop Alternatif
    5:  (280, 360),   # Loop Kriteria
    6:  (280, 460),   # Decision BENEFIT/COST
    7:  (200, 560),   # Benefit (Left)
    8:  (360, 560),   # Cost (Right)
    9:  (280, 650),   # Merge Kriteria (Loop back to 5)
    10: (280, 740),   # Compute Yi (Loop back to 4)
    11: (280, 830),   # Sort Rankings
    12: (280, 905),   # Terminal Exit
}

R = 21 # Radius of node circles
SHADOW_OFFSET = 4.5

def generate_svg():
    svg_lines = [
        f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',
        '  <defs>',
        '    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">',
        '      <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#000000" />',
        '    </marker>',
        '  </defs>',
        f'  <rect width="{W}" height="{H}" fill="#ffffff" />',
        '  <!-- ================= EDGES (CONNECTING ARROWS) ================= -->'
    ]

    # Edge 1 -> 2 (Branch left)
    svg_lines.append('  <!-- Edge 1 -> 2 -->')
    svg_lines.append('  <path d="M 264 75 L 156 145" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 1 -> 3 (Straight down)
    svg_lines.append('  <!-- Edge 1 -> 3 -->')
    svg_lines.append('  <path d="M 280 81 L 280 137" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 2 -> 12 (Curved down left to terminal exit)
    svg_lines.append('  <!-- Edge 2 -> 12 -->')
    svg_lines.append('  <path d="M 125 175 C 50 280 40 800 258 900" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 3 -> 4 (Straight down)
    svg_lines.append('  <!-- Edge 3 -> 4 -->')
    svg_lines.append('  <path d="M 280 181 L 280 237" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 4 -> 5 (Straight down)
    svg_lines.append('  <!-- Edge 4 -> 5 -->')
    svg_lines.append('  <path d="M 280 281 L 280 337" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 4 -> 11 (Loop alternatif selesai - curved bypass on the right)
    svg_lines.append('  <!-- Edge 4 -> 11 -->')
    svg_lines.append('  <path d="M 301 260 C 450 290 450 790 302 827" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 5 -> 6 (Straight down)
    svg_lines.append('  <!-- Edge 5 -> 6 -->')
    svg_lines.append('  <path d="M 280 381 L 280 437" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 5 -> 10 (Loop kriteria selesai - curved bypass on inner right)
    svg_lines.append('  <!-- Edge 5 -> 10 -->')
    svg_lines.append('  <path d="M 299 370 C 400 400 400 700 300 735" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 6 -> 7 (BENEFIT - branch down left)
    svg_lines.append('  <!-- Edge 6 -> 7 -->')
    svg_lines.append('  <path d="M 266 477 L 214 543" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 6 -> 8 (COST - branch down right)
    svg_lines.append('  <!-- Edge 6 -> 8 -->')
    svg_lines.append('  <path d="M 294 477 L 346 543" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 7 -> 9 (Merge back to 9)
    svg_lines.append('  <!-- Edge 7 -> 9 -->')
    svg_lines.append('  <path d="M 214 577 L 266 633" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 8 -> 9 (Merge back to 9)
    svg_lines.append('  <!-- Edge 8 -> 9 -->')
    svg_lines.append('  <path d="M 346 577 L 294 633" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 9 -> 5 (Loop back kriteria on left)
    svg_lines.append('  <!-- Edge 9 -> 5 (Loop Kriteria) -->')
    svg_lines.append('  <path d="M 261 645 C 150 620 150 400 259 365" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 10 -> 4 (Loop back alternatif on left)
    svg_lines.append('  <!-- Edge 10 -> 4 (Loop Alternatif) -->')
    svg_lines.append('  <path d="M 260 740 C 90 710 90 300 259 265" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    # Edge 11 -> 12 (Straight down to exit)
    svg_lines.append('  <!-- Edge 11 -> 12 -->')
    svg_lines.append('  <path d="M 280 851 L 280 882" fill="none" stroke="#000000" stroke-width="1.6" marker-end="url(#arrow)" />')

    svg_lines.append('  <!-- ================= NODES ================= -->')

    for n_id, (cx, cy) in sorted(nodes.items()):
        # 1. Solid black shadow circle (offset +4.5, +4.5)
        svg_lines.append(f'  <!-- Node {n_id} Shadow -->')
        svg_lines.append(f'  <circle cx="{cx + SHADOW_OFFSET}" cy="{cy + SHADOW_OFFSET}" r="{R}" fill="#000000" />')
        # 2. Main circle (light gray fill #e3e5e8 with solid black stroke 1.6px)
        svg_lines.append(f'  <!-- Node {n_id} Body -->')
        svg_lines.append(f'  <circle cx="{cx}" cy="{cy}" r="{R}" fill="#e3e5e8" stroke="#000000" stroke-width="1.6" />')
        # 3. Node number in italic serif font (Times New Roman Italic)
        svg_lines.append(f'  <text x="{cx}" y="{cy + 5.5}" font-family="\'Times New Roman\', Times, Georgia, serif" font-style="italic" font-size="16" font-weight="normal" fill="#000000" text-anchor="middle">{n_id}</text>')

    svg_lines.append('</svg>')
    return '\n'.join(svg_lines)

if __name__ == "__main__":
    out_dir = "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams"
    svg_path = os.path.join(out_dir, "flow_graph_classic.svg")
    png_path = os.path.join(out_dir, "flow_graph_classic.png")
    html_path = os.path.join(out_dir, "flow_graph_classic.html")

    svg_content = generate_svg()

    # Save SVG
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[OK] Saved SVG: {svg_path}")

    # HTML wrapper for crisp rendering
    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
  </style>
</head>
<body>
  {svg_content}
</body>
</html>"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Rasterize to PNG with headless Chrome
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={W},{H}",
        f"--screenshot={png_path}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode == 0:
        print(f"[OK] Rendered PNG: {png_path}")
    else:
        print(f"[ERR] Chrome failed: {res.stderr.decode('utf-8')}")

    # Also copy to artifacts
    artifact_dir = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/e6c145f5-ba78-4f4a-bc31-4712ef0b13ed"
    if os.path.exists(artifact_dir):
        import shutil
        shutil.copyfile(svg_path, os.path.join(artifact_dir, "flow_graph_classic.svg"))
        shutil.copyfile(png_path, os.path.join(artifact_dir, "flow_graph_classic.png"))
        print(f"[OK] Copied to artifact: {png_path}")
