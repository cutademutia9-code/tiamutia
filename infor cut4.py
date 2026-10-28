print("PROGRAM PEMBELIAN BARANG")
print("-------------------------")

nama = input("Nama pembeli: ")
barang = input("Nama barang: ")
harga = int(input("Harga barang: Rp "))
jumlah = int(input("Jumlah barang: "))

total = harga * jumlah

if total >= 100000:
    diskon = total * 10 / 100
else:
    diskon = 0

bayar = total - diskon

print("\n--- STRUK PEMBELIAN ---")
print("Nama pembeli:", nama)
print("Nama barang:", barang)
print("Harga barang: Rp", harga)
print("Jumlah barang:", jumlah)
print("Total belanja: Rp", total)
print("Diskon: Rp", int(diskon))
print("Total pembayaran: Rp", int(bayar))