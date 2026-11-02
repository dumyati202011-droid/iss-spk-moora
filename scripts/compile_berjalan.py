import os
import subprocess

with open("/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_berjalan.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Make sure End Node is precisely at cx = 170
old_circle = '<circle cx="270" cy="664"'
if old_circle in html_content:
    html_content = html_content.replace('<circle cx="270" cy="664" r="14" fill="#ffffff" stroke="#1e293b" stroke-width="2" />\n      <circle cx="270" cy="664" r="8" fill="#1e293b" />',
                                        '<circle cx="170" cy="664" r="14" fill="#ffffff" stroke="#1e293b" stroke-width="2" />\n      <circle cx="170" cy="664" r="8" fill="#1e293b" />\n      <text x="170" y="694" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">Selesai</text>')
    html_content = html_content.replace('<line x1="385" y1="664" x2="284" y2="664"', '<line x1="385" y1="664" x2="184" y2="664"')

with open("/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_berjalan.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Extract SVG pure
start_tag = "<svg"
end_tag = "</svg>"
s_idx = html_content.find(start_tag)
e_idx = html_content.find(end_tag) + len(end_tag)
pure_svg = html_content[s_idx:e_idx]

svg_path = "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_diagram_sistem_berjalan.svg"
png_path = "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_diagram_sistem_berjalan.png"
artifact_dir = "/Users/mr.rnvrs/.gemini/antigravity-ide/brain/bf16a660-61d1-4c97-9b52-171c84a54e6d"

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(pure_svg)

with open(os.path.join(artifact_dir, "activity_diagram_sistem_berjalan.svg"), "w", encoding="utf-8") as f:
    f.write(pure_svg)

print("SVG extracted and saved.")

# Screenshot with Chrome headless
chrome_cmd = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=1060,820",
    f"--screenshot={png_path}",
    "/Users/mr.rnvrs/nama-project/iss-spk-moora/public/diagrams/activity_berjalan.html"
]

res = subprocess.run(chrome_cmd, capture_output=True, text=True)
print("Chrome exit code:", res.returncode)

subprocess.run(["cp", png_path, os.path.join(artifact_dir, "activity_diagram_sistem_berjalan.png")])
print("PNG compiled and copied to artifact successfully!")
