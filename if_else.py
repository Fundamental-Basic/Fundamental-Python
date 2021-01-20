#CONDITIONS AND IF STATEMENTS

a = 10
b = 20
if b > a:
  print("b is greater than a")

#INDENTATION

c = 30
d = 40
if d > c:
    print("d is greater than c") # ada indentation

#ELIF

e = 30
f = 30
if e > f:
  print("e is greater than f")
elif e == f:
  print("e and f are equal")

#ELSE

g = 50
h = 40
if h > g:
  print("h is greater than g")
elif g == h:
  print("g and h are equal")
else:
  print("g is greater than h")

#TERNARY OPERATORS/ CONDITIONAL EXPRESSIONS

i = 100
j = 130
print("TERNARY, J") if j > i else print("=") if i == j else print("I")

#AND

k = 200
l = 50
m = 400
if k > l and m > k:
  print("Both conditions are True")

#OR

n = 200
o = 30
p = 500
if n > o or n > p:
  print("At least one of the conditions is True")

#NESTED IF

q = 41

if q > 10:
  print("Above ten,")
  if q > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#THE PASS STATEMENTS

r = 60
s = 100

if s > r:
  pass

#CONTOH SOAL

nilai = 98

if nilai >= 60 and nilai <= 100:
    print('lulus')
    if nilai >= 90 and nilai <= 100:
        print('grade A')
    elif nilai >= 60 and nilai <= 89:
        print('grade B')
elif nilai >= 0 and nilai <= 59:
    print('gagal, tetap semangat belajar lagi')
    if nilai >= 50 and nilai <= 59:
        print('grade C')
    elif nilai >= 30 and nilai <= 49:
        print('grade D')
    elif nilai >= 0 and nilai <= 29:
        print('grade E')
else:
    print('anda salah memasukan nilai')