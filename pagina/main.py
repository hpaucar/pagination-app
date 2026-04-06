import fitz  # PyMuPDF

pdf = fitz.open("input.pdf")

for i, page in enumerate(pdf):
    text = f"{i+1}"
    
    # Posición (x, y)
    page.insert_text(
        (500, 800),  # ajusta según tu PDF
        text,
        fontsize=12
    )

pdf.save("output.pdf")