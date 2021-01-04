provider = 1
nominal = 15

if provider == 1:
    pro = 'simpati'
    if nominal == 10:
        harga = 11000
    elif nominal == 20:
        harga = 12000
    else: print('nominal')
if provider == 2:
    pro = 'IM3'
    if nominal == 10:
        harga = 11500
    elif nominal == 20:
        harga = 12500
if provider == 3:
    pro = 'XL'
    if nominal == 10:
        harga = 13000
    elif nominal == 25:
        harga = 26000
print( 'Pulsa', pro, 'nominal', nominal, 'harganya', harga )
