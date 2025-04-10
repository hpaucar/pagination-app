import fitz  # PyMuPDF
from num2words import num2words
from PIL import Image, ImageDraw, ImageFont
import os

# Load the PDF
pdf_path = "expediente.pdf"
doc = fitz.open(pdf_path)

# Ruta a la fuente manuscrita (ajusta si es necesario)
italic_font_path = "/usr/share/fonts/truetype/Dancing_Script/static/DancingScript-Regular.ttf"

# Crear carpeta para las imágenes
output_dir = "imgs"
os.makedirs(output_dir, exist_ok=True)

# Función para crear imagen con texto alineado a la derecha
def create_number_image(number_text):
    """Genera una imagen con texto en cursiva alineado a la derecha."""
    img_size = (200, 80)  # Tamaño de imagen (ancho, alto)
    img = Image.new("RGB", img_size, (255, 255, 255))  # Fondo blanco
    draw = ImageDraw.Draw(img)

    # Cargar fuente
    try:
        font = ImageFont.truetype(italic_font_path, 22)
    except IOError:
        print(f"⚠️ No se encontró la fuente: {italic_font_path}. Usando fuente por defecto.")
        font = ImageFont.load_default()

    # Dibujar cada línea alineada a la derecha
    lines = number_text.split("\n")
    y = 10
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = img_size[0] - text_width - 10  # 10px de margen derecho
        draw.text((x, y), line, font=font, fill=(0, 0, 255))  # Texto azul
        y += text_height + 5  # Espacio entre líneas

    img_filename = f"page_number_{number_text.replace(' ', '_')}.png"
    img_path = os.path.join(output_dir, img_filename)
    img.save(img_path)
    return img_path

# Procesar cada página del PDF
for i, page in enumerate(doc, start=1):
    page_number_text = f"{i}\n{num2words(i, lang='es')}"  # Ejemplo: "1\nuno"
    img_path = create_number_image(page_number_text)

    # Insertar la imagen en la esquina superior derecha de la página
    rect = fitz.Rect(495, 0, 595, 50)  # Ajusta según tamaño del texto o la imagen
    page.insert_image(rect, filename=img_path)

# Guardar el PDF modificado
output_pdf_path = "expediente_numbered.pdf"
doc.save(output_pdf_path)
doc.close()

print(f"✅ PDF guardado como {output_pdf_path}")
