import pypdfium2 as pdfium
import os
from PIL import Image

pdf_filename = [f for f in os.listdir('.') if f.endswith('.pdf')][0]
pdf = pdfium.PdfDocument(pdf_filename)

# PDF page index is 0-based.
# PDF page 48 = index 47 (printed pp 84, 85)
# PDF page 49 = index 48 (printed pp 86, 87)
# PDF page 50 = index 49 (printed pp 88, 89)
# PDF page 51 = index 50 (printed pp 90, 91)
# PDF page 52 = index 51 (printed pp 92, 93)
# PDF page 53 = index 52 (printed pp 94, 95)
# PDF page 54 = index 53 (printed pp 96, 97)

for p_num in range(47, 54): # PDF pages 48 to 54
    im = pdf[p_num].render(scale=1.5).to_pil()
    im.save(f"page_images/page_{p_num+1:03d}.png")
    w, h = im.size
    # left page
    im.crop((0, 0, int(w*0.52), h)).save(f"recipe_crops/p{p_num+1:03d}_left.png")
    # right page
    im.crop((int(w*0.48), 0, w, h)).save(f"recipe_crops/p{p_num+1:03d}_right.png")

print("Rendered and cropped PDF pages 48 to 54 successfully.")
