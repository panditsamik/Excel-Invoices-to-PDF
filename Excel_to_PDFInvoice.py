import glob
import pathlib

from fpdf import FPDF
import pandas

fileNames = glob.glob("files/*.xlsx")

pg_No = 1

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for file in fileNames:
    df = pandas.read_excel(file, sheet_name="Sheet 1")
    pdf.add_page()

    fileNo = pathlib.Path(file).stem
    fileNoUpdated = fileNo.split("-")
    invoice_no = str(fileNoUpdated[0])
    date = str(fileNoUpdated[1])
    pdf.set_font(family="Times", size=15, style="B")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=f"Invoice Number :{invoice_no}", ln=1, align="L")
    pdf.cell(w=0, h=10, txt=f"Date :{date}", ln=1, align="L")

    header_list = list(df.columns)
    header_list = [item.replace("_", " ").title() for item in header_list]
    pdf.set_font(family="Times", size=12, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=str(header_list[0]), ln=0, border=1)
    pdf.cell(w=70, h=8, txt=str(header_list[1]), ln=0, border=1)
    pdf.cell(w=40, h=8, txt=str(header_list[2]), ln=0, border=1)
    pdf.cell(w=30, h=8, txt=str(header_list[3]), ln=0, border=1)
    pdf.cell(w=23, h=8, txt=str(header_list[4]), ln=1, border=1)

    for index, dict in df.iterrows():
        pdf.set_font(family="Times", size=8, style="I")
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(dict["product_id"]), ln=0, border=1)
        pdf.cell(w=70, h=8, txt=str(dict["product_name"]), ln=0, border=1)
        pdf.cell(w=40, h=8, txt=str(dict["amount_purchased"]), ln=0, border=1)
        pdf.cell(w=30, h=8, txt=str(dict["price_per_unit"]), ln=0, border=1)
        pdf.cell(w=23, h=8, txt=str(dict["total_price"]), ln=1, border=1)

    total = df["total_price"].sum()
    amount_purchased = df["amount_purchased"].sum()
    pdf.cell(w=30, h=8, txt=str("Total"), ln=0, border=1)
    pdf.cell(w=70, h=8, txt="", ln=0, border=1)
    pdf.cell(w=40, h=8, txt=str(amount_purchased), ln=0, border=1)
    pdf.cell(w=30, h=8, txt="", ln=0, border=1)
    pdf.cell(w=23, h=8, txt=str(total), ln=1, border=1)

    pdf.set_font(family="Times", size=14, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=0, h=15, txt=f"The total price of {amount_purchased} items is Rs. {total}.", ln=1, align="L")
    pdf.image("pythonhow.png", w=10)

    pdf.ln(220)
    pdf.set_font(family="Times", size=14, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=0, h=15, txt=str(pg_No), ln=1, align="C")
    pg_No += 1

pdf.output(f"PDFs/Page1.pdf")
