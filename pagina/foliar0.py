import fitz
from num2words import num2words

pdf = fitz.open("input.pdf")

for i, page in enumerate(pdf):
    width = page.rect.width
    height = page.rect.height

    text = num2words(i+1, lang='es')

    page.insert_text(
        (width/2 - 50, height - 30),
        text,
        fontsize=12
    )

pdf.save("output.pdf")