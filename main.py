import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    filename = Path(filepath).stem
    invoice_number = filename.split('-')[0]
    date = filename.split('-')[1]
    # invoice_number, date = filename.split('-')  ----> Alternate and simple method

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=22)
    pdf.cell(w=0, h=10, txt=f"Invoice number: {invoice_number}", align="L", ln=1)
    pdf.cell(w=0, h=10, txt=f"Date: {date}", align="L", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    columns = df.columns
    columns = [each_item.replace('_', ' ').title() for each_item in columns]
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=60, h=8, txt=columns[1], border=1)
    pdf.cell(w=45, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=25, h=8, txt=columns[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=60, h=8, txt=row['product_name'], border=1)
        pdf.cell(w=45, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=25, h=8, txt=str(row['total_price']), border=1, ln=1)

    pdf.output(f"PDF_invoices/{filename}.pdf")

