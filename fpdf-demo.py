# ? fpdf demo app from @ https://python.plainenglish.io/best-python-libraries-to-write-reports-to-pdf-87771be815c9

from fpdf import FPDF

data = [{"a": 1, "b": 2, "c": 3, "d": 4}, {"a": 5, "b": 6, "c": 7, "d": 8}]


def write_table_using_fpdf():
    pdf = FPDF(orientation="landscape", format="a3")
    pdf.add_page()
    pdf.set_font("Times", size=12)

    # set the line height and column width
    line_height = pdf.font_size * 17.5
    col_width = pdf.epw / 5

    for row in data:
        for k, v in row.items():
            print(v)
            pdf.multi_cell(col_width, line_height, str(v), border=1, ln=3, max_line_height=pdf.font_size, align="L")
        pdf.ln(line_height)
    pdf.output(name="pdf_using_fpdf.pdf")


write_table_using_fpdf()
