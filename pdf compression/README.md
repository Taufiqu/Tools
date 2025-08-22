# PDF Compression Tool

Tool untuk mengompress file PDF dengan mengurangi kualitas gambar untuk mengurangi ukuran file.

## Fitur
- Kompresi PDF dengan mengoptimalkan gambar
- Pengaturan kualitas kompresi (default: 60%)
- Mempertahankan teks asli
- Interface file picker yang mudah digunakan

## Cara Menggunakan

### Menggunakan File Batch (Termudah)
1. Double-click file `run.bat`
2. Program akan otomatis menginstall dependencies jika belum ada
3. Dialog akan muncul untuk memilih file PDF
4. Pilih file PDF yang ingin dikompress
5. File hasil akan disimpan dengan suffix `_compressed`

### Menggunakan Command Line
```batch
python "kompres-pdf-gambar.py"
```

## Dependencies
- Python 3.x
- PyMuPDF (fitz) - akan diinstall otomatis
- Pillow (PIL) - akan diinstall otomatis
- tkinter - biasanya sudah included di Python

## Output
File baru: `[nama_file_asli]_compressed.pdf`

## Contoh
Jika file asli: `dokumen_besar.pdf` (10 MB)
Output: `dokumen_besar_compressed.pdf` (±3-5 MB)

## Pengaturan Kompresi
Secara default menggunakan kualitas 60% yang memberikan keseimbangan baik antara:
- Ukuran file yang signifikan lebih kecil
- Kualitas gambar yang masih dapat diterima

## Tips
- Tool ini paling efektif untuk PDF yang banyak mengandung gambar
- PDF yang hanya berisi teks tidak akan banyak berkurang ukurannya
- Backup file asli sebelum kompresi untuk berjaga-jaga
- Cek kualitas hasil sebelum menghapus file asli
