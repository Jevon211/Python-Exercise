from __future__ import print_function

def main():
    print("PROGRAM PEMBAGIAN BILANGAN")

    try:
        a = float(raw_input("Masukkan a:"))
        b = float(raw_input("Masukkan b:"))

        hasil = a / b
    
    # mengantisipasi pembagian dengan 0
    except ZeroDivisionError:
        print("\nError: Nilai b tidak boleh nol")
    
    # mengantisipasi variabel a atau b belum diiisi
    except ValueError:
        print("\nError: a dan b harus berupa angka")

    # mengantisipasi variabel a atau b belum diisi
    except KeyboardInterrupt:
        print("\nError: jangan tekan Ctrl+C!")

    else:
        print("\na : ", a)
        print("b : ", b)
        print("a / b = ", hasil)

if __name__ == '__main__':
    main()
    

    