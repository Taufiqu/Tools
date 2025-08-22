@echo off
title PDF Compression Tool
echo ================================================
echo           PDF COMPRESSION TOOL
echo ================================================
echo.
echo Tool untuk mengompress PDF dengan mengurangi kualitas gambar
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
python -c "import fitz" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing PyMuPDF...
    python -m pip install PyMuPDF
)

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

echo.
echo Starting PDF Compressor...
echo Silakan pilih file PDF yang ingin dikompress...
echo.

REM Check if Python file exists
if not exist "kompres-pdf-gambar.py" (
    echo ERROR: File "kompres-pdf-gambar.py" tidak ditemukan!
    echo Pastikan file berada di folder yang sama dengan run.bat
    pause
    exit /b 1
)

python "kompres-pdf-gambar.py"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Terjadi kesalahan saat menjalankan program.
    pause
    exit /b 1
)

echo.
echo Program selesai!
pause
