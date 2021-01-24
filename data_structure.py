'''LIST'''

#LIST : UNTUK MENYIMPAN DATA YANG BANYAK DALAM SATU VAIABLE (SEPERTI ARRAY)
# LIST MENGUNAKAN SIKU []
#ISI DATA LIST BISA BERMACAM-MACAM TIPE DATA

fruit = ['apple','banana', 'orange', 'anggur','mango']

print(len(fruit))
print(max(fruit))
print(min(fruit))
print(list(fruit))
print(fruit [1])

#LOOPING UNTUK MENAMPILKAN DATA LIST
for i in fruit :
    print(i)

#UNTUK MENGGANTI DATA/ITEM DALAM LIST
fruit [0] = 'guava'
print(fruit)

#UNTUK MENAMBAHKAN DATA/ITEM DALAM DATA
#ADA BEBERAPA METHOD : INSERT, EXTEND

#INSERT UNTUK MENAMBAHKAN ITEM PADA INDEKS TERTENTU
fruit.insert(2, 'strawberry')
print(fruit)

#MEMOTONG ITEM DALAM DATA LIST (SLICING)

#OPERASI LIST (+, *)
#OPERASI PENGGABUNGAN
new_fruit = ['lychee', 'watermelon']
new = fruit + new_fruit
print('NEW',new)

#OPERASI PERKALIAN,UNTUK MENGULANG SEBANYAK n (*)


#LIST MULTIDIMENSI, UNTUK DATA YANG KOMPLEKS
#TABEL, MATRIKS DLL

drinks =[
    ['juice', 'coffee', 'tea'],
    ['orange juice', 'coffee latte', 'green tea'],
    ['mango juice', 'coffee americano', 'white tea'],
    ['avocado juice','espresso', 'oolong tea']
]

#cetak indeks ke 1 (kolom), indeks ke 2 baris
# 3 kolom, 4 baris


#tampilkan seluruh data list multidimensi (gunakan nested looping)
for x in drinks : #pengulangan data kolom
    for y in x : #pengulangan data baris
        print(y) #cetak semua data


'''DICTIONARY'''
#STRUCTURE DATA YANG MENYIMPAN DATA YANG MEMILIKI KEY DAN VALUE
#KEY


myProfile = {
    'name': 'kumbi',
    'age': 18,
    'married': False,
    'hobby': ['reading', 'playing games', 'hiking'],
    #nested (didalam dictionary ada dictionary)
    'sosmed': {
        'instagram': '@kumbi',
        'facebook': "kumbi.105"
    }
}

print(myProfile['sosmed']['instagram'])
print(myProfile['hobby'][1])
print(myProfile.get('married')) #untu
print(len(myProfile)) #untuk menampilkan jumlah data/item dalam variable atau list tsb

#untuk menampilkan key dan value
print(myProfile.items())

#untuk menampilkan valuenya saja
print(myProfile.values())

#mencetak semua nilai dari dictionary myProfile (gunakan perulangan)
for profile in myProfile.values() :
    print(profile)

#menambah item/data dalam data dictionary myProfile
myProfile['favcolor']= 'blue'
print(myProfile)

#mengubah value dalam dalam data dictionary


'''TUPLE'''
#BESIFAT IMMUTABLE (ISI TIDAK BISA DIRUBAH/DIHAPUS)
#ISI/ITEM/DATA TUPLE BISA BERBAGAI MACAM NILAI DAN OBJEK