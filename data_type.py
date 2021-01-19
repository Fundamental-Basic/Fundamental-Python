''' TIPE DATA / DATA TYPE
'''

a = 6 #tipe data integer (int)
b = 2.1 #tipe data float
c = 'Hello World' #tipe data string (str)

'''tipe data stirng bisa diakses sesuai indeksnya dan berapa karakter yg akan diakses, contohnya 
dari vaiable c hanya akan diakses karakter 'Wor' maka cara aksesnya seperti ini
print (c[6:9])
dimana :

6 = indeks karakter W (indeks dimulai dari 0)
9 = jumlah karakter yg diakses
'''

print (c[6:9])

w, x, y, z = 1, 'mobil', 'motor', 9.7 #tipe data string (str)

'''untuk mengakses karakter dari salah satu vaiable bisa dengan code seperti ini 
print('%s' %x)
dimana 
%s = tipe format untuk tipe data string; f= float, i= integer 
%x = untuk mengakses variable x
 '''

print('%s' %x)
print('%f' %z)
print('%s dan %s adalah alat transportasi' %(x,y))
print('%i' %w)


d = 1j #tipe data complex
e = ["apel", "anggur", "nanas"] #tipe data list
f = ("jambu", "melon", "semangka") #tipe data tuple
g = {"pisang", "nangka", "mangga"} #tipe data set
h = {"name" : "John", "age" : 36} #tipe data dictionary
i = range(6) #tipe data range
j = frozenset({"manggis", "jeruk", "leci"}) #tipe data frozenset
k = True #tipe data booleans (bool), hanya ada dua yaitu True dan False
l = b"Hello" #tipe data bytes
m = bytearray(5) #tipe data bytearray
n = memoryview(bytes(5)) #tipe data memoryview

print(g)

'''CARA MERUBAH/ CASTING TIPE DATA'''
data_integer = 9
data_integer = float(data_integer)
print(data_integer)




