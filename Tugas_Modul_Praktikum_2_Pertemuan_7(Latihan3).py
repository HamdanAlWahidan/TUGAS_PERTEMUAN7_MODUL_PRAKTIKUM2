#!/usr/bin/python3

a = int(input("Masukkan Nilai A : "))
b = int(input("Masukkan Nilai B : "))
c = int(input("Masukkan Nilai C : "))

if a+b == c or b+c == a or c+a == b:
    print("BENAR")
else:
    print("SALAH")
