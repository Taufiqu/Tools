@echo off
title File Check Tool
echo ================================================
echo              FILE CHECK TOOL
echo ================================================
echo.
echo Checking semua file Python di setiap folder...
echo.

echo [1/4] Checking Favicon Generator...
cd "favicon generator"
if exist "favicon-generator.py" (
    echo   ✅ favicon-generator.py - FOUND
) else (
    echo   ❌ favicon-generator.py - NOT FOUND
)
cd ..

echo.
echo [2/4] Checking PDF Splitter...
cd "fragmentation pdf"
if exist "pecah-pdf.py" (
    echo   ✅ pecah-pdf.py - FOUND
) else (
    echo   ❌ pecah-pdf.py - NOT FOUND
)
cd ..

echo.
echo [3/4] Checking PDF Compressor...
cd "pdf compression"
if exist "kompres-pdf-gambar.py" (
    echo   ✅ kompres-pdf-gambar.py - FOUND
) else (
    echo   ❌ kompres-pdf-gambar.py - NOT FOUND
)
cd ..

echo.
echo [4/4] Checking PDF to Image...
cd "pdf to image"
if exist "pdf-to-image-gui.py" (
    echo   ✅ pdf-to-image-gui.py - FOUND
) else (
    echo   ❌ pdf-to-image-gui.py - NOT FOUND
)

if exist "pdf-to-image-simple.py" (
    echo   ✅ pdf-to-image-simple.py - FOUND
) else (
    echo   ❌ pdf-to-image-simple.py - NOT FOUND
)

if exist "pdf-to-image.py" (
    echo   ✅ pdf-to-image.py - FOUND
) else (
    echo   ❌ pdf-to-image.py - NOT FOUND
)
cd ..

echo.
echo ================================================
echo File check completed!
echo ================================================
pause
