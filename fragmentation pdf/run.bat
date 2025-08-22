@echo off
title PDF Splitter Tool
echo ================================================
echo            PDF SPLITTER TOOL
echo ================================================
echo.
echo Tool untuk memecah file PDF menjadi halaman terpisah
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
python -c "import pypdf" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing pypdf...
    python -m pip install pypdf
)

python -c "import tkinter" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing tkinter...
    python -m pip install tk
)

echo.
echo Starting PDF Splitter...
echo Silakan pilih file PDF yang ingin dipecah...
echo.

REM Check if Python file exists
if not exist "pecah-pdf.py" (
    echo ERROR: File "pecah-pdf.py" tidak ditemukan!
    echo Pastikan file berada di folder yang sama dengan run.bat
    pause
    exit /b 1
)

python "pecah-pdf.py"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Terjadi kesalahan saat menjalankan program.
    pause
    exit /b 1
)

echo.
echo Program selesai!
pause
