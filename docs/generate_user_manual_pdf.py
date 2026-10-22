"""
Direct Markdown-to-PDF compiler for docs/User_Manual.md
Reads the actual User_Manual.md file and generates docs/User_Manual.pdf using fpdf2.
"""

import os
import re
from fpdf import FPDF

class UserManualPDF(FPDF):
    def __init__(self, project_title="IT 3131 Final Project"):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(15, 15, 15)
        self.project_title = project_title

    def header(self):
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(90, 100, 115)
        self.cell(0, 5, "MiniOS Alpha -- User Manual", border=0, align="L")
        self.cell(0, 5, self.project_title, border=0, align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(200, 205, 215)
        self.set_line_width(0.3)
        self.line(15, 12, self.w - 15, 12)
        self.ln(3)

    def footer(self):
        self.set_y(-12)
        self.set_draw_color(200, 205, 215)
        self.set_line_width(0.3)
        self.line(15, self.h - 12, self.w - 15, self.h - 12)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(110, 115, 125)
        self.cell(0, 8, "MiniOS Alpha Simulator", border=0, align="L")
        self.cell(0, 8, f"Page {self.page_no()}", border=0, align="R")

    def sanitize(self, text):
        return (
            text.replace("—", "--")
            .replace("–", "-")
            .replace("•", "-")
            .replace("“", '"')
            .replace("”", '"')
            .replace("‘", "'")
            .replace("’", "'")
        )

    def render_doc_header(self, title, metadata):
        self.ln(2)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(20, 35, 60)
        self.cell(0, 8, self.sanitize(title), border=0, align="L", new_x="LMARGIN", new_y="NEXT")
        
        self.set_font("Helvetica", "", 9)
        self.set_text_color(80, 90, 105)
        meta_str = " | ".join(metadata)
        self.cell(0, 5, self.sanitize(meta_str), border=0, align="L", new_x="LMARGIN", new_y="NEXT")
        
        self.set_draw_color(30, 60, 110)
        self.set_line_width(0.8)
        self.line(15, self.get_y() + 2, self.w - 15, self.get_y() + 2)
        self.ln(4)

    def h2(self, text):
        self.ln(2)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(25, 45, 80)
        self.set_fill_color(240, 244, 250)
        self.cell(0, 6.5, f" {self.sanitize(text)}", border=0, fill=True, align="L", new_x="LMARGIN", new_y="NEXT")
        self.ln(1.5)

    def h3(self, text):
        self.ln(1.5)
        self.set_font("Helvetica", "B", 9.5)
        self.set_text_color(40, 60, 95)
        self.cell(0, 5, self.sanitize(text), border=0, align="L", new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)

    def command_header(self, name):
        if self.get_y() > self.h - 38:
            self.add_page()
        self.ln(1)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(20, 40, 80)
        self.cell(0, 5, f"COMMAND: {self.sanitize(name)}", border=0, new_x="LMARGIN", new_y="NEXT")

    def para(self, text):
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(40, 45, 55)
        self.multi_cell(0, 4.2, self.sanitize(text))
        self.ln(1)

    def bullet(self, text):
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(40, 45, 55)
        self.cell(4, 4.2, "-", border=0)
        self.multi_cell(0, 4.2, self.sanitize(text))
        self.ln(0.5)

    def key_val(self, key, val, val_is_code=False):
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(70, 75, 85)
        self.set_x(15)
        self.cell(16, 4, f"{key}:", border=0)
        self.set_x(31)
        if val_is_code:
            self.set_font("Courier", "B", 8)
            self.set_text_color(20, 30, 55)
        else:
            self.set_font("Helvetica", "", 8)
            self.set_text_color(35, 40, 50)
        self.multi_cell(self.w - 31 - 15, 4, self.sanitize(val))

    def code_box(self, code_text):
        lines = self.sanitize(code_text).strip("\n").split("\n")
        self.set_font("Courier", "", 7.5)
        self.set_fill_color(248, 250, 252)
        self.set_draw_color(215, 220, 228)
        self.set_text_color(25, 30, 40)
        
        line_height = 3.6
        block_h = len(lines) * line_height + 3
        if self.get_y() + block_h > self.h - 15:
            self.add_page()
            
        start_y = self.get_y()
        self.rect(15, start_y, self.w - 30, block_h, style="DF")
        self.set_y(start_y + 1.5)
        for line in lines:
            self.set_x(17)
            self.cell(self.w - 34, line_height, line.replace("\t", "    "), border=0, new_x="LMARGIN", new_y="NEXT")
        self.set_y(start_y + block_h + 1.5)

    def render_table(self, headers, rows):
        if self.get_y() > self.h - 35:
            self.add_page()
        self.set_font("Helvetica", "B", 8)
        self.set_fill_color(230, 238, 248)
        self.set_draw_color(200, 210, 225)
        
        col_w = (self.w - 30) / len(headers)
        for h in headers:
            self.cell(col_w, 5, self.sanitize(h), border=1, fill=True, align="L")
        self.ln()
        
        self.set_font("Helvetica", "", 8)
        for row in rows:
            for cell in row:
                self.cell(col_w, 4.5, self.sanitize(cell), border=1, align="L")
            self.ln()
        self.ln(2)

def build_pdf_from_md(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Determine Project Title from metadata
    project_title = "IT 3131 Final Project"
    for line in md_text.splitlines():
        if "**Project:**" in line:
            project_title = line.split("**Project:**")[1].strip()

    pdf = UserManualPDF(project_title=project_title)
    pdf.add_page()

    lines = md_text.splitlines()
    i = 0
    in_code = False
    code_buffer = []

    doc_title = "MiniOS Alpha -- User Manual"
    metadata = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Handle code blocks
        if stripped.startswith("```"):
            if in_code:
                in_code = False
                pdf.code_box("\n".join(code_buffer))
                code_buffer = []
            else:
                in_code = True
                code_buffer = []
            i += 1
            continue

        if in_code:
            code_buffer.append(line)
            i += 1
            continue

        # Ignore thematic breaks
        if stripped == "---":
            i += 1
            continue

        # Title
        if stripped.startswith("# "):
            doc_title = stripped[2:].strip()
            i += 1
            continue

        # Metadata under title
        if stripped.startswith("**Operating System:**") or stripped.startswith("**Project:**"):
            clean_meta = stripped.replace("**", "").replace("`", "")
            metadata.append(clean_meta)
            if len(metadata) == 2:
                pdf.render_doc_header(doc_title, metadata)
            i += 1
            continue

        # H2
        if stripped.startswith("## "):
            pdf.h2(stripped[3:].strip())
            i += 1
            continue

        # H3
        if stripped.startswith("### "):
            pdf.h3(stripped[4:].strip())
            i += 1
            continue

        # COMMAND:
        if stripped.startswith("#### COMMAND:"):
            cmd_name = stripped.split("#### COMMAND:")[1].strip()
            pdf.command_header(cmd_name)
            i += 1
            continue

        # Purpose, Syntax, Example
        if stripped.startswith("**Purpose:**"):
            purpose_text = stripped.replace("**Purpose:**", "").strip()
            # If purpose is on next line
            if not purpose_text and i + 1 < len(lines):
                i += 1
                purpose_text = lines[i].strip()
            pdf.key_val("Purpose", purpose_text)
            i += 1
            continue

        if stripped.startswith("**Syntax:**"):
            syntax_text = stripped.replace("**Syntax:**", "").strip()
            if not syntax_text and i + 1 < len(lines):
                i += 1
                syntax_text = lines[i].strip()
            syntax_clean = syntax_text.replace("`", "")
            pdf.key_val("Syntax", syntax_clean, val_is_code=True)
            i += 1
            continue

        if stripped.startswith("**Example:**"):
            pdf.set_font("Helvetica", "B", 8)
            pdf.set_text_color(70, 75, 85)
            pdf.cell(0, 4, "Example:", border=0, new_x="LMARGIN", new_y="NEXT")
            i += 1
            continue

        # Table detection
        if stripped.startswith("|") and stripped.endswith("|"):
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            i += 1
            if i < len(lines) and "---" in lines[i]:
                i += 1
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                row = [c.strip().replace("`", "") for c in lines[i].strip().strip("|").split("|")]
                rows.append(row)
                i += 1
            pdf.render_table(headers, rows)
            continue

        # Bullets
        if stripped.startswith("- ") or stripped.startswith("* "):
            bullet_text = stripped[2:].replace("`", "").replace("**", "")
            pdf.bullet(bullet_text)
            i += 1
            continue

        # Numbered list items
        num_match = re.match(r"^(\d+\.)\s+(.*)", stripped)
        if num_match:
            item_text = num_match.group(2).replace("`", "").replace("**", "").replace("_", "")
            pdf.bullet(f"{num_match.group(1)} {item_text}")
            i += 1
            continue

        # Regular paragraph
        if stripped:
            clean_para = stripped.replace("`", "").replace("**", "").replace("_", "")
            pdf.para(clean_para)

        i += 1

    pdf.output(pdf_path)
    print(f"Successfully generated {pdf_path} from {md_path}")

if __name__ == "__main__":
    md_file = os.path.abspath("docs/User_Manual.md")
    pdf_file = os.path.abspath("docs/User_Manual.pdf")
    build_pdf_from_md(md_file, pdf_file)
