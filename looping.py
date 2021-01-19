angka = [1,2,3,4,5,6]
for x in angka :
    print(x)

'''jika hanya ingin mengakses hanya indeks pertama [0] maka gunakan break indeks kedua [1]'''
minuman = ['Aqua', 'Le Mineral', 'Vit']
for y in minuman :
    if y == 'Le Mineral':
        break
    print('saya mau beli', y)

a = 1
while (a<=5):
    print('Data ke-', a)
    a=a+1

b = 1
while (b<10):
    b=b+1
    if (b==3):
        continue
    print('cetak angka ke-', b)

