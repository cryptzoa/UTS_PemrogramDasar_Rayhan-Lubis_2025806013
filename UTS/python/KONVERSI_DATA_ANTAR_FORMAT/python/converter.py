import csv, json

def read_csv(file_path):
    """Membaca file CSV dan mengubah ke list of dict"""
    data = []
    with open(file_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 4:
                continue  
            nama, nim, nilai, mutu = row
            try:
                data.append({
                    "nama": nama.strip(),
                    "nim": nim.strip(),
                    "nilai_akhir": float(nilai),
                    "mutu": mutu.strip()
                })
            except ValueError:
                continue
    return data


def save_json(data, file_path):
    """Menyimpan data dalam format JSON"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
