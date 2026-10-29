
def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_case = [
    (59, "Tidak lulus"),
    (60, "Lulus"),
    (61, "Lulus"),
]

for nilai, expected in test_case:
    actual = status_lulus(nilai)
    status = "PASS" if actual == expected else "FAIL"

    print(
        f"Nilai: {nilai} | "
        f"Expected: {expected} | "
        f"Actual: {actual} | {status}"
    )
