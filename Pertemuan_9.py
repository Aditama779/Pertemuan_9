# latihan
#No 1
kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. tambah 'truk' di akhir
kendaraan.append('truk')
print(f"setelah append = {kendaraan}")

# b. sisipkan 'becak' di index 1
kendaraan.insert(1, 'becak')
print(f"setelah insert = {kendaraan}")

# c. hapus data paling belakang
kendaraan.pop()
print(f"setelah pop = {kendaraan}")

# d. ubah 'sepeda' menjadi 'skuter'
kendaraan[kendaraan.index('sepeda')] = 'skuter'
print(f"setelah diubah = {kendaraan}")

# e. jumlah total data
print(f"jumlah data = {len(kendaraan)}")

#No 2
angka = [75, 80, 90, 75, 85, 100, 65]

# a. index skor 100
print(f"index skor 100 = {angka.index(100)}")

# b. jumlah siswa dengan skor 75
print(f"jumlah skor 75 = {angka.count(75)}")

# c. urutkan dari terkecil
angka.sort()
print(f"setelah sort = {angka}")

# d. balik urutan
angka.reverse()
print(f"setelah reverse = {angka}")

#No 3
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

menu_utama.extend(menu_tambahan)
print(f"data gabungan = \n{menu_utama}")

#No 4
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. harga Pensil (baris 1, kolom 1)
print(f"harga Pensil = {data_barang[1][1]}")

# b. perulangan
for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")