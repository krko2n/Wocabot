#!/usr/bin/env python3
"""Easy interactive WocaBee launcher; never saves credentials."""
import getpass
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def ask_int(label, default, minimum=1):
    while True:
        response = input(f"{label} [{default}]: ").strip()
        if not response:
            return default
        if response.isdecimal() and int(response) >= minimum:
            return int(response)
        print(f"Zadej cele cislo >= {minimum}.")


def main():
    if sys.version_info < (3, 9):
        print("Vyžaduje Python 3.9 nebo novější.")
        return 1
    try:
        import playwright  # noqa: F401
        import requests  # noqa: F401
        import toml  # noqa: F401
    except ImportError:
        print("Nainstaluj závislosti: python -m pip install -r requirements.txt")
        return 1

    print("\n=== VOCABOT ===")
    print("Údaje se neukládají do souboru.\n")

    try:
        username = os.environ.get("WOCABEE_USERNAME") or input("Přihlašovací jméno: ").strip()
        password = os.environ.get("WOCABEE_PASSWORD") or getpass.getpass("Heslo: ")
        if not username or not password:
            print("Je potřeba vyplnit jméno i heslo.")
            return 1
        print("\nČísla odpovídají pořadí tříd a balíčků v aplikaci, od 1.")
        class_index = ask_int("Číslo třídy", 1) - 1
        package_index = ask_int("Číslo balíčku", 1) - 1
        points = ask_int("Kolik bodů navíc", 100)
        double_points = input("Dvojnásobné body? [a/N]: ").strip().lower() in ("a", "ano", "y", "yes")
    except (EOFError, KeyboardInterrupt):
        print("\nSpuštění zrušeno.")
        return 130

    data_dir = ROOT / "data"
    data_dir.mkdir(exist_ok=True)
    child_env = os.environ.copy()
    child_env.update({
        "WOCABEE_USERNAME": username,
        "WOCABEE_PASSWORD": password,
        "WOCABEE_CLASS_INDEX": str(class_index),
        "WOCABEE_PACKAGE_INDEX": str(package_index),
        "WOCABEE_DOUBLE_POINTS": str(double_points).lower(),
        "WORDLIST_FILE": str(data_dir / "wordlist.json"),
        "PICTURE_FILE": str(data_dir / "picturelist.json"),
        "ADDON_POINTS": str(points),
        "MILESTONE_REMINDER": "100",
        "DEBUG_PORT": "http://127.0.0.1:9222",
        "HEADLESS": "false",
    })
    try:
        print("\nSpouštím prohlížeč. Ukončení: Ctrl+C.\n")
        return subprocess.call([sys.executable, str(ROOT / "startup.py")], cwd=ROOT, env=child_env)
    except KeyboardInterrupt:
        print("\nBot zastaven.")
        return 130
    finally:
        child_env.pop("WOCABEE_USERNAME", None)
        child_env.pop("WOCABEE_PASSWORD", None)


if __name__ == "__main__":
    sys.exit(main())
