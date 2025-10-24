# main.py
from colorama import Fore, Style, init
from game import play_full_campaign
from scoreboard import add_score, top_scores
import sys

init(autoreset=True)

def prompt_positive_int(prompt):
    while True:
        try:
            v = int(input(prompt))
            if v > 0:
                return v
            print("Masukkan angka lebih besar dari 0.")
        except ValueError:
            print("Input bukan angka. Coba lagi.")

def main():
    print(Fore.CYAN + "=== GUESS BATTLE ===" + Style.RESET_ALL)
    print("Mode: Campaign (Level 1 → 2 → 3)\n")

    num_players = prompt_positive_int("Berapa pemain yang akan bermain? (1 untuk single-player): ")

    results = []
    for i in range(1, num_players + 1):
        name = input(f"\nMasukkan nama pemain #{i}: ").strip()
        if not name:
            name = f"Pemain{i}"
        print(Fore.YELLOW + f"\nGiliran: {name}" + Style.RESET_ALL)
        total = play_full_campaign(name)
        results.append((name, total))
        # simpan segera ke scoreboard
        add_score(name, total)

    print("\n" + "="*40)
    print(Fore.GREEN + "Sesi selesai — hasil pemain:" + Style.RESET_ALL)
    for name, score in results:
        print(f"- {name}: {score}")

    print("\n" + Fore.MAGENTA + "Top 5 Pemain Terbaik:" + Style.RESET_ALL)
    top = top_scores(5)
    if not top:
        print("Belum ada skor.")
    else:
        for idx, entry in enumerate(top, start=1):
            print(f"{idx}. {entry['name']} — {entry['score']} (tanggal: {entry.get('date','-')})")

    print("\nTerima kasih sudah bermain! 👋")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + Fore.RED + "Permainan dihentikan. Sampai jumpa!" + Style.RESET_ALL)
        sys.exit(0)
