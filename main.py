import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    filename = Path(filepath).stem
    invoice_number = filename.split('-')[0]
    date = filename.split('-')[1]

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=22)
    pdf.cell(w=0, h=10, txt=f"Invoice number: {invoice_number}", align="L")
    pdf.ln(10)
    pdf.cell(w=0, h=10, txt=f"Date: {date}", align="L")
    pdf.output(f"PDF_invoices/{filename}.pdf")

