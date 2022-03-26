import datetime as dt
from re import A
from sys import builtin_module_names

print ("==Silahkan masukan tanggal lahir kalian: ")

tanggal = int(input("Masukan Tanggal: \t"))
bulan = int(input("Masukan Bulan: \t\t"))
tahun = int(input("Masukan Tahun: \t\t"))

tanggal_lahir = dt.date(tahun, bulan, tanggal)

print("Tanggal Lahir anda adalah : {}".format(tanggal_lahir))

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
25
print(f"hariny adalah: {tanggal_lahir:%A}")
print(f"umur anda sekarang adalah: {umur_tahun}")