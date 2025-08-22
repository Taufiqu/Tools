@echo off
title Favicon Generator Tool
echo ================================================
echo          FAVICON GENERATOR TOOL
echo ================================================
echo.
echo Tool untuk mengonversi gambar menjadi favicon
echo Format yang didukung: PNG, JPG, GIF, BMP, TIFF, WebP
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python tidak ditemukan!
    echo Silakan install Python terlebih dahulu.
    pause
    exit /b 1
)

REM Install required packages if needed
echo Checking dependencies...
python -c "import PIL" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing Pillow...
    python -m pip install Pillow
)

python -c "import tkinter" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing tkinter...
    python -m pip install tk
)

REM Check if Python file exists
if not exist "favicon-generator.py" (
    echo ERROR: File "favicon-generator.py" tidak ditemukan!
    echo Pastikan file berada di folder yang sama dengan run.bat
    pause
    exit /b 1
)

echo.
echo Pilih mode yang ingin digunakan:
echo 1. GUI Mode (Recommended) - Interface grafis yang mudah
echo 2. Interactive Mode - Mode interaktif text-based
echo 3. Sample Mode - Buat sample image untuk testing
echo 4. Help - Lihat bantuan dan contoh penggunaan
echo.
set /p choice="Pilih mode (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting GUI Mode...
    echo Interface grafis akan terbuka...
    python "favicon-generator.py" --gui
) else if "%choice%"=="2" (
    echo.
    echo Starting Interactive Mode...
    python "favicon-generator.py" --interactive
) else if "%choice%"=="3" (
    echo.
    echo Starting Sample Mode...
    echo Membuat sample image untuk testing...
    python "favicon-generator.py" --sample
) else if "%choice%"=="4" (
    echo.
    echo Menampilkan bantuan...
    python "favicon-generator.py" --help
    echo.
    echo ================================================
    echo           CONTOH PENGGUNAAN
    echo ================================================
    echo Command Line Mode:
    echo   python "favicon-generator.py" logo.png
    echo   python "favicon-generator.py" logo.png --web
    echo   python "favicon-generator.py" logo.png -o my_icon.ico
    echo.
) else (
    echo.
    echo Pilihan tidak valid! Starting GUI Mode...
    python "favicon-generator.py" --gui
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Terjadi kesalahan saat menjalankan program.
    pause
    exit /b 1
)

echo.
echo Program selesai!
pause
