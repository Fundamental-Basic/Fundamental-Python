#
#
# #i = 0
# for i in range (0, 9):
#     for j in range (i):
#         print(j)
#
# def pajak (arg):
#     return 0.1 * arg
#
# print(pajak(100000)) #cara memanggil function pajak

# def profile(nama, umur):
#     print('nama saya ', nama, 'umur', umur)
#
# nama = input('masukan nama:')
# umur = input('masukan umur:')
#
# print(profile(nama, umur))
#
# from myFunction.Calculator import *
#
# num1 = 20
# num2 = 30
#
# print('penambahan', num1, 'dan', num2, 'adalah', penambahan(num1, num2))
# print('pengurangan', num1, 'dan', num2, 'adalah', pengurangan(num1, num2))
# print('perkalian', num1, 'dan', num2, 'adalah', perkalian(num1, num2))
# print('pembagian', num1, 'dan', num2, 'adalah', pembagian(num1, num2))

#LATIHAN
#diketahui :
'''
harga laptop = 7juta
uang muka = 1juta
bunga 10%
cicilan 12 bulan
sisa cicilan = harga - uang muka
berapakah jumlah suku bunga?
berapakah total tagihan?
berapakah tagihan perbulan ? '''

# from myFunction.kredit import *
# harga_laptop = input('masukan harga laptop:')
# harga_laptop = int
#
# uang_muka = input('masukan nilai uang muka :')
# bunga = 0.1
# tenor = 12
# jumlah_suku_bunga =


#memanggil function dalam class
# from myFunction.kucing import *
#
# objKucing = Kucing()
# objKucing.suara()
# objKucing.jenis()
#
# from myFunction.ayam import *
#
# objAyam = Ayam()
# objAyam.suara()
# objAyam.jenis()7

from myFunction.Score import *

nilai = input('masukan nilai anda:')
print('Nilai Anda ',nilai,',', getScore_nilai(int (nilai)), 'dengan', getScore_grade(int (nilai)))

