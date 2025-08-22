@echo off
title PDF & Image Tools Collection
color 0A

:menu
cls
echo ================================================
echo         PDF & IMAGE TOOLS COLLECTION
echo ================================================
echo.
echo Pilih tool yang ingin digunakan:
echo.
echo 1. Favicon Generator     - Convert gambar ke favicon
echo 2. PDF Splitter         - Pecah PDF jadi halaman terpisah  
echo 3. PDF Compressor       - Kompres PDF untuk ukuran lebih kecil
echo 4. PDF to Image         - Convert PDF ke gambar (PNG/JPEG/etc)
echo.
echo 0. Exit
echo.
set /p choice="Pilih nomor tool (0-4): "

if "%choice%"=="1" (
    echo.
    echo Starting Favicon Generator...
    cd "favicon generator"
    call run.bat
    cd ..
    goto menu
) else if "%choice%"=="2" (
    echo.
    echo Starting PDF Splitter...
    cd "fragmentation pdf"
    call run.bat
    cd ..
    goto menu
) else if "%choice%"=="3" (
    echo.
    echo Starting PDF Compressor...
    cd "pdf compression"
    call run.bat
    cd ..
    goto menu
) else if "%choice%"=="4" (
    echo.
    echo Starting PDF to Image Converter...
    cd "pdf to image"
    call run.bat
    cd ..
    goto menu
) else if "%choice%"=="0" (
    echo Goodbye!
    exit /b 0
) else (
    echo.
    echo Pilihan tidak valid! Silakan pilih nomor 0-4.
    echo.
    pause
    goto menu
)
