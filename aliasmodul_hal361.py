from __future__ import print_function
import geometri2D_hal356 as duaD

def main():
    p = 10
    l = 8

    luas = duaD.luasPersegiPanjang(p, l)

    print("PERSEGI PANJANG")
    print("Panjang\t: ", p)
    print("Lebar\t: ", l)
    print("Luas\t: ", luas)

if __name__ == '__main__':
    main()
    