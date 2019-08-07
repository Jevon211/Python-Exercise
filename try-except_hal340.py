from __future__ import print_function

# mengimpor modul sys untuk exit()
import sys

def main():
    print("PROGRAM PEMBANGIAN BILANGAN")
    a = float(raw_input("Masukkan a\t: "))
    b = float(raw_input("Masukkan b\t: "))

    try:
        hasil = a/b
    except ZeroDivisionError:
        print("\nERROR: Nilai b tidak boleh nol")
        sys.exit(1)

    print("a / b: ", hasil)

if __name__ == '__main__':
    main()
    




    

