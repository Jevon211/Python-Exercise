from __future__ import print_function

def main():
    print("PROGRAM PEMBAGIAN BILANGAN")
    
    try:
        a = float(raw_input("Masukkan a:"))
        b = float(raw_input("Masukkan b:"))

        hasil = a / b

    except (ZeroDivisionError, ValueError, KeyboardInterrupt):
        print("\nError: Anda telah melakukan kesalahan " + "kesalahan")
    else:
        print("\na : ", a)
        print("b : ", b)
        print("a / b: ", hasil)

if __name__ == '__main__':
    main()
    