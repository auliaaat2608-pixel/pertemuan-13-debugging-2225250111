
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return None

    return sum(nilai) / len(nilai)


def status(nilai):
    if nilai >= 60:
        return "Lulus"

    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:
        return None

    tertinggi = nilai[0]

    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x

    return tertinggi


def jalankan_test(nama, fungsi, input_data, expected):
    actual = fungsi(input_data)

    if actual == expected:
        hasil = "PASS"
    else:
        hasil = "FAIL"

    print(
        f"{nama} | Expected: {expected} | "
        f"Actual: {actual} | {hasil}"
    )

    return actual == expected


# Data utama
nilai = [80, 60, 90, 70]

print("=== HASIL PROGRAM ===")
print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))

print("\n=== PENGUJIAN TEST CASE ===")

tests = [
    ("T1 Rata-rata 4 data",
     hitung_rata_rata, [80, 60, 90, 70], 75.0),

    ("T2 Rata-rata 2 data",
     hitung_rata_rata, [100, 80], 90.0),

    ("T3 Status nilai 60",
     status, 60, "Lulus"),

    ("T4 Status nilai 59",
     status, 59, "Tidak lulus"),

    ("T5 Nilai tertinggi",
     nilai_tertinggi, [80, 60, 90, 70], 90),

    ("T6 List kosong",
     hitung_rata_rata, [], None),

    ("T7 Semua nilai negatif",
     nilai_tertinggi, [-5, -2, -8], -2),
]

jumlah_lulus = 0

for nama, fungsi, input_data, expected in tests:
    if jalankan_test(nama, fungsi, input_data, expected):
        jumlah_lulus += 1

print(f"\nHasil akhir: {jumlah_lulus}/{len(tests)} test PASS")
