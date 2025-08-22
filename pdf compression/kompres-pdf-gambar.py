import fitz  # PyMuPDF
import os
from tkinter import Tk, filedialog
from PIL import Image
import io

def compress_pdf(input_path, output_path, quality=60):
    """
    Compress PDF by reducing image quality and file size
    """
    input_doc = fitz.open(input_path)
    output_doc = fitz.open()  # Create new document
    
    for page_num in range(len(input_doc)):
        page = input_doc[page_num]
        
        # Get page as pixmap (image)
        mat = fitz.Matrix(1.0, 1.0)  # No scaling
        pix = page.get_pixmap(matrix=mat)
        
        # Convert to PIL Image for compression
        img_data = pix.tobytes("ppm")
        pil_image = Image.open(io.BytesIO(img_data))
        
        # Convert to RGB if needed
        if pil_image.mode != 'RGB':
            pil_image = pil_image.convert('RGB')
        
        # Compress the image
        compressed_buffer = io.BytesIO()
        pil_image.save(compressed_buffer, format='JPEG', quality=quality, optimize=True)
        compressed_data = compressed_buffer.getvalue()
        
        # Create new page in output document
        new_page = output_doc.new_page(width=page.rect.width, height=page.rect.height)
        
        # Insert compressed image as background
        new_page.insert_image(page.rect, stream=compressed_data)
        
        # Copy text content (if any)
        try:
            text_dict = page.get_text("dict")
            for block in text_dict["blocks"]:
                if "lines" in block:  # Text block
                    for line in block["lines"]:
                        for span in line["spans"]:
                            new_page.insert_text(
                                (span["bbox"][0], span["bbox"][1]), 
                                span["text"], 
                                fontsize=span["size"],
                                color=(0, 0, 0)
                            )
        except:
            pass  # Skip if text extraction fails
    
    # Save compressed document
    output_doc.save(output_path, garbage=4, deflate=True)
    output_doc.close()
    input_doc.close()

# GUI file picker (multi-file)
root = Tk()
root.withdraw()
input_pdfs = filedialog.askopenfilenames(title="Pilih PDF yang mau dikompres (multi)", filetypes=[("PDF files", "*.pdf")])

if input_pdfs:
    for input_pdf in input_pdfs:
        base = os.path.splitext(input_pdf)[0]
        output_pdf = base + "_compressed.pdf"
        print(f"Proses: {os.path.basename(input_pdf)} ➡ {os.path.basename(output_pdf)}")
        try:
            compress_pdf(input_pdf, output_pdf, quality=60)
            
            # Check file size reduction
            original_size = os.path.getsize(input_pdf)
            compressed_size = os.path.getsize(output_pdf)
            reduction = (1 - compressed_size/original_size) * 100
            
            print(f"✅ Berhasil: {os.path.basename(output_pdf)}")
            print(f"   📉 Ukuran: {original_size/1024:.1f}KB ➡ {compressed_size/1024:.1f}KB (hemat {reduction:.1f}%)")
            
        except Exception as e:
            print(f"❌ Error pada {os.path.basename(input_pdf)}: {e}")
    print("🎉 Proses kompresi selesai!")
else:
    print("Lu gak milih file apapun, ngapain nanya wkwk.")
