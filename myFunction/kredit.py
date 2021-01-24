def jumlah_suku_bunga (harga_laptop, bunga):
    return harga_laptop * bunga

def total_tagihan (harga_laptop, jumlah_suku_bunga):
    return harga_laptop + jumlah_suku_bunga

def tagihan_perbulan (total_tagihan, uang_muka, tenor):
    return (total_tagihan-uang_muka) / tenor