# PDF to Image Converter

Tool untuk mengonversi file PDF menjadi gambar dalam berbagai format (PNG, JPEG, WEBP, TIFF).

## Fitur
- Konversi PDF ke gambar dengan berbagai format
- 3 versi berbeda: GUI, Simple, dan Basic
- Pengaturan resolusi/DPI yang fleksibel
- Support batch conversion (semua halaman sekaligus)
- Preview hasil konversi
- Progress bar untuk file besar

## Versi yang Tersedia

### 1. GUI Version (`pdf-to-image-gui.py`) - **Recommended**
- Interface lengkap dengan pengaturan detail
- Pilihan format output: PNG, JPEG, WEBP, TIFF
- Pengaturan DPI: 72, 100, 150, 200, 300, 600
- Pilihan kualitas untuk JPEG
- Progress bar dan preview
- Paling user-friendly

### 2. Simple Version (`pdf-to-image-simple.py`)
- Langsung convert ke PNG dengan kualitas tinggi
- Minimal interface, maksimal hasil
- Cocok untuk penggunaan cepat

### 3. Basic Version (`pdf-to-image.py`)
- Versi paling sederhana
- Convert langsung tanpa banyak pengaturan

## Cara Menggunakan

### Menggunakan File Batch (Termudah)
1. Double-click file `run.bat`
2. Program akan otomatis menginstall dependencies jika belum ada
3. Pilih versi yang ingin digunakan (1/2/3)
4. Pilih file PDF yang ingin dikonversi
5. Gambar hasil akan disimpan di folder yang sama atau folder pilihan

### Menggunakan Command Line
```batch
# GUI Version
python "pdf-to-image-gui.py"

# Simple Version  
python "pdf-to-image-simple.py"

# Basic Version
python "pdf-to-image.py"
```

## Dependencies
- Python 3.x
- PyMuPDF (fitz) - akan diinstall otomatis
- Pillow (PIL) - akan diinstall otomatis
- tkinter - biasanya sudah included di Python

## Output
- Format: PNG, JPEG, WEBP, TIFF (tergantung pengaturan)
- Nama file: `page_1.png`, `page_2.png`, dst.
- Resolusi: Dapat diatur dari 72 DPI hingga 600 DPI

## Pengaturan Resolusi
- **72 DPI**: Web/screen viewing (file kecil)
- **150 DPI**: Dokumen standar (balanced)
- **300 DPI**: Print quality (file besar, kualitas tinggi)
- **600 DPI**: Professional printing (file sangat besar)

## Tips
- Gunakan PNG untuk dokumen dengan teks yang tajam
- Gunakan JPEG untuk dokumen dengan banyak foto/gambar
- DPI 150 adalah pilihan terbaik untuk kebanyakan keperluan
- Untuk file PDF besar, gunakan DPI rendah dulu untuk preview
- Format WEBP memberikan kompresi terbaik dengan kualitas bagus
