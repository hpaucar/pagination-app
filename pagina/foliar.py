import fitz
from num2words import num2words

pdf = fitz.open("input.pdf")

for i, page in enumerate(pdf):
    width = page.rect.width

    numero = i + 1
    texto = num2words(numero, lang="es")

    # 👉 Caja en la parte superior derecha
    rect = fitz.Rect(width - 120, 10, width - 15, 40)

    contenido = f"{numero}\n{texto}"

    page.insert_textbox(
        rect,
        contenido,
        fontsize=8,
        fontfile=r"C:\Windows\Fonts\timesi.ttf",  # Times New Roman cursiva
        #fontfile=r"C:\Windows\Fonts\ariali.ttf",  # 👈 Arial cursiva
        color=(1, 0, 0),
        align=2  # derecha
    )

pdf.save("output.pdf")