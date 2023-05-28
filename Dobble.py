import sys

def dobble(n):
    if n < 2:
        return

    kartya_szam = n * n + n + 1

    pakli = []

    elso_kartya = list(range(1, n + 1))
    pakli.append(elso_kartya)

    for i in range(1, kartya_szam):
        kartya = [(i % n) + 1]
        for l in range(1, n):
            kartya.append((l + 1) * n + (i - 1) * l % n + 1)
        pakli.append(kartya)

    return pakli

def print_pakli(pakli):
    for kartya in pakli:
        print(" ".join(str(szam) for szam in kartya))

if len(sys.argv) != 2:
    print("Használat: python dobble.py <mennyiseg szama>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    sys.exit(1)

pakli = dobble(n)
print_pakli(pakli)
