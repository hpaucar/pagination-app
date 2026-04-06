import fitz  # PyMuPDF
from num2words import num2words

# Load the PDF
pdf_path = "file.pdf"
doc = fitz.open(pdf_path)

# Process each page
for i, page in enumerate(doc, start=1):
    width = page.rect.width

    page_number_text = f"{i}\n{num2words(i, lang='es')}"

    # 👉 Caja en la parte superior derecha
    rect = fitz.Rect(width - 150, 10, width - 10, 60)

    page.insert_textbox(
        rect,
        page_number_text,
        fontsize=10,
        color=(0.4, 0, 0.4),
        fontname="times-italic",
        #fontfile=r"C:\Windows\Fonts\timesi.ttf",  # Times New Roman cursiva
        align=2  # 👉 derecha
    )

# Save the modified PDF
output_pdf_path = "file_numbered.pdf"
doc.save(output_pdf_path)
doc.close()

print(f"PDF saved as {output_pdf_path}")
