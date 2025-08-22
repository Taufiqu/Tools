# PDF & Image Tools Collection

Kumpulan tools Python untuk memproses PDF dan gambar dengan mudah.

## 📁 Tools yang Tersedia

### 1. **Favicon Generator**
- **Lokasi**: `favicon generator/`
- **Fungsi**: Mengonversi gambar menjadi favicon dalam berbagai format
- **Run**: `favicon generator/run.bat` atau `run_tools.bat` → pilih 1

### 2. **PDF Splitter** 
- **Lokasi**: `fragmentation pdf/`
- **Fungsi**: Memecah file PDF besar menjadi halaman-halaman terpisah
- **Run**: `fragmentation pdf/run.bat` atau `run_tools.bat` → pilih 2

### 3. **PDF Compressor**
- **Lokasi**: `pdf compression/`
- **Fungsi**: Mengompress PDF dengan mengurangi kualitas gambar
- **Run**: `pdf compression/run.bat` atau `run_tools.bat` → pilih 3

### 4. **PDF to Image Converter**
- **Lokasi**: `pdf to image/`
- **Fungsi**: Mengonversi PDF menjadi gambar (PNG, JPEG, WEBP, TIFF)
- **Run**: `pdf to image/run.bat` atau `run_tools.bat` → pilih 4

## 🚀 Cara Menggunakan

### Opsi 1: Menu Utama (Recommended)
1. Double-click `run_tools.bat` di folder utama
2. Pilih tool yang ingin digunakan (1-4)
3. Ikuti instruksi yang muncul

### Opsi 2: Langsung ke Tool
1. Masuk ke folder tool yang diinginkan
2. Double-click file `run.bat` di folder tersebut

## 📋 System Requirements

- **Windows** 7/8/10/11
- **Python 3.x** (akan dideteksi otomatis)
- **Internet connection** (untuk install dependencies pertama kali)

## 🔧 Dependencies

Semua dependencies akan diinstall otomatis saat pertama kali menjalankan tool:
- `Pillow` (PIL) - untuk processing gambar
- `PyMuPDF` (fitz) - untuk processing PDF
- `pypdf` - untuk manipulasi PDF
- `tkinter` - untuk GUI (biasanya sudah included)

## 📖 Documentation

Setiap folder tool memiliki `README.md` sendiri dengan dokumentasi lengkap:
- [Favicon Generator README](favicon%20generator/README.md)
- [PDF Splitter README](fragmentation%20pdf/README.md)  
- [PDF Compressor README](pdf%20compression/README.md)
- [PDF to Image README](pdf%20to%20image/README.md)

## ⚡ Quick Start

1. **Download/clone** repositori ini
2. **Double-click** `run_tools.bat`
3. **Pilih tool** yang ingin digunakan
4. **Done!** Dependencies akan diinstall otomatis

## 💡 Tips

- **Backup file asli** sebelum memproses (khususnya untuk compression)
- **Tutup file PDF** di aplikasi lain sebelum memproses
- **Gunakan gambar berkualitas tinggi** untuk favicon
- **Pilih DPI sesuai kebutuhan** untuk PDF to Image

## 🤝 Contributing

Feel free to contribute dengan:
- Menambah tools baru
- Improve existing tools
- Fix bugs
- Improve documentation

---

**Author**: GitHub Copilot  
**Date**: August 2025  
**Version**: 1.0
