# PERULANGAN (LOOP)

# For-loop
# For kondisi:
#   Aksi

a = 0
a += 1 # a = a + 1
print (a)
a += 1
print (a)
a += 1
print (a)

print("ini akhir for 1\n")

# Perulangan dengan list
angka_list = [0,1,4,8,10]
for i in angka_list:
    print(f"i sekarang -> {i}")

# Perulangan dengan range
angka_range = range(5) # Diulangi 5 kali

for i in angka_range:
    print(f"i sekarang -> {i}")

print("ini akhir for 2 \n")

angka_range2 = range(1, 10)
for i in angka_range:
    print(f"i sekarang -> {i}")

print("ini akhir for 3 \n")


# Latihan 

# perulangan dengan nama

data_str = "Jusmanullah"
for huruf in data_str:
    print(huruf)

print("akhir perulangan string\n")