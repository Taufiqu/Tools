@echo off
title PDF to Image Converter
echo ================================================
echo         PDF TO IMAGE CONVERTER
echo ================================================
echo.
echo Tool untuk mengonversi PDF menjadi gambar (PNG, JPEG, WEBP, TIFF)
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
echo Pilih versi yang ingin dijalankan:
echo 1. GUI Version (Recommended) - Interface lengkap dengan pengaturan
echo 2. Simple Version - Langsung convert ke PNG
echo 3. Basic Version - Versi dasar
echo.
set /p choice="Pilih (1/2/3): "

REM Check if Python files exist
if "%choice%"=="1" (
    if not exist "pdf-to-image-gui.py" (
        echo ERROR: File "pdf-to-image-gui.py" tidak ditemukan!
        pause
        exit /b 1
    )
    echo Starting GUI version...
    python "pdf-to-image-gui.py"
) else if "%choice%"=="2" (
    if not exist "pdf-to-image-simple.py" (
        echo ERROR: File "pdf-to-image-simple.py" tidak ditemukan!
        pause
        exit /b 1
    )
    echo Starting Simple version...
    python "pdf-to-image-simple.py"
) else if "%choice%"=="3" (
    if not exist "pdf-to-image.py" (
        echo ERROR: File "pdf-to-image.py" tidak ditemukan!
        pause
        exit /b 1
    )
    echo Starting Basic version...
    python "pdf-to-image.py"
) else (
    if not exist "pdf-to-image-gui.py" (
        echo ERROR: File "pdf-to-image-gui.py" tidak ditemukan!
        pause
        exit /b 1
    )
    echo Pilihan tidak valid. Starting GUI version...
    python "pdf-to-image-gui.py"
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
