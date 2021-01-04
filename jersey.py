jersey = 1
ukuran = 'm'

if jersey == 1:
    tim = 'persib'
    if ukuran == 's':
        harga = 100000
        print( 'jersey', tim, 'ukuran', ukuran, 'haragnya', harga )
    elif ukuran == 'm':
        harga = 150000
        print( 'jersey', tim, 'ukuran', ukuran, 'haragnya', harga )
    elif ukuran == 'l':
        harga = 200000
        print( 'jersey', tim, 'ukuran', ukuran, 'haragnya', harga )
    else:
        harga = 0
        if harga == 0:
            print('ukuran tidak tersedia')
        else:
            print('jersey', tim, 'ukuran', ukuran, 'haragnya', harga)
else:
    print('jersey tidak tersedia')