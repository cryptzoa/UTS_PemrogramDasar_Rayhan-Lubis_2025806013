def display_data(data):
    """Menampilkan data mahasiswa ke terminal dengan format rapi"""
    print("=== DATA MAHASISWA ===")
    for d in data:
        print(f"Nama    : {d['nama']}")
        print(f"NIM     : {d['nim']}")
        print(f"Nilai   : {d['nilai_akhir']}")
        print(f"Mutu    : {d['mutu']}")
        print("-" * 30)

def average_score(data):
    """Menghitung rata-rata nilai akhir mahasiswa"""
    total = sum(d["nilai_akhir"] for d in data)
    return total / len(data) if data else 0
