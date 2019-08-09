from __future__ import print_function
import geometri2D_hal356

def main():
    # persegi panjang
    p = 10
    l = 8

    luas = geometri2D_hal356.luasPersegiPanjang(p, l)
    kel = geometri2D_hal356.kelilingPersegiPanjang(p, l)

    print("PERSEGI PANJANG")
    print("Panjang\t: ", p)
    print("Luas\t: ", luas)
    print("Keliling\t= ", kel)

    # lingkaran
    jarijari = 3

    luas = geometri2D_hal356.luasLingkaran(jarijari)
    kel = geometri2D_hal356.kelilingLingkaran(jarijari)
    
    print("\nLINGKARAN")
    print("Keliling\t: ", kel)

if __name__ == '__main__':
    main()
    