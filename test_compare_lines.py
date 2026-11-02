import subprocess
import os

def render_svg(svg_code, out_name):
    html = f'''<!DOCTYPE html><html><body style="margin:0;padding:0;background:#fff;display:flex;justify-content:center;">{svg_code}</body></html>'''
    with open(f'public/diagrams/{out_name}.html', 'w') as f:
        f.write(html)
    cmd = [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless',
        '--disable-gpu',
        '--window-size=1600,1020',
        f'--screenshot=public/diagrams/{out_name}.png',
        f'file://{os.path.abspath(f"public/diagrams/{out_name}.html")}'
    ]
    subprocess.run(cmd, check=True)
    print(f"Rendered {out_name}.png")

base_svg = open('public/diagrams/test_use_case.svg').read()

# 1. Straight Line from Super Admin
lines_straight = '''  <!-- Association Lines -->
  <g stroke="#111827" stroke-width="1.8">
    <!-- Super Admin connects to UC 1, 2, and 5 (Dashboard) -->
    <line x1="200" y1="248" x2="415" y2="205" />
    <line x1="200" y1="248" x2="415" y2="315" />
    <line x1="200" y1="248" x2="415" y2="690" />

    <!-- Site Supervisor connects to UC 3, 4, & 5 -->
    <line x1="200" y1="503" x2="415" y2="445" />
    <line x1="200" y1="503" x2="415" y2="555" />
    <line x1="200" y1="503" x2="415" y2="690" />

    <!-- Branch Manager connects to UC 5 & 6 -->
    <line x1="200" y1="758" x2="415" y2="690" />
    <line x1="200" y1="758" x2="415" y2="815" />
  </g>'''

svg_straight = base_svg.replace(
    base_svg[base_svg.find('  <!-- Association Lines -->'):base_svg.find('  <!-- Column 1: Primary Use Cases')],
    lines_straight + '\n\n'
)

with open('public/diagrams/use_case_straight.svg', 'w') as f:
    f.write(svg_straight)

render_svg(svg_straight, 'use_case_straight')
