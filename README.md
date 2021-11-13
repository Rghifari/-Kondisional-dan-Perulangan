```
Nama    : Muhammad Rafi Al Ghifari
Nim     : 312110526
Kelas   : TI.21.BA.1
```

# Kondisional & Perulangan

# Lab 2 : Struktur Kondisi

*Latihan 1
1. Buat program sederhada dengan input 2 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if.

# Codingan
```

# membuat judul program
print(' ')
print('Program menentukan Nilai Terbesar dari 2 bilangan')

# input bilangan
print(' ')
a = int(input("masukan bilangan pertama: "))
b = int(input("masukan bilangan kedua: "))

# Menentukan Nilai Bilangan  dengan if else
print(' ')
if a > b:
    maks = a
else:
    maks = b
# mencetak nilai maksimum
print('Nilai Terbesar adalah %d' % maks)

```
<img width="705" alt="Nilai Terbesar" src="https://user-images.githubusercontent.com/93661771/141132238-878a2dd9-7b5e-4e42-ad42-c83daa57194b.PNG">

# Hasil Output Codingan Nilai Terbesar
<img width="960" alt="output nilai terbesar" src="https://user-images.githubusercontent.com/93661771/141132533-ccab2595-a039-44ce-896b-1f2ee26d154d.PNG">

*Latihan 2
1. Buat program untuk mengurutkan data berdasarkan input sejumlah data (minimal 3 variable input atau lebih), kemudian tampilkan hasilnya secara berurutan mulai dari data terkecil.

# Codingan
```
print('')
print("Program mengurutkan data")
data = []
for i in range (3):
    x = int(input('Masukan bilangan: '))
    data.append(x)
print('Data sebelum diurutkan: ', data)
list.sort(data)
print('Data sesudah diurutkan: ', data)
```
<img width="704" alt="Variable urutan data terkecil" src="https://user-images.githubusercontent.com/93661771/141644854-a7d5bcf1-3d1b-46e0-b2ff-bfabcb55d82a.PNG">

# Hasil Output Codingan Program mengurutkan data
<img width="941" alt="Output variable" src="https://user-images.githubusercontent.com/93661771/141644874-e8da61c1-4304-4279-9c92-e7257dc29f02.PNG">

# Lab 3 : Perulangan

*Latihan 1
1. Buat program dengan perulangan bertingkat (nested) for yang menghasilkan output sebagai berikut:

# Codingan
```
s = ''
for i in range (10):
    s += str(i) +'   '
print (s)

s = ''
for i in range (1, 11):
    s += str(i) +'   '
print (s)

s = ''
for i in range (2, 12):
    s += str(i) +'   '
print (s)

s = ''
for i in range (3, 13):
    s += str(i) +'   '
print (s)

s = ''
for i in range (4, 14):
    s += str(i) +'   '
print (s)

s = ''
for i in range (5, 15):
    s += str(i) +'   '
print (s)

s = ''
for i in range (6, 16):
    s += str(i) +'   '
print (s)

s = ''
for i in range (7, 17):
    s += str(i) +'   '
print (s)

s = ''
for i in range (8, 18):
    s += str(i) +'   '
print (s)

s = ''
for i in range (9, 19):
    s += str(i) +'   '
print (s)

```
<img width="705" alt="Perulangan bertingkat" src="https://user-images.githubusercontent.com/93661771/141139646-f36b4280-b726-4acd-b753-7f8552c645fc.PNG">

# Hasil Output Codingan
<img width="808" alt="output perulangan bertingkat" src="https://user-images.githubusercontent.com/93661771/141139750-7bed1b34-3613-4f7a-83bf-890a10bef541.PNG">

*Latihan 2
1. Tampilkan n bilangan acak yang lebih kecil dari 0.5.
2. nilai n diisi pada saat runtime
3. anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya

# Codingan
```
print('==== Bilangan Acak yang lebih kecil dari 0.5 ====')
print(' ')
import random
N = int(input("Masukan nilai N : "))
a = 0
for x in range(N):
    a += 1
    b = random.uniform(.0,.5)
    print('Data ke:',a,'==>',b)
print('Selesai')
print(' ')
jawab = 'lanjutkan'
hitung = 0
while jawab == "lanjutkan":
    hitung += 1
    jawab = input('Ingin Mengulang ? (Y/N) : ')
    if jawab == "Lanjutkan":
        break
print('Total perulangan : ' + str (hitung))
```
# Hasil Codingan (Program)
![hasil codingan](https://user-images.githubusercontent.com/46749500/53287636-a9dbbc80-37b1-11e9-8043-13169152b9dd.png)

# Tugas Latihan 
1. Simpan project Praktikum hari ini ke repository server.
2. Buat penjelasan setiap Lab/latihannya pada file README.md

# Sekian & Terimakasih

