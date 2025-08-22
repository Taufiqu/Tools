# PDF Splitter Tool

Tool untuk memecah file PDF besar menjadi halaman-halaman terpisah.

## Fitur
- Memecah PDF menjadi file terpisah per halaman
- Interface file picker yang mudah digunakan
- Otomatis membuat folder output
- Support semua jenis file PDF

## Cara Menggunakan

### Menggunakan File Batch (Termudah)
1. Double-click file `run.bat`
2. Program akan otomatis menginstall dependencies jika belum ada
3. Dialog akan muncul untuk memilih file PDF
4. Pilih file PDF yang ingin dipecah
5. File hasil akan disimpan di folder baru dengan nama `[nama_file]_split`

### Menggunakan Command Line
```batch
python "pecah-pdf.py"
```

## Dependencies
- Python 3.x
- pypdf - akan diinstall otomatis
- tkinter - biasanya sudah included di Python

## Output
- Folder baru: `[nama_file_asli]_split`
- File per halaman: `output_page_1.pdf`, `output_page_2.pdf`, dst.

## Contoh
Jika file asli: `dokumen_besar.pdf` (50 halaman)
Output:
```
dokumen_besar_split/
├── output_page_1.pdf
├── output_page_2.pdf
├── ...
└── output_page_50.pdf
```

## Tips
- Pastikan file PDF tidak dalam keadaan terbuka di aplikasi lain
- File akan disimpan di lokasi yang sama dengan file asli
- Proses bisa memakan waktu untuk file PDF yang sangat besar
