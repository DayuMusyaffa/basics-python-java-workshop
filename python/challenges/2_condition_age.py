# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
umur = int(input("masukkan umur anda: "))

# 2. TODO Tentukan kategori berdasarkan usia
kategori_usia = umur
if umur >= 60:
    print("Lansia")
elif umur >= 18:
    print("Dewasa")
elif umur >= 12:
    print("Remaja")
else:
    print("Anak")

print("Anda Berumur: ", kategori_usia)