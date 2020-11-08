_________________________________________________________________________________

Jadi pada pertemuan ini saya diberikan beberapa tugas oleh dosen saya yaitu diantaranya:

## TUGAS MODUL PRAKTIKUM 2
* LATIHAN 1

Pada tugas ini, saya diminta untuk membuat sebuah program menentukan nilai akhir
Untuk bisa dapat menghasilkan output tersebut maka saya memasukan syntax:

```
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

```

Jika sudah memasukan semua syntax diatas dan telah di run, maka kamu akan mendapatkan tampilan seperti gambar yang ada dibawah ini.

![Foto Lat1](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7_MODUL_PRAKTIKUM2/blob/main/Modul%20Praktikum%202/Latihan1.png) <br>

* LATIHAN 2

Di tugas latihan kedua ini, saya diminta untuk membuat sebuah program meanmpilkan status gaji karyawan. Maka saya memasukan syntax:
```
gaji = int(input("Masukan Gaji : "))
berkeluarga = (False, True) [input("Sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True) [input("Punya Rumah? (Y/T)") == "Y"]

if gaji > 3000000:
    print("Gaji Sudah Diatas UMR")
    if berkeluarga:
        print("Wajib Ikutan Asuransi Dan Menabung Untuk Pensiun")
    else:
        print("Tidak Perlu Ikutan Asuransi")
        if punya_rumah:
            print("Wajib Bayar Pajak Rumah")
        else:
            print("Tidak Wajib Bayar Pajak Rumah")

else:
    print("Gaji Belum UMR")

```

Jika sudah memasukan semua syntax diatas dan telah di run, maka kamu akan mendapatkan tampilan seperti gambar yang ada dibawah ini

![Foto Lat2](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7_MODUL_PRAKTIKUM2/blob/main/Modul%20Praktikum%202/Latihan2.png) <br>

* LATIHAN 3

Di latihan 3 ini saya di suruh membuat sebuah program dimana ketika kita menginput kan data, outputnya akan mengahasilkan outputan dengan nilai data tersebut merupakan nilai benar/salah, dengan syarat bawah 2 bilangan tersebut hasilnya sama dengan yang lain nya (sederhana nya 2 bilangan harus bernilai sama)

Pada syntax kali ini saya membuat 3 inputan data seperti di bawah ini :

```
#!/usr/bin/python3

a = int(input("Masukkan Nilai A : "))
b = int(input("Masukkan Nilai B : "))
c = int(input("Masukkan Nilai C : "))

if a+b == c or b+c == a or c+a == b:
    print("BENAR")
else:
    print("SALAH")
```

Jika sudah memasukan semua syntax diatas dan telah di run, maka kamu akan mendapatkan tampilan seperti gambar yang ada dibawah ini

![Foto Lat3](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7_MODUL_PRAKTIKUM2/blob/main/Modul%20Praktikum%202/Latihan3.png) <br>

## TUGAS PRAKTIKUM 2

![Foto Lat3](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7_MODUL_PRAKTIKUM2/blob/main/Modul%20Praktikum2/Tugas.png) <br>

Di tugas ini, saya di suruh membuat program dimana data akhirnya menampilkan bilangan terbesar.

untuk itu saya menulis syntax seperti ini:

```
a = int(input("Masukkan Nilai A : "))
b = int(input("Masukkan Nilai B : "))
c = int(input("Masukkan Nilai C : "))

if a>b and a>c:
    print("Nilai A Bilangan Terbesar")
elif b>a and b>c:
    print("Nilai B BIlangan Terbesar")
else:
    print("Nilai C BIlangan Terbesar")
```

Jika sudah memasukan semua syntax diatas dan telah di run, maka kamu akan mendapatkan tampilan seperti gambar yang ada dibawah ini

![Foto Lat2](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7_MODUL_PRAKTIKUM2/blob/main/Modul%20Praktikum%202/Tugas%20Praktikum2.png) <br>

* CONTOH FLOWCHARTNYA

![SSUSER](https://user-images.githubusercontent.com/72789338/98458976-9ca27380-21c8-11eb-9378-665dd1239794.jpeg)
 <br>

___________________________________________________________________________________________________
