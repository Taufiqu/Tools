import fitz  # PyMuPDF
import os
from tkinter import Tk, filedialog
from PIL import Image
import io

def pdf_to_images_batch(input_path, output_folder, image_format="PNG", dpi=150):
    """
    Simple batch converter for PDF to images
    """
    doc = fitz.open(input_path)
    base_filename = os.path.splitext(os.path.basename(input_path))[0]
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    converted_files = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Calculate matrix for DPI
        zoom = dpi / 72.0
        mat = fitz.Matrix(zoom, zoom)
        
        # Get page as pixmap
        pix = page.get_pixmap(matrix=mat)
        
        # Create output filename
        if len(doc) == 1:
            # Single page PDF
            page_filename = f"{base_filename}.{image_format.lower()}"
        else:
            # Multi-page PDF
            page_filename = f"{base_filename}_page_{page_num + 1:03d}.{image_format.lower()}"
        
        output_path = os.path.join(output_folder, page_filename)
        
        # Save directly using PyMuPDF
        if image_format.upper() == "PNG":
            pix.save(output_path)
        elif image_format.upper() == "JPEG":
            # For JPEG, convert via PIL for better quality control
            img_data = pix.tobytes("ppm")
            pil_image = Image.open(io.BytesIO(img_data))
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            pil_image.save(output_path, format="JPEG", quality=85, optimize=True)
        else:
            pix.save(output_path)
        
        converted_files.append(output_path)
    
    doc.close()
    return converted_files

# GUI file picker (multi-file)
root = Tk()
root.withdraw()
input_pdfs = filedialog.askopenfilenames(title="Pilih PDF untuk dikonversi ke gambar", filetypes=[("PDF files", "*.pdf")])

if input_pdfs:
    # Ask for output directory
    output_dir = filedialog.askdirectory(title="Pilih folder untuk menyimpan gambar")
    
    if output_dir:
        print("🖼️  PDF to Image Converter (Simple)")
        print("=" * 40)
        
        total_converted = 0
        
        for input_pdf in input_pdfs:
            pdf_name = os.path.splitext(os.path.basename(input_pdf))[0]
            pdf_output_folder = os.path.join(output_dir, f"{pdf_name}_images")
            
            print(f"Proses: {os.path.basename(input_pdf)}")
            
            try:
                converted_files = pdf_to_images_batch(
                    input_pdf, 
                    pdf_output_folder, 
                    image_format="PNG",  # Change to "JPEG" if you prefer
                    dpi=150  # Change DPI as needed
                )
                
                total_converted += len(converted_files)
                
                # Calculate folder size
                folder_size = sum(os.path.getsize(f) for f in converted_files)
                
                print(f"✅ Berhasil: {len(converted_files)} halaman ➡ {pdf_output_folder}")
                print(f"   📊 Ukuran: {folder_size/1024/1024:.1f} MB")
                
            except Exception as e:
                print(f"❌ Error pada {os.path.basename(input_pdf)}: {e}")
        
        print(f"\n🎉 Total {total_converted} gambar berhasil dibuat!")
        print(f"📂 Lokasi: {output_dir}")
    else:
        print("❌ Folder output tidak dipilih!")
else:
    print("Lu gak milih file apapun, ngapain nanya wkwk.")
