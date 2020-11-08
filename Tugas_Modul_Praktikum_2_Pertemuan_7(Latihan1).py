nama = input("Masukkan Nama : ")
uts = int(input("Masukkan Nilai UTS : "))
uas = int(input("Masukkan Nilai UAS : "))
tugas = int(input("Masukkan Nilai Tugas : "))

akhir = tugas * .2 + uts * .4 + uas * .4
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]
if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "E"

print("\nNama           :",nama)
print("NILAI UTS        :",uts)
print("NILAI UAS        :",uas)
print("NILAI TUGAS      :",tugas)
print("NILAI AKHIR      :",akhir)
print("\nNilia Huruf    :",huruf)
print("keterangan       :",keterangan)
