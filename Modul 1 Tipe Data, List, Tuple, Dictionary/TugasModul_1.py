# Input jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

# Input data untuk setiap mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"\nData Mahasiswa ke-{i+1}")
    
    # Input NIM dan Nama
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")

    # Input mata kuliah dan nilai
    mata_kuliah_nilai = []
    while True:
        mk = input("Masukkan nama mata kuliah (atau 'selesai' untuk selesai): ")
        if mk.lower() == 'selesai':
            break
        nilai = float(input(f"Masukkan nilai untuk {mk}: "))
        mata_kuliah_nilai.append((mk, nilai))
    
    # Simpan data mahasiswa dalam dictionary
    data_mahasiswa[nim] = {'nama': nama, 'nilai': mata_kuliah_nilai}

# Tampilkan rata-rata nilai untuk setiap mahasiswa
print("\nRata-rata nilai untuk setiap mahasiswa:")
for nim, mhs in data_mahasiswa.items():
    nilai_total = sum(nilai for _, nilai in mhs['nilai'])
    jumlah_mk = len(mhs['nilai'])
    rata_rata = nilai_total / jumlah_mk if jumlah_mk else 0
    print(f"NIM: {nim}, Nama: {mhs['nama']}, Rata-rata: {rata_rata:.2f}")

# Tampilkan daftar seluruh data mahasiswa
print("\nDaftar seluruh data mahasiswa:")
for nim, mhs in data_mahasiswa.items():
    print(f"NIM: {nim}, Nama: {mhs['nama']}, Mata Kuliah dan Nilai: {mhs['nilai']}")