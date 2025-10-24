# scoreboard.py
import json
import os
from datetime import datetime

DEFAULT_PATH = "scores.json"

def load_scores(path=DEFAULT_PATH):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # bila file corrupt atau baca gagal, kembalikan list kosong
        return []

def save_scores(scores, path=DEFAULT_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2, ensure_ascii=False)

def add_score(name: str, score: int, path=DEFAULT_PATH):
    scores = load_scores(path)
    entry = {
        "name": name,
        "score": int(score),
        "date": datetime.now().isoformat()
    }
    scores.append(entry)
    # sort descending berdasarkan score
    scores = sorted(scores, key=lambda e: e["score"], reverse=True)
    save_scores(scores, path)
    return scores

def top_scores(n=5, path=DEFAULT_PATH):
    scores = load_scores(path)
    scores = sorted(scores, key=lambda e: e["score"], reverse=True)
    return scores[:n]

if __name__ == "__main__":
    # demo kecil
    print(top_scores())
