# Jumlah baris piramida
n = 3
i = 0

while i < n:
    spasi = " " * (n - i - 1)
    bintang = "*" * (2 * i + 1)
    print(spasi + bintang)
    i += 1
