
from pathlib import Path

try:
    lokasi_file = Path(__file__).with_name("nilai.txt")

    with open(lokasi_file, "r", encoding="utf-8") as file:
        nilai = [
            int(baris.strip())
            for baris in file
            if baris.strip()
        ]

    if not nilai:
        print("File tidak berisi data nilai.")
    else:
        print("Jumlah data:", len(nilai))
        print("Rata-rata:", sum(nilai) / len(nilai))

except FileNotFoundError:
    print("File nilai.txt tidak ditemukan.")
    print("Lokasi yang dicari:", lokasi_file)

except ValueError:
    print("File berisi data yang bukan bilangan bulat.")
