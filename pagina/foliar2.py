import fitz  # PyMuPDF
from num2words import num2words

pdf = fitz.open("input.pdf")

for i, page in enumerate(pdf):
    num_text = num2words(i+1, lang='es')
    
    page.insert_text(
        (400, 800),
        num_text,
        fontsize=12
    )

pdf.save("output.pdf")