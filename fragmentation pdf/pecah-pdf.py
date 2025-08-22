import os
from tkinter import Tk, filedialog
from pypdf import PdfReader, PdfWriter

# Biar gak muncul jendela Tk kosong
root = Tk()
root.withdraw()

# Munculin file picker
file_path = filedialog.askopenfilename(title="Pilih file PDF gede lu", filetypes=[("PDF files", "*.pdf")])

if not file_path:
    print("Gak jadi milih file.")
else:
    try:
        reader = PdfReader(file_path)
        output_dir = os.path.splitext(file_path)[0] + "_split"
        os.makedirs(output_dir, exist_ok=True)

        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            output_file = os.path.join(output_dir, f"output_page_{i+1}.pdf")
            with open(output_file, "wb") as f:
                writer.write(f)

        print(f"File berhasil di-split ke folder: {output_dir}")
    except Exception as e:
        print(f"Error saat mecah PDF: {e}")
