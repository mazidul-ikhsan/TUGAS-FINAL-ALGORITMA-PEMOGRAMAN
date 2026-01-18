# Start

# Masukkan jumlah hari sewa
hari = int(input("Masukkan jumlah hari sewa: "))

# Proses perhitungan
if hari <= 3:
    tarif = 200000
else:
    tarif = 100000

total = hari * tarif

# Tampilkan total bayar
print("Total bayar: Rp", total)

# End


