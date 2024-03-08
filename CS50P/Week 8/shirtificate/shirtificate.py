from ctypes import alignment
from turtle import color
from fpdf import FPDF

data = input("Name: ").strip()

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.image("./shirtificate.png", x=10, y=20,
          keep_aspect_ratio=True, h=pdf.eph, w=pdf.epw)
with pdf.local_context("helvetica", "", 40):
    pdf.cell(pdf.epw, 40, "CS50 Shirtificate", align="C")
pdf.ln()
with pdf.local_context("helvetica", "B", 25):
    pdf.set_text_color(255, 255, 255)
    pdf.cell(w=pdf.epw, h=150, text=f"{data} took CS50", align="C")
pdf.ln()
pdf.output("shirtificate.pdf")
