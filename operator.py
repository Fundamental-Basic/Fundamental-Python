#OPERATOR ARITMATIKA / ARITMETHIC OPERATORS
a = 5
b = 6
c = 2
d = 2.1
e = 2.2
f = '{:03.1f}'.format(d + e)
g = '{:03.1f}'.format(a + e)

print(f' 11 = ', a + b) #addition (penjumalahan)
print(f' -1 = ', a - b) #subtraction (pengurangan)
print(f' 30 = ', a * b) #multiplication (perkalian)
print(f' 3 = ', b / c) #divdion (pembagian)
print(f' 25 = ', a ** c) #exponent (pemangkatan)
print(f' 2 = ', a // c) #floor division (hasil pembagian dimana hanya bil. bulat saja yang ditampilkan)
print(f' 1 = ', a % c) #modulus (sisa bagi)
print(f)
print(g)


#OPERATOR PERBANDINGAN /  COMPARISON (RELATIONAL) OPERATORS
'''OPERATOR PERBANDINGAN AKAN MENGHASILKAN NILAI BOOLEAN (TRUE/FALSE)'''

satu = 8
dua = 8
tiga = 9
empat = 8.1
lima = 9.2

case_1= satu ==	dua #Equal / sama dengan / satu == dua
case_2 = satu != tiga #Not equal/ tidak sama dengan/	satu != dua
case_3 = tiga > satu #Greater than/ lebih besar/ tiga > satu
case_4 = satu <	tiga #Less than/ lebih kecil/ satu < tiga
case_5 = satu >= dua #Greater than or equal to/ lebih besar atau sama dengan/ satu >= dua
case_6 = satu <= dua #Less than or equal to/ lebih kecil atau sama dengan/satu <= dua
case_7 = '{:03.1f}'.format(empat+lima) == '{:03.1f}'.format(17.3)

'''pada case_7 itu terdapat format dengan ket. sbg berikut :
03 artinya terdapat 3 karakter pada variable empat dan lima 
1f artinya satu angka dibelakang koma/desimal/float '''

print(case_7)

#OPERATOR PENUGASAN / ASSIGNMENT OPERATORS

biru = 10
hijau = 20
biru*=2 #nilai dari vaiable biru dikali 2
hijau**=2 #nilai dari variable hijau dipangkat 2

print(f'operator penugasan', biru)
print(hijau)


#OPERATOR LOGIKA / LOGICAL OPERATORS = and, or, not

'''akan menghasilkan nilai boolean (True/False)
and = semua kondisi harus benar maka hasil benar
or = salah satu benar maka hasil benar
not = kebalikan (inverse) '''

h = 5
i = 10
j = h == 5 and (i/h) == 2 #hasil True
k = h != 5 or (i/h) == 2 #hasil True
l = True
m = not (l) #hasil akan False

print(f'operator logika', j)
print(k)
print(f'operator logika', m)



#OPERATOR BITWISE / BITWISE OPERATORS = |(OR), & (AND), XOR (^), NOT(~), shift right, shift left
'''
-konsep logika dari operator '&' dan '~' sama seperti operator logika
-operator ^(XOR) akan menghasilkan True = salah satu true
-oprator '<<' akan menggeser n bit ke arah kiri dari bilangan yang sudah dikonversikan ke bil. biner
-setiap pergeseran 1 bit ke arah kiri akan menghasilkan operand dikali 2 dan sebaliknya jika ke arah 
kanan maka akan dibagi 2.
contohnya : 16 << 1 artinya 16 digeser 1 bit ke arah kiri, sehingga hasilnya 16 dikali 2 = 32
'''

n = 1
o = 4
p = format(n,'08b') #untuk memunculkan nilai biner dari variable n (2)
q = n | o # bitwise | (or)
r = format(9, '08b')
s = format(6, '08b')
#t = r & s #bitwise and (&)
#u = r ^ s #bitwise xor (^)
v = ~ o #bitwise not (~)
w = >> o
y = << n


print(f'biner dari variable p', p)
print(q)
print(r)
#print(t)
#print(u)
print(format(v, '08b'))
print(w)
print(y)

#OPERATOR KEANGGOTAAN  / MEMBERSHIP OPERATORS = IN, NOT IN

motor_honda = ['megapro', 'tiger', 'cbr']

print(f'operator membership','tiger' in motor_honda) #True
print(f'operator membership','tiger' not in motor_honda) #False
print(f'operator membership','ninja' not in motor_honda) #True
print(f'operator membership','ninja' in motor_honda) #False

#OPERATOR IDENTITAS / IDENTITY OPERATORS = IS, ISNOT

rumah_a = ['ayah', 'ibu', 'anak']
rumah_b = ['ayah', 'ibu', 'anak']
x = rumah_a

print(f'identity operator', x is rumah_a) #True
print(x is rumah_b) #False
print(x is not rumah_b) #True
print(x == rumah_b) #True
print(rumah_a == rumah_b) #True

