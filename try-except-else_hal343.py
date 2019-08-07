from __future__ import print_function

def main():
    print("PROGRAM PEMBAGIAN BILANGAN")

    a = float(raw_input("Masukkan a: "))
    b = float(raw_input("Masukkan b: "))

    try:
        hasil = a / b
    except ZeroDivisionError:
        print("\nERROR: Nilai b tiak boleh nol")
    else:
        print("\na :", a)
        print("b :", b)
        print("a / b = ", hasil)

if __name__ == '__main__':
    main()
    