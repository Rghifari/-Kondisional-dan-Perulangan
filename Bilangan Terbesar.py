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
