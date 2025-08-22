import fitz  # PyMuPDF
import os
from tkinter import Tk, filedialog, messagebox, simpledialog
from PIL import Image
import io

def convert_pdf_to_images(input_path, output_folder, image_format="PNG", dpi=150, quality=95):
    """
    Convert PDF pages to images
    
    Args:
        input_path: Path to input PDF file
        output_folder: Folder to save converted images
        image_format: Output format (PNG, JPEG, WEBP, etc.)
        dpi: Resolution for conversion (higher = better quality, larger file)
        quality: JPEG quality (1-100, only for JPEG format)
    """
    doc = fitz.open(input_path)
    base_filename = os.path.splitext(os.path.basename(input_path))[0]
    
    converted_files = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Calculate matrix for DPI
        zoom = dpi / 72.0  # 72 is default DPI
        mat = fitz.Matrix(zoom, zoom)
        
        # Get page as pixmap (image)
        pix = page.get_pixmap(matrix=mat)
        
        # Convert to PIL Image
        img_data = pix.tobytes("ppm")
        pil_image = Image.open(io.BytesIO(img_data))
        
        # Create output filename
        page_filename = f"{base_filename}_page_{page_num + 1:03d}.{image_format.lower()}"
        output_path = os.path.join(output_folder, page_filename)
        
        # Save image with appropriate settings
        if image_format.upper() == "JPEG":
            # Convert to RGB for JPEG
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            pil_image.save(output_path, format=image_format, quality=quality, optimize=True)
        elif image_format.upper() == "PNG":
            pil_image.save(output_path, format=image_format, optimize=True)
        elif image_format.upper() == "WEBP":
            pil_image.save(output_path, format=image_format, quality=quality, optimize=True)
        else:
            pil_image.save(output_path, format=image_format)
        
        converted_files.append(output_path)
        print(f"   📄 Halaman {page_num + 1} ➡ {page_filename}")
    
    doc.close()
    return converted_files

def get_user_preferences():
    """
    Get user preferences for conversion settings
    """
    root = Tk()
    root.withdraw()
    
    # Ask for image format
    format_choice = messagebox.askyesnocancel(
        "Format Gambar", 
        "Pilih format output:\n\n"
        "YES = PNG (kualitas terbaik, file besar)\n"
        "NO = JPEG (kualitas bagus, file kecil)\n"
        "CANCEL = WEBP (modern, kompresi bagus)"
    )
    
    if format_choice is True:
        image_format = "PNG"
        quality = 95  # Not used for PNG
    elif format_choice is False:
        image_format = "JPEG"
        # Ask for JPEG quality
        quality = simpledialog.askinteger(
            "Kualitas JPEG", 
            "Masukkan kualitas JPEG (1-100):\n95 = Sangat Tinggi\n85 = Tinggi\n75 = Sedang\n60 = Rendah",
            initialvalue=85,
            minvalue=1,
            maxvalue=100
        )
        if quality is None:
            quality = 85
    else:
        image_format = "WEBP"
        # Ask for WebP quality
        quality = simpledialog.askinteger(
            "Kualitas WebP", 
            "Masukkan kualitas WebP (1-100):\n95 = Sangat Tinggi\n85 = Tinggi\n75 = Sedang\n60 = Rendah",
            initialvalue=85,
            minvalue=1,
            maxvalue=100
        )
        if quality is None:
            quality = 85
    
    # Ask for DPI
    dpi = simpledialog.askinteger(
        "Resolusi (DPI)", 
        "Masukkan resolusi DPI:\n300 = Print Quality (sangat tinggi)\n150 = Screen Quality (tinggi)\n100 = Web Quality (sedang)\n72 = Low Quality (rendah)",
        initialvalue=150,
        minvalue=50,
        maxvalue=600
    )
    if dpi is None:
        dpi = 150
    
    root.destroy()
    return image_format, quality, dpi

def main():
    print("🖼️  PDF to Image Converter")
    print("=" * 40)
    
    # Get user preferences
    try:
        image_format, quality, dpi = get_user_preferences()
        print(f"⚙️  Pengaturan: Format={image_format}, Quality={quality}, DPI={dpi}")
    except:
        print("❌ Proses dibatalkan oleh user")
        return
    
    # GUI file picker (multi-file)
    root = Tk()
    root.withdraw()
    input_pdfs = filedialog.askopenfilenames(
        title="Pilih PDF yang mau dikonversi ke gambar (multi)", 
        filetypes=[("PDF files", "*.pdf")]
    )
    
    if not input_pdfs:
        print("Lu gak milih file apapun, ngapain nanya wkwk.")
        return
    
    # Ask for output folder
    output_base_folder = filedialog.askdirectory(title="Pilih folder untuk menyimpan gambar")
    if not output_base_folder:
        print("❌ Folder output tidak dipilih!")
        return
    
    total_converted = 0
    total_size = 0
    
    for input_pdf in input_pdfs:
        pdf_name = os.path.splitext(os.path.basename(input_pdf))[0]
        
        # Create subfolder for each PDF
        pdf_output_folder = os.path.join(output_base_folder, f"{pdf_name}_images")
        os.makedirs(pdf_output_folder, exist_ok=True)
        
        print(f"\n📁 Proses: {os.path.basename(input_pdf)}")
        print(f"   💾 Output: {pdf_output_folder}")
        
        try:
            converted_files = convert_pdf_to_images(
                input_pdf, 
                pdf_output_folder, 
                image_format=image_format,
                dpi=dpi,
                quality=quality
            )
            
            # Calculate total size of converted images
            folder_size = sum(os.path.getsize(f) for f in converted_files)
            total_size += folder_size
            total_converted += len(converted_files)
            
            print(f"   ✅ Berhasil: {len(converted_files)} halaman dikonversi")
            print(f"   📊 Total ukuran: {folder_size/1024/1024:.1f} MB")
            
        except Exception as e:
            print(f"   ❌ Error pada {os.path.basename(input_pdf)}: {e}")
    
    print(f"\n🎉 Konversi selesai!")
    print(f"📈 Total: {total_converted} gambar dibuat")
    print(f"💾 Total ukuran: {total_size/1024/1024:.1f} MB")
    print(f"📂 Lokasi: {output_base_folder}")

if __name__ == "__main__":
    main()
