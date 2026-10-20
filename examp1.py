import tkinter as tk

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("400x500")
top.resizable(False, False)

judul = tk.Label(
    top,
    text="Aplikasi prediksi prodi pilihan",
    font=("Arial", 16, "bold")
) 
judul.grid(row=0, column=0, columnspan=2, pady=20)

mapel = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Informatika",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Sejarah",
    "Geografi"
]

input_nilai = []

for i, nama_mapel in enumerate(mapel):
    label = tk.Label(top, text=nama_mapel, font=("Arial", 10))
    label.grid(row=i + 1, column=0, padx=20, pady=5, sticky="w")

    entry = tk.Entry(top, width=20)
    entry.grid(row=i + 1, column=1, padx=20, pady=5)

    input_nilai.append(entry)

def hasil_prediksi():
    hasil.config(text="Teknologi Informasi")

tombol = tk.Button(
    top,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
tombol.grid(row=11, column=0, columnspan=2, pady=20)

hasil = tk.Label(
    top,
    text="",
    font=("Arial", 14, "bold"),
    fg="RED"
)
hasil.grid(row=12, column=0, columnspan=2, pady=10)


top.mainloop()