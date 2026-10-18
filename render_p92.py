import pypdfium2 as pdfium
import os
from PIL import Image

pdf_filename = [f for f in os.listdir('.') if f.endswith('.pdf')][0]
pdf = pdfium.PdfDocument(pdf_filename)

im = pdf[91].render(scale=1.5).to_pil() # PDF page 92 (0-indexed 91)
im.save("recipe_crops/page_092.png")
w, h = im.size
im.crop((0, 0, int(w*0.52), h)).save("recipe_crops/p92_left.png")
im.crop((int(w*0.48), 0, w, h)).save("recipe_crops/p92_right.png")
print("Rendered PDF page 92.")
