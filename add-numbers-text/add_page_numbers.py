import fitz  # PyMuPDF
from num2words import num2words

# Load the PDF
pdf_path = "expediente.pdf"
doc = fitz.open(pdf_path)

# Process each page
for i, page in enumerate(doc, start=1):
    page_number_text = f"{i} - {num2words(i, lang='es')}"
    page.insert_text((500, 20), page_number_text, fontsize=15, color=(0, 0, 1), fontname="times-italic")

# Save the modified PDF
output_pdf_path = "expediente_numbered.pdf"
doc.save(output_pdf_path)
doc.close()

print(f"PDF saved as {output_pdf_path}")
