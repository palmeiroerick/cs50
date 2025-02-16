from fpdf import FPDF


name = input("Name: ")
header_text = "CS50 Shirtificate"

pdf = FPDF()

pdf.add_page()

pdf.set_font("helvetica", size=50)
pdf.cell(0, 50, text=header_text, align="C", new_x="LMARGIN", new_y="NEXT")

pdf.image("shirtificate.png", x=10, y=76, w=190, keep_aspect_ratio=True)

pdf.set_font("Helvetica", "B", size=28)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 180, align="C", text=f"{name} took CS50")

pdf.output("shirtificate.pdf")
