# Input jumlah deret
n = 10

# Inisialisasi dua angka pertama
a = 1
b = 1

print(a, end=' ') 
print(b, end=' ')  

# Proses fibonacci
for i in range(2, n):  
    c = a + b 
    print(c, end=' ')
    # Update nilai untuk iterasi selanjutnya
    a = b
    b = c