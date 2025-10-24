# game.py
import random
from colorama import Fore, Style, init

init(autoreset=True)

LEVELS = {
    1: {'range': (1, 10), 'attempts': 3, 'multiplier': 1},
    2: {'range': (1, 50), 'attempts': 5, 'multiplier': 2},
    3: {'range': (1, 100), 'attempts': 7, 'multiplier': 3},
}

def _prompt_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(Fore.YELLOW + "Input tidak valid — masukkan angka." + Style.RESET_ALL)

def play_level(player_name: str, level: int) -> int:
    """
    Jalankan satu level untuk player_name.
    Mengembalikan skor level (int). 0 jika kalah.
    """
    cfg = LEVELS.get(level)
    if not cfg:
        raise ValueError("Level tidak tersedia")

    lo, hi = cfg['range']
    attempts = cfg['attempts']
    multiplier = cfg['multiplier']

    secret = random.randint(lo, hi)

    print(Fore.CYAN + f"\n== {player_name} • Level {level} | Tebak {lo}–{hi} | Percobaan: {attempts} ==" + Style.RESET_ALL)

    while attempts > 0:
        try:
            guess = int(input(f"Masukkan tebakan (sisa {attempts}): "))
        except ValueError:
            print(Fore.YELLOW + "Bukan angka. Coba lagi." + Style.RESET_ALL)
            continue

        if guess == secret:
            # skor = sisa percobaan * 10 * multiplier
            score = attempts * 10 * multiplier
            print(Fore.GREEN + f"🎉 Benar! Angka: {secret}. Skor level: {score}" + Style.RESET_ALL)
            return score
        elif guess < secret:
            print(Fore.MAGENTA + "Terlalu kecil." + Style.RESET_ALL)
            # hint jarak
            if secret - guess > (hi - lo) // 3:
                print("➡️ Kamu terlalu jauh dari jawabannya!")
        else:
            print(Fore.MAGENTA + "Terlalu besar." + Style.RESET_ALL)
            if guess - secret > (hi - lo) // 3:
                print("⬅️ Kamu terlalu jauh dari jawabannya!")

        attempts -= 1
        if attempts > 0:
            print(f"Nyawa tersisa: {attempts}\n")

    print(Fore.RED + f"💀 Kalah — angka yang benar: {secret}. Skor level: 0" + Style.RESET_ALL)
    return 0

def play_full_campaign(player_name: str) -> int:
    """
    Jalankan campaign: level 1 -> level 2 -> level 3.
    Kembalikan total skor untuk pemain.
    """
    total = 0
    for lvl in sorted(LEVELS.keys()):
        lvl_score = play_level(player_name, lvl)
        total += lvl_score
    print(Fore.BLUE + f"\n{player_name} • Total skor campaign: {total}" + Style.RESET_ALL)
    return total

if __name__ == "__main__":
    # quick local demo
    name = input("Nama pemain demo: ")
    play_full_campaign(name)
