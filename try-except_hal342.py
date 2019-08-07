from __future__ import print_function
import sys

def main():
    print("PROGRAM PEMBAGIAN BILANGAN")
    a = float(raw_input("Masukkan a: "))
    b = float(raw_input("Masukkan b: "))

    try:
        hasil = a / b
    except ZeroDivisionError:
        print("\nError : Nilai b tidak boleh nol")

    # menampilkan hasil
    print("\na : ",a)
    print("b :", b)

    # menampilkan kesalahan NameError
    print("a/b = ", hasil)

if __name__ == '__main__':
    main()
    