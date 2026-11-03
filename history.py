from datetime import datetime


def salveaza(operatie, a, b, rezultat, fisier="istoric.log"):
    with open(fisier, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} | {a} {operatie} {b} = {rezultat}\n")
