print('')
print("Program mengurutkan data")
data = []
for i in range (3):
    x = int(input('Masukan bilangan: '))
    data.append(x)
print('Data sebelum diurutkan: ', data)
list.sort(data)
print('Data sesudah diurutkan: ', data)
