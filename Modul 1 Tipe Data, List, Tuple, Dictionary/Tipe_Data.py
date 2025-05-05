# Integer (int)

x = 10
y = -200
z = 0
print(type(x))  # <class 'int'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'int'>

# operator penjumlahan untuk tipe data integer
a1 = 5
a2 = -180

a3 = a1 + a2
print(a3)
print(type(a3))

# Float (float)

# Tipe data float
a = 3.141592
b = -0.001
c = 1.0
d = float('inf') # memasukkan infinity sebagai float

# melihat isi variabel
print(a)
print(b)
print(c)
print(d)

# cek tipe data dari variabel
print(type(a))  # <class 'float'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'float'>

# membandingkan nilai b3 dengan yang lain
if (a < d):
    print('lebih kecil')
else:
    print('lebih besar')

# Operasi aritmatika pada float
print(a + c)
print(b ** a)
print(abs(a))

# hasil operasi aritmatika pada float
float = b * a
print(float)
print(type(float))

# mengubah hasil operasi aritmatika float menjadi integer
print(int(b * a))

# String (str)

a = 'Halo'
b = "Python"
c = """Ini adalah
string multi-baris"""
print(type(a))  # <class 'str'>
print(type(b))  # <class 'str'>
print(type(c))  # <class 'str'>

# indexing dan slicing 
text = "Python"
print(text[0])     # Output: P
print(text[-1])    # Output: n
print(text[0:3])   # Output: Pyt
print(text[:4])    # Output: Pyth
print(text[::2])   # Output: Pto (loncat 2 karakter)

# Operasi pada String

# Operasi penggabungan string
print('Hello ' + 'World')

# Operasi pengulangan string
print('Hi' * 3)

# Operasi Pengecekan string
print('a' in 'data') # menghasilkan boolean (True/False)

# Operasi panjang string
print(len('Python'))

# Fungsi dalam String

s = "python programming"
print(s.upper())       # 'PYTHON PROGRAMMING'
print(s.capitalize())  # 'Python programming'
print(s.title())       # 'Python Programming'
print(s.replace("python", "java"))  # 'java programming'
print(s.split())       # ['python', 'programming']
print(s.find("gram"))  # 10

# String Format

# String format menggunakan F-String
name = "Winda Kosherawati"
age = 20
print(f"Halo, nama saya {name}, umur saya {age}")

# String format dengan format method
print("Halo, nama saya {}, umur saya {}".format(name, age))