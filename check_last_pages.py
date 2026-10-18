import pypdfium2 as pdfium

import os
pdf_filename = [f for f in os.listdir('.') if f.endswith('.pdf')][0]
pdf = pdfium.PdfDocument(pdf_filename)
print("Total PDF pages:", len(pdf))

# Render last 5 pages: 105, 106, 107, 108, 109
for p_idx in [104, 105, 106, 107, 108]:
    page = pdf[p_idx]
    image = page.render(scale=1.5).to_pil()
    image.save(f"page_images/page_{p_idx+1:03d}.png")
    print(f"Rendered PDF page {p_idx+1}")
