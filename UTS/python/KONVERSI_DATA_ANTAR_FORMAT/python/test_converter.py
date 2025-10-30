from converter import compute_average

def test_compute_average():
    data = [
        {"nama": "Rina", "nim": "2310001", "nilai_akhir": "80"},
        {"nama": "Doni", "nim": "2310002", "nilai_akhir": "70"}
    ]
    assert round(compute_average(data), 2) == 75.0
