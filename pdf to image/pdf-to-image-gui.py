import fitz  # PyMuPDF
import os
from tkinter import Tk, filedialog, messagebox, simpledialog, ttk, W, E, N, S, StringVar, BooleanVar, DoubleVar
from PIL import Image
import io
import threading
from datetime import datetime

class PDFToImageConverter:
    def __init__(self):
        self.root = Tk()
        self.root.title("PDF to Image Converter Pro")
        self.root.geometry("600x500")
        
        # Configure root grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(W, E, N, S))
        
        # Title
        title_label = ttk.Label(main_frame, text="PDF to Image Converter Pro", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # File selection
        ttk.Label(main_frame, text="File PDF:").grid(row=1, column=0, sticky=W, pady=5)
        self.file_var = StringVar()
        ttk.Entry(main_frame, textvariable=self.file_var, width=50, state="readonly").grid(row=1, column=1, padx=(10, 0), pady=5)
        ttk.Button(main_frame, text="Browse Files", command=self.browse_files).grid(row=2, column=1, sticky=W, padx=(10, 0), pady=5)
        
        # Output folder
        ttk.Label(main_frame, text="Output Folder:").grid(row=3, column=0, sticky=W, pady=5)
        self.output_var = StringVar()
        ttk.Entry(main_frame, textvariable=self.output_var, width=50, state="readonly").grid(row=3, column=1, padx=(10, 0), pady=5)
        ttk.Button(main_frame, text="Browse Folder", command=self.browse_output).grid(row=4, column=1, sticky=W, padx=(10, 0), pady=5)
        
        # Settings frame
        settings_frame = ttk.LabelFrame(main_frame, text="Pengaturan Konversi", padding="10")
        settings_frame.grid(row=5, column=0, columnspan=2, sticky=(W, E), pady=20)
        
        # Format selection
        ttk.Label(settings_frame, text="Format Output:").grid(row=0, column=0, sticky=W, pady=5)
        self.format_var = StringVar(value="PNG")
        format_combo = ttk.Combobox(settings_frame, textvariable=self.format_var, values=["PNG", "JPEG", "WEBP", "TIFF"], state="readonly")
        format_combo.grid(row=0, column=1, padx=(10, 0), pady=5, sticky=W)
        
        # DPI selection
        ttk.Label(settings_frame, text="Resolusi (DPI):").grid(row=1, column=0, sticky=W, pady=5)
        self.dpi_var = StringVar(value="150")
        dpi_combo = ttk.Combobox(settings_frame, textvariable=self.dpi_var, values=["72", "100", "150", "200", "300", "600"], state="readonly")
        dpi_combo.grid(row=1, column=1, padx=(10, 0), pady=5, sticky=W)
        
        # Quality selection (for JPEG/WEBP)
        ttk.Label(settings_frame, text="Kualitas (1-100):").grid(row=2, column=0, sticky=W, pady=5)
        self.quality_var = StringVar(value="85")
        quality_spin = ttk.Spinbox(settings_frame, from_=1, to=100, textvariable=self.quality_var, width=10)
        quality_spin.grid(row=2, column=1, padx=(10, 0), pady=5, sticky=W)
        
        # Page range
        ttk.Label(settings_frame, text="Range Halaman:").grid(row=3, column=0, sticky=W, pady=5)
        page_frame = ttk.Frame(settings_frame)
        page_frame.grid(row=3, column=1, padx=(10, 0), pady=5, sticky=W)
        
        self.page_all_var = BooleanVar(value=True)
        ttk.Radiobutton(page_frame, text="Semua", variable=self.page_all_var, value=True).pack(side="left")
        ttk.Radiobutton(page_frame, text="Range:", variable=self.page_all_var, value=False).pack(side="left", padx=(10, 0))
        
        self.page_start_var = StringVar(value="1")
        self.page_end_var = StringVar(value="1")
        ttk.Entry(page_frame, textvariable=self.page_start_var, width=5).pack(side="left", padx=(5, 0))
        ttk.Label(page_frame, text="to").pack(side="left", padx=5)
        ttk.Entry(page_frame, textvariable=self.page_end_var, width=5).pack(side="left")
        
        # Progress bar
        self.progress_var = DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=6, column=0, columnspan=2, sticky=(W, E), pady=20)
        
        # Status label
        self.status_var = StringVar(value="Siap untuk konversi...")
        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=7, column=0, columnspan=2, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)
        
        self.convert_btn = ttk.Button(button_frame, text="Mulai Konversi", command=self.start_conversion)
        self.convert_btn.pack(side="left", padx=(0, 10))
        
        ttk.Button(button_frame, text="Keluar", command=self.root.quit).pack(side="left")
        
        # File list
        self.selected_files = []
        
    def browse_files(self):
        files = filedialog.askopenfilenames(
            title="Pilih file PDF",
            filetypes=[("PDF files", "*.pdf")]
        )
        if files:
            self.selected_files = list(files)
            if len(files) == 1:
                self.file_var.set(os.path.basename(files[0]))
            else:
                self.file_var.set(f"{len(files)} files selected")
    
    def browse_output(self):
        folder = filedialog.askdirectory(title="Pilih folder output")
        if folder:
            self.output_var.set(folder)
    
    def convert_pdf_to_images(self, pdf_path, output_folder, settings, progress_callback=None):
        """Convert PDF to images with progress callback"""
        doc = fitz.open(pdf_path)
        base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # Create output subfolder
        pdf_output_folder = os.path.join(output_folder, f"{base_filename}_images")
        os.makedirs(pdf_output_folder, exist_ok=True)
        
        # Determine page range
        total_pages = len(doc)
        if settings['page_all']:
            start_page = 0
            end_page = total_pages
        else:
            start_page = max(0, settings['page_start'] - 1)
            end_page = min(total_pages, settings['page_end'])
        
        converted_files = []
        pages_to_convert = end_page - start_page
        
        for i, page_num in enumerate(range(start_page, end_page)):
            page = doc[page_num]
            
            # Calculate matrix for DPI
            zoom = settings['dpi'] / 72.0
            mat = fitz.Matrix(zoom, zoom)
            
            # Get page as pixmap
            pix = page.get_pixmap(matrix=mat)
            
            # Create filename
            if pages_to_convert == 1:
                filename = f"{base_filename}.{settings['format'].lower()}"
            else:
                filename = f"{base_filename}_page_{page_num + 1:03d}.{settings['format'].lower()}"
            
            output_path = os.path.join(pdf_output_folder, filename)
            
            # Save image
            if settings['format'].upper() in ['JPEG', 'WEBP']:
                # Use PIL for better quality control
                img_data = pix.tobytes("ppm")
                pil_image = Image.open(io.BytesIO(img_data))
                if pil_image.mode != 'RGB' and settings['format'].upper() == 'JPEG':
                    pil_image = pil_image.convert('RGB')
                pil_image.save(output_path, format=settings['format'], quality=settings['quality'], optimize=True)
            else:
                # Use PyMuPDF directly
                pix.save(output_path)
            
            converted_files.append(output_path)
            
            # Update progress
            if progress_callback:
                progress = ((i + 1) / pages_to_convert) * 100
                progress_callback(progress, f"Converting page {page_num + 1} of {base_filename}")
        
        doc.close()
        return converted_files, pdf_output_folder
    
    def start_conversion(self):
        if not self.selected_files:
            messagebox.showerror("Error", "Pilih file PDF terlebih dahulu!")
            return
        
        if not self.output_var.get():
            messagebox.showerror("Error", "Pilih folder output terlebih dahulu!")
            return
        
        # Disable convert button
        self.convert_btn.config(state="disabled")
        
        # Get settings
        settings = {
            'format': self.format_var.get(),
            'dpi': int(self.dpi_var.get()),
            'quality': int(self.quality_var.get()),
            'page_all': self.page_all_var.get(),
            'page_start': int(self.page_start_var.get()) if self.page_start_var.get().isdigit() else 1,
            'page_end': int(self.page_end_var.get()) if self.page_end_var.get().isdigit() else 1
        }
        
        # Start conversion in separate thread
        thread = threading.Thread(target=self.convert_files, args=(settings,))
        thread.daemon = True
        thread.start()
    
    def convert_files(self, settings):
        total_files = len(self.selected_files)
        total_converted = 0
        total_size = 0
        
        for i, pdf_path in enumerate(self.selected_files):
            try:
                # Update status
                self.status_var.set(f"Processing {os.path.basename(pdf_path)}...")
                
                def progress_callback(page_progress, message):
                    file_progress = (i / total_files) * 100
                    overall_progress = file_progress + (page_progress / total_files)
                    self.progress_var.set(overall_progress)
                    self.status_var.set(message)
                
                converted_files, output_folder = self.convert_pdf_to_images(
                    pdf_path, 
                    self.output_var.get(), 
                    settings, 
                    progress_callback
                )
                
                # Calculate size
                folder_size = sum(os.path.getsize(f) for f in converted_files)
                total_size += folder_size
                total_converted += len(converted_files)
                
            except Exception as e:
                messagebox.showerror("Error", f"Error processing {os.path.basename(pdf_path)}: {str(e)}")
        
        # Conversion complete
        self.progress_var.set(100)
        self.status_var.set(f"Selesai! {total_converted} gambar dibuat ({total_size/1024/1024:.1f} MB)")
        self.convert_btn.config(state="normal")
        
        messagebox.showinfo("Selesai", f"Konversi selesai!\n\n"
                           f"Total gambar: {total_converted}\n"
                           f"Total ukuran: {total_size/1024/1024:.1f} MB\n"
                           f"Lokasi: {self.output_var.get()}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PDFToImageConverter()
    app.run()
