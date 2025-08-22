#!/usr/bin/env python3
"""
Favicon Generator Tool
======================

Tool untuk mengonversi gambar menjadi favicon dalam berbagai format dan ukuran.
Mendukung format ICO dan PNG dengan ukuran standar web.

Usage:
    python "favicon-generator.py" logo.png                    # Buat favicon.ico sederhana
    python "favicon-generator.py" logo.png -o my_icon.ico     # Custom output name
    python "favicon-generator.py" logo.png --web              # Buat semua format web
    python "favicon-generator.py" --sample                    # Buat sample image untuk testing

Author: GitHub Copilot
Date: August 2025
"""

import os
import sys
import argparse
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

try:
    from PIL import Image
except ImportError:
    print("❌ Pillow library tidak ditemukan!")
    print("📦 Install dengan: pip install Pillow")
    input("Press Enter untuk install Pillow secara otomatis...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image
    print("✅ Pillow berhasil diinstall!")


class FaviconGenerator:
    """Class untuk generate favicon dari gambar"""
    
    def __init__(self):
        self.standard_sizes = [256]  # Ukuran 256px untuk scale maksimal
        self.web_formats = {
            'favicon.ico': [(256, 256)],  # Ukuran 256px maksimal untuk ICO
            'favicon-32x32.png': [(32, 32)],
            'favicon-48x48.png': [(48, 48)],
            'favicon-64x64.png': [(64, 64)],
            'apple-touch-icon.png': [(180, 180)],
            'android-chrome-192x192.png': [(192, 192)],
            'android-chrome-512x512.png': [(512, 512)]
        }
    
    def create_favicon(self, input_path, output_path=None, sizes=None):
        """
        Mengonversi gambar menjadi favicon ICO
        
        Args:
            input_path (str): Path ke file gambar input
            output_path (str): Path untuk menyimpan favicon
            sizes (list): List ukuran favicon
        
        Returns:
            str: Path file yang dibuat, atau None jika gagal
        """
        if sizes is None:
            sizes = self.standard_sizes
            
        try:
            with Image.open(input_path) as img:
                print(f"📷 Memproses gambar: {input_path}")
                print(f"   - Format asli: {img.format}")
                print(f"   - Mode: {img.mode}")
                print(f"   - Ukuran: {img.size}")
                
                # Konversi ke RGBA jika perlu
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                    print("   - Dikonversi ke RGBA")
                
                # Tentukan output path
                if output_path is None:
                    input_file = Path(input_path)
                    output_path = input_file.parent / f"{input_file.stem}.ico"
                
                # Buat list gambar dengan berbagai ukuran
                icon_sizes = []
                for size in sizes:
                    resized = img.resize((size, size), Image.Resampling.LANCZOS)
                    icon_sizes.append(resized)
                
                # Simpan sebagai ICO file
                icon_sizes[0].save(
                    output_path,
                    format='ICO',
                    sizes=[(size, size) for size in sizes]
                )
                
                print(f"✅ Favicon berhasil dibuat: {output_path}")
                print(f"📏 Ukuran: {', '.join([f'{s}x{s}' for s in sizes])}")
                print(f"📦 Ukuran file: {os.path.getsize(output_path)} bytes")
                
                return str(output_path)
                
        except FileNotFoundError:
            print(f"❌ File {input_path} tidak ditemukan!")
            return None
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def create_web_favicons(self, input_path, output_dir=None):
        """
        Membuat favicon dalam semua format web standar
        
        Args:
            input_path (str): Path ke file gambar input
            output_dir (str): Directory untuk menyimpan hasil
        
        Returns:
            list: List file yang dibuat
        """
        try:
            with Image.open(input_path) as img:
                print(f"📷 Memproses gambar: {input_path}")
                print(f"   - Format: {img.format}, Mode: {img.mode}, Ukuran: {img.size}")
                
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                    print("   - Dikonversi ke RGBA")
                
                # Tentukan output directory
                input_file = Path(input_path)
                if output_dir is None:
                    output_dir = input_file.parent / "favicon_output"
                
                output_dir = Path(output_dir)
                output_dir.mkdir(exist_ok=True)
                print(f"📁 Output directory: {output_dir}")
                
                created_files = []
                total_size = 0
                
                for filename, sizes in self.web_formats.items():
                    print(f"🔄 Membuat {filename}...")
                    
                    if filename.endswith('.ico'):
                        # Untuk ICO, buat multiple sizes dalam satu file
                        icon_sizes = []
                        for width, height in sizes:
                            resized = img.resize((width, height), Image.Resampling.LANCZOS)
                            icon_sizes.append(resized)
                        
                        output_path = output_dir / filename
                        icon_sizes[0].save(
                            output_path,
                            format='ICO',
                            sizes=sizes
                        )
                        created_files.append(output_path)
                        file_size = os.path.getsize(output_path)
                        total_size += file_size
                        print(f"   ✅ {filename} ({file_size} bytes)")
                    else:
                        # Untuk PNG, buat file individual
                        for width, height in sizes:
                            resized = img.resize((width, height), Image.Resampling.LANCZOS)
                            output_path = output_dir / filename
                            resized.save(output_path, format='PNG', optimize=True)
                            created_files.append(output_path)
                            file_size = os.path.getsize(output_path)
                            total_size += file_size
                            print(f"   ✅ {filename} ({width}x{height}) - {file_size} bytes")
                
                print(f"\n✅ Semua favicon berhasil dibuat!")
                print(f"📁 Lokasi: {output_dir}")
                print(f"📦 Total ukuran: {total_size} bytes")
                print(f"📄 Jumlah file: {len(created_files)}")
                
                return created_files
                
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None
    
    def generate_html_code(self, favicon_dir):
        """
        Generate HTML code untuk menggunakan favicon
        
        Args:
            favicon_dir (str): Directory tempat favicon disimpan
        """
        html_code = '''<!-- Favicon HTML Tags - Copy paste ke dalam <head> section -->
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="icon" type="image/png" sizes="48x48" href="favicon-48x48.png">
<link rel="icon" type="image/png" sizes="64x64" href="favicon-64x64.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="android-chrome-192x192.png">
<link rel="icon" type="image/png" sizes="512x512" href="android-chrome-512x512.png">
<meta name="theme-color" content="#ffffff">'''
        
        print("\n📝 HTML code untuk favicon:")
        print("=" * 50)
        print(html_code)
        print("=" * 50)
        
        # Simpan ke file
        if favicon_dir:
            html_file = Path(favicon_dir) / "favicon_html.txt"
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_code)
            print(f"💾 HTML code disimpan di: {html_file}")
    
    def create_sample_image(self, output_path="sample_logo.png"):
        """
        Membuat sample image untuk testing
        
        Args:
            output_path (str): Path untuk menyimpan sample image
        
        Returns:
            str: Path file yang dibuat
        """
        print("🎨 Membuat sample image...")
        
        # Buat gambar sample dengan design menarik
        img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
        
        # Buat design gradient circular
        center_x, center_y = 256, 256
        max_radius = 200
        
        for x in range(512):
            for y in range(512):
                distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
                
                if distance <= max_radius:
                    # Gradient dari center ke edge
                    ratio = 1 - (distance / max_radius)
                    
                    # Warna gradient biru ke orange
                    red = int(255 * ratio * 0.8)
                    green = int(150 * ratio)
                    blue = int(255 * (1 - ratio * 0.3))
                    alpha = 255
                    
                    # Tambah efek lingkaran
                    if distance > max_radius * 0.8:
                        edge_ratio = (distance - max_radius * 0.8) / (max_radius * 0.2)
                        alpha = int(255 * (1 - edge_ratio))
                    
                    img.putpixel((x, y), (red, green, blue, alpha))
        
        img.save(output_path, format='PNG')
        file_size = os.path.getsize(output_path)
        print(f"✅ Sample image '{output_path}' berhasil dibuat ({file_size} bytes)")
        print(f"📏 Ukuran: 512x512 pixels")
        return output_path

    def select_image_file(self):
        """
        Membuka dialog untuk memilih file gambar
        
        Returns:
            str: Path file yang dipilih, atau None jika dibatalkan
        """
        # Sembunyikan root window
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        # File types yang didukung
        filetypes = [
            ('Semua format gambar', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.webp'),
            ('PNG files', '*.png'),
            ('JPEG files', '*.jpg *.jpeg'),
            ('GIF files', '*.gif'),
            ('BMP files', '*.bmp'),
            ('TIFF files', '*.tiff'),
            ('WebP files', '*.webp'),
            ('Semua files', '*.*')
        ]
        
        try:
            file_path = filedialog.askopenfilename(
                title="Pilih file gambar untuk dikonversi ke favicon",
                filetypes=filetypes,
                initialdir=os.getcwd()
            )
            
            if file_path:
                print(f"📁 File dipilih: {file_path}")
                return file_path
            else:
                print("❌ Tidak ada file yang dipilih")
                return None
                
        except Exception as e:
            print(f"❌ Error membuka file dialog: {e}")
            return None
        finally:
            root.destroy()

    def select_output_directory(self):
        """
        Membuka dialog untuk memilih directory output
        
        Returns:
            str: Path directory yang dipilih, atau None jika dibatalkan
        """
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        try:
            dir_path = filedialog.askdirectory(
                title="Pilih folder untuk menyimpan favicon",
                initialdir=os.getcwd()
            )
            
            if dir_path:
                print(f"📁 Directory dipilih: {dir_path}")
                return dir_path
            else:
                print("❌ Tidak ada directory yang dipilih")
                return None
                
        except Exception as e:
            print(f"❌ Error membuka directory dialog: {e}")
            return None
        finally:
            root.destroy()

    def interactive_mode(self):
        """
        Mode interaktif untuk penggunaan yang lebih mudah
        """
        print("🔧 Favicon Generator - Mode Interaktif")
        print("=" * 50)
        
        while True:
            print("\n📋 Pilih opsi:")
            print("1. Konversi gambar ke favicon sederhana (.ico)")
            print("2. Konversi gambar ke semua format web")
            print("3. Buat sample image untuk testing")
            print("4. Keluar")
            
            choice = input("\nPilihan Anda (1-4): ").strip()
            
            if choice == '1':
                print("\n🔍 Pilih file gambar...")
                image_path = self.select_image_file()
                if image_path and os.path.exists(image_path):
                    print("\n🎯 Pilih lokasi untuk menyimpan favicon (opsional)...")
                    output_dir = self.select_output_directory()
                    if output_dir:
                        output_path = os.path.join(output_dir, Path(image_path).stem + ".ico")
                    else:
                        output_path = None
                    self.create_favicon(image_path, output_path)
                elif image_path:
                    print("❌ File tidak ditemukan!")
                    
            elif choice == '2':
                print("\n🔍 Pilih file gambar...")
                image_path = self.select_image_file()
                if image_path and os.path.exists(image_path):
                    print("\n🎯 Pilih lokasi untuk menyimpan favicon...")
                    output_dir = self.select_output_directory()
                    files = self.create_web_favicons(image_path, output_dir)
                    if files:
                        self.generate_html_code(Path(files[0]).parent)
                elif image_path:
                    print("❌ File tidak ditemukan!")
                    
            elif choice == '3':
                print("\n🎯 Pilih lokasi untuk menyimpan sample image...")
                output_dir = self.select_output_directory()
                if output_dir:
                    sample_path = os.path.join(output_dir, "sample_logo.png")
                else:
                    sample_path = "sample_logo.png"
                self.create_sample_image(sample_path)
                
            elif choice == '4':
                print("👋 Terima kasih telah menggunakan Favicon Generator!")
                break
                
            else:
                print("❌ Pilihan tidak valid!")

    def gui_mode(self):
        """
        Mode GUI sederhana menggunakan tkinter
        """
        try:
            root = tk.Tk()
            root.title("🔧 Favicon Generator")
            root.geometry("500x350")
            root.resizable(False, False)
            
            # Style
            root.configure(bg='#f0f0f0')
            
            # Header
            header = tk.Label(root, text="🔧 Favicon Generator", 
                            font=('Arial', 16, 'bold'), 
                            bg='#f0f0f0', fg='#333')
            header.pack(pady=20)
            
            # Description
            desc = tk.Label(root, text="Konversi gambar menjadi favicon untuk website Anda", 
                          font=('Arial', 10), bg='#f0f0f0', fg='#666')
            desc.pack(pady=5)
            
            # Selected file label
            self.selected_file_label = tk.Label(root, text="Belum ada file dipilih", 
                                              font=('Arial', 9), bg='#f0f0f0', fg='#999')
            self.selected_file_label.pack(pady=10)
            
            # Button frame
            button_frame = tk.Frame(root, bg='#f0f0f0')
            button_frame.pack(pady=20)
            
            # Select file button
            select_btn = tk.Button(button_frame, text="📁 Pilih File Gambar", 
                                 command=self.gui_select_file,
                                 font=('Arial', 10, 'bold'),
                                 bg='#4CAF50', fg='white',
                                 padx=20, pady=10)
            select_btn.pack(side=tk.LEFT, padx=10)
            
            # Convert buttons frame
            convert_frame = tk.Frame(root, bg='#f0f0f0')
            convert_frame.pack(pady=10)
            
            # Simple convert button
            simple_btn = tk.Button(convert_frame, text="🔄 Buat Favicon ICO", 
                                 command=self.gui_convert_simple,
                                 font=('Arial', 9),
                                 bg='#2196F3', fg='white',
                                 padx=15, pady=8)
            simple_btn.pack(side=tk.LEFT, padx=5)
            
            # Web convert button
            web_btn = tk.Button(convert_frame, text="🌐 Buat Semua Format Web", 
                              command=self.gui_convert_web,
                              font=('Arial', 9),
                              bg='#FF9800', fg='white',
                              padx=15, pady=8)
            web_btn.pack(side=tk.LEFT, padx=5)
            
            # Sample button
            sample_btn = tk.Button(root, text="🎨 Buat Sample Image", 
                                 command=self.gui_create_sample,
                                 font=('Arial', 9),
                                 bg='#9C27B0', fg='white',
                                 padx=15, pady=8)
            sample_btn.pack(pady=10)
            
            # Output text
            output_frame = tk.Frame(root, bg='#f0f0f0')
            output_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            
            self.output_text = tk.Text(output_frame, height=8, font=('Consolas', 8))
            scrollbar = tk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.output_text.yview)
            self.output_text.configure(yscrollcommand=scrollbar.set)
            
            self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            self.selected_file = None
            
            # Redirect print to text widget
            import sys
            sys.stdout = self
            
            self.output_text.insert(tk.END, "✅ GUI Mode siap digunakan!\n")
            self.output_text.insert(tk.END, "💡 Pilih file gambar untuk memulai konversi.\n\n")
            
            root.mainloop()
            
        except Exception as e:
            print(f"❌ Error menjalankan GUI: {e}")
            print("💡 Gunakan mode interaktif sebagai alternatif")
    
    def write(self, text):
        """Redirect stdout ke text widget"""
        if hasattr(self, 'output_text'):
            self.output_text.insert(tk.END, text)
            self.output_text.see(tk.END)
    
    def flush(self):
        """Required for stdout redirect"""
        pass
    
    def gui_select_file(self):
        """Handler untuk button pilih file di GUI"""
        self.selected_file = self.select_image_file()
        if self.selected_file:
            filename = os.path.basename(self.selected_file)
            self.selected_file_label.config(text=f"📁 {filename}", fg='#4CAF50')
        else:
            self.selected_file_label.config(text="Belum ada file dipilih", fg='#999')
    
    def gui_convert_simple(self):
        """Handler untuk konversi sederhana di GUI"""
        if not self.selected_file:
            messagebox.showwarning("Peringatan", "Silakan pilih file gambar terlebih dahulu!")
            return
        
        output_dir = self.select_output_directory()
        if output_dir:
            output_path = os.path.join(output_dir, Path(self.selected_file).stem + ".ico")
        else:
            output_path = None
        
        result = self.create_favicon(self.selected_file, output_path)
        if result:
            messagebox.showinfo("Sukses", f"Favicon berhasil dibuat!\n{result}")
    
    def gui_convert_web(self):
        """Handler untuk konversi web di GUI"""
        if not self.selected_file:
            messagebox.showwarning("Peringatan", "Silakan pilih file gambar terlebih dahulu!")
            return
        
        output_dir = self.select_output_directory()
        files = self.create_web_favicons(self.selected_file, output_dir)
        if files:
            self.generate_html_code(Path(files[0]).parent)
            messagebox.showinfo("Sukses", f"Semua favicon berhasil dibuat!\nTotal file: {len(files)}")
    
    def gui_create_sample(self):
        """Handler untuk buat sample di GUI"""
        output_dir = self.select_output_directory()
        if output_dir:
            sample_path = os.path.join(output_dir, "sample_logo.png")
        else:
            sample_path = "sample_logo.png"
        
        result = self.create_sample_image(sample_path)
        if result:
            messagebox.showinfo("Sukses", f"Sample image berhasil dibuat!\n{result}")
            # Auto select the sample file
            self.selected_file = result
            filename = os.path.basename(result)
            self.selected_file_label.config(text=f"📁 {filename}", fg='#4CAF50')


def main():
    """Main function dengan command line interface"""
    parser = argparse.ArgumentParser(
        description='🔧 Favicon Generator - Konversi gambar ke favicon',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
📖 Contoh penggunaan:
  python "favicon-generator.py" logo.png                    # Buat favicon.ico sederhana
  python "favicon-generator.py" logo.png -o my_icon.ico     # Custom output name
  python "favicon-generator.py" logo.png --web              # Buat semua format web
  python "favicon-generator.py" logo.png --web -o favicons/ # Custom output directory
  python "favicon-generator.py" --sample                    # Buat sample image untuk testing
  python "favicon-generator.py" --interactive               # Mode interaktif (text-based)
  python "favicon-generator.py" --gui                       # Mode GUI (graphical interface)

💡 Tips:
  - Gunakan gambar PNG dengan background transparan
  - Resolusi minimal 256x256 untuk hasil terbaik
  - Format yang didukung: PNG, JPG, GIF, BMP, TIFF, WebP
  - Mode GUI paling mudah untuk pemula
  - Ukuran favicon diperbesar untuk visibilitas yang lebih baik
        '''
    )
    
    parser.add_argument('input', nargs='?', help='Path ke file gambar input')
    parser.add_argument('-o', '--output', help='Path output file atau directory')
    parser.add_argument('-s', '--sizes', nargs='+', type=int, default=[256],
                       help='Ukuran favicon (default: 256)')
    parser.add_argument('--web', action='store_true',
                       help='Buat semua format favicon untuk web')
    parser.add_argument('--sample', action='store_true',
                       help='Buat sample image untuk testing')
    parser.add_argument('--interactive', action='store_true',
                       help='Jalankan dalam mode interaktif')
    parser.add_argument('--gui', action='store_true',
                       help='Jalankan dalam mode GUI (graphical user interface)')
    
    args = parser.parse_args()
    
    print("🔧 Favicon Generator Tool v1.0")
    print("=" * 40)
    
    generator = FaviconGenerator()
    
    # Mode GUI
    if args.gui:
        generator.gui_mode()
        return
    
    # Mode interaktif
    if args.interactive:
        generator.interactive_mode()
        return
    
    # Jika diminta sample image
    if args.sample:
        sample_path = generator.create_sample_image()
        print(f"\n💡 Sekarang coba jalankan:")
        print(f'   python "favicon-generator.py" {sample_path} --web')
        return
    
    # Validasi input
    if not args.input:
        print("❌ Input file tidak diberikan!")
        print("💡 Jalankan dengan --gui untuk mode GUI yang mudah")
        print("💡 Jalankan dengan --interactive untuk mode interaktif")
        print("💡 Atau gunakan --sample untuk membuat contoh gambar")
        parser.print_help()
        return
    
    if not os.path.exists(args.input):
        print(f"❌ File {args.input} tidak ditemukan!")
        return
    
    print(f"🔄 Memproses: {args.input}")
    
    # Buat favicon
    if args.web:
        files = generator.create_web_favicons(args.input, args.output)
        if files:
            generator.generate_html_code(Path(files[0]).parent)
            print(f"\n🎉 Selesai! Semua file favicon telah dibuat.")
            print(f"📋 Copy HTML code di atas ke dalam <head> section website Anda.")
    else:
        result = generator.create_favicon(args.input, args.output, args.sizes)
        if result:
            print(f"\n🎉 Selesai! Favicon ICO telah dibuat.")
            print(f"💡 Untuk membuat semua format web, gunakan flag --web")


if __name__ == "__main__":
    main()