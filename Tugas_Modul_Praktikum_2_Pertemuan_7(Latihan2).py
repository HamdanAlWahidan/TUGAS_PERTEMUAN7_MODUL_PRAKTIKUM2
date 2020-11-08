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
