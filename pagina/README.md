# 📄 Foliador de PDF con Python + Poetry

Este proyecto permite **foliar documentos PDF automáticamente**, agregando:

- Número de página
- Representación en texto (ej: `1 uno`, `2 dos`)
- Alineado a la **parte superior derecha**
- Fuente cursiva (Arial o Times New Roman)
- Color personalizable

---

## 🚀 Requisitos

- Python 3.11+
- Poetry instalado

Verificar instalación:

```bash
python --version
poetry --version
```

---

## 📦 Instalación del proyecto

### 1. Crear proyecto con Poetry

```bash
poetry new foliar_pdf
cd foliar_pdf
```

---

### 2. Agregar dependencias

```bash
poetry add pymupdf num2words
```

---

### 3. Activar entorno virtual (opcional)

```bash
poetry shell
```

---

## 📁 Estructura del proyecto

```text
foliar_pdf/
│
├── foliar.py
├── input.pdf
├── pyproject.toml
└── README.md
```

---

## 🧾 Código principal (`foliar.py`)

```python
import fitz  # PyMuPDF
from num2words import num2words

pdf_path = "input.pdf"
doc = fitz.open(pdf_path)

for i, page in enumerate(doc, start=1):
    width = page.rect.width

    text = f"{i}\n{num2words(i, lang='es')}"

    rect = fitz.Rect(width - 150, 10, width - 10, 60)

    page.insert_textbox(
        rect,
        text,
        fontsize=7,
        color=(0.4, 0, 0.4),  # morado oscuro
        fontfile=r"C:\Windows\Fonts\ariali.ttf",  # Arial cursiva
        align=2  # derecha
    )

output_pdf_path = "expediente_numbered.pdf"
doc.save(output_pdf_path)
doc.close()

print(f"PDF guardado como {output_pdf_path}")
```

---

## ▶️ Ejecución

### Opción 1 (recomendada)

```bash
poetry run python foliar.py
```

---

### Opción 2

```bash
poetry shell
python foliar.py
```

---

## 📤 Resultado

Se generará:

```text
expediente_numbered.pdf
```

Con numeración en cada página:

```text
1
uno

2
dos
```

Ubicada en la parte superior derecha.

---

## 🎨 Personalización

### Cambiar color

```python
color=(0.4, 0, 0.4)
```

---

### Cambiar fuente

Arial cursiva:
```python
fontfile=r"C:\Windows\Fonts\ariali.ttf"
```

Times New Roman cursiva:
```python
fontfile=r"C:\Windows\Fonts\timesi.ttf"
```

---

### Cambiar tamaño

```python
fontsize=7
```

---

### Ajustar posición

```python
rect = fitz.Rect(width - 150, 10, width - 10, 60)
```

---

## ⚠️ Problemas comunes

### ❌ ModuleNotFoundError

```bash
poetry run python foliar.py
```

---

### ❌ Error de fuente

Verificar que exista:

```text
C:\Windows\Fonts\ariali.ttf
```

---

### ❌ PDF no encontrado

Colocar `input.pdf` en la raíz del proyecto.

---

## 🧠 Buenas prácticas

- Usar `insert_textbox` para alineación correcta
- Probar con PDFs pequeños primero
- Mantener fuentes dentro del proyecto para portabilidad

---

## 🚀 Extensiones futuras

- Formato `Folio 001`
- Texto en mayúsculas (`UNO`)
- Procesamiento por lotes
- Interfaz web

---

## 👨‍💻 Autor

Herminio Paucar  
FISI - UNMSM
