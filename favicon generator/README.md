# Favicon Generator Tool

Tool untuk mengonversi gambar menjadi favicon dalam berbagai format dan ukuran.

## Fitur
- Konversi gambar ke format ICO
- Generate favicon untuk web (berbagai ukuran)
- Support format PNG, JPG, BMP
- Interface GUI yang mudah digunakan

## Cara Menggunakan

### Menggunakan File Batch (Termudah)
1. Double-click file `run.bat`
2. Program akan otomatis menginstall dependencies jika belum ada
3. Pilih file gambar yang ingin dikonversi
4. Favicon akan otomatis dibuat

### Menggunakan Command Line
```batch
# Buat favicon sederhana
python "favicon generator.py" logo.png

# Custom output name
python "favicon generator.py" logo.png -o my_icon.ico

# Buat semua format web
python "favicon generator.py" logo.png --web

# Buat sample image untuk testing
python "favicon generator.py" --sample
```

## Dependencies
- Python 3.x
- Pillow (PIL) - akan diinstall otomatis

## Output
- `favicon.ico` - Icon standar 256x256px
- `favicon-32x32.png` - Icon untuk browser modern
- `apple-touch-icon.png` - Icon untuk iOS
- `android-chrome-*.png` - Icon untuk Android

## Tips
- Gunakan gambar dengan resolusi tinggi untuk hasil terbaik
- Format PNG atau SVG memberikan hasil paling bagus
- Gambar berbentuk persegi (1:1 ratio) paling ideal
