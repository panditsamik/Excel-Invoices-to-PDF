import glob
import pathlib

from fpdf import FPDF

txtFiles = glob.glob("Text+Files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for file in txtFiles:
    pdf.add_page()

    fileName = str(file.split(".txt")[0])
    filenameUpdated = fileName.replace("Text+Files/", "").title()

    pdf.set_font(family="Times", size=15, style="B")
    pdf.set_text_color(80, 100, 80)
    pdf.cell(w=10, h=10, txt=str(filenameUpdated), ln=1, align="L")

    with open(file, "r") as write:
        content = write.read()

    pdf.set_font(family="Times", size=10, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.multi_cell(w=0, h=8, txt=content)

pdf.output("PDFs/Page2.pdf")
