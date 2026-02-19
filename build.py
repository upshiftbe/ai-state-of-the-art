#!/usr/bin/env python3
"""
Build script to convert README.md to index.html for GitHub Pages
Generates a dark, modern AI-themed webpage
"""

import markdown
from pathlib import Path

# Read the markdown file
readme_path = Path(__file__).parent / "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Convert markdown to HTML
html_body = markdown.markdown(md_content, extensions=["tables"])

# Create the full HTML page with dark AI theme
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI State of the ART</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.7;
            color: #e0e0e0;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1428 100%);
            min-height: 100vh;
            padding: 40px 20px;
            position: relative;
            overflow-x: hidden;
        }}

        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(0, 255, 136, 0.03) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(102, 51, 255, 0.03) 0%, transparent 50%);
            pointer-events: none;
            z-index: -1;
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
            background: rgba(15, 20, 40, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(0, 255, 136, 0.1);
            box-shadow: 0 8px 32px 0 rgba(0, 255, 136, 0.05),
                        inset 0 0 60px rgba(102, 51, 255, 0.02);
            padding: 50px;
            position: relative;
        }}

        h1 {{
            color: #00ff88;
            margin-bottom: 15px;
            font-size: 2.8em;
            font-weight: 700;
            text-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
            letter-spacing: -1px;
        }}

        h2 {{
            color: #00d4ff;
            margin-top: 40px;
            margin-bottom: 25px;
            font-size: 1.9em;
            font-weight: 600;
            border-bottom: 2px solid rgba(0, 255, 136, 0.3);
            padding-bottom: 12px;
            text-shadow: 0 0 10px rgba(0, 212, 255, 0.2);
        }}

        p {{
            margin-bottom: 20px;
            font-size: 1.05em;
            color: #c0c0c0;
            line-height: 1.8;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 30px 0;
            background: rgba(20, 30, 60, 0.4);
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid rgba(0, 255, 136, 0.15);
        }}

        th {{
            background: linear-gradient(135deg, rgba(0, 255, 136, 0.15) 0%, rgba(0, 212, 255, 0.1) 100%);
            color: #00ff88;
            padding: 16px 18px;
            text-align: left;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-size: 0.9em;
            border-bottom: 2px solid rgba(0, 255, 136, 0.2);
        }}

        td {{
            padding: 14px 18px;
            border-bottom: 1px solid rgba(0, 255, 136, 0.08);
            color: #d0d0d0;
        }}

        tr:hover {{
            background: rgba(0, 255, 136, 0.05);
            border-left: 3px solid rgba(0, 255, 136, 0.3);
            padding-left: 15px;
        }}

        a {{
            color: #00d4ff;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
            border-bottom: 1px solid rgba(0, 212, 255, 0.3);
        }}

        a:hover {{
            color: #00ff88;
            text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
            border-bottom: 1px solid rgba(0, 255, 136, 0.6);
        }}

        .credit {{
            margin-top: 50px;
            padding-top: 25px;
            padding: 20px;
            border-top: 1px solid rgba(0, 255, 136, 0.15);
            font-size: 0.95em;
            color: #a0a0a0;
            background: rgba(0, 255, 136, 0.02);
            border-radius: 8px;
        }}

        .credit strong {{
            color: #00ff88;
        }}

        /* Scrollbar styling */
        ::-webkit-scrollbar {{
            width: 10px;
        }}

        ::-webkit-scrollbar-track {{
            background: rgba(0, 255, 136, 0.05);
        }}

        ::-webkit-scrollbar-thumb {{
            background: rgba(0, 255, 136, 0.3);
            border-radius: 5px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(0, 255, 136, 0.5);
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 25px;
            }}

            h1 {{
                font-size: 2em;
            }}

            h2 {{
                font-size: 1.4em;
            }}

            table {{
                font-size: 0.9em;
            }}

            th, td {{
                padding: 10px 12px;
            }}

            p {{
                font-size: 1em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_body}
    </div>
</body>
</html>"""

# Write the output file
output_path = Path(__file__).parent / "index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✓ Built index.html from README.md - Dark AI Theme")
