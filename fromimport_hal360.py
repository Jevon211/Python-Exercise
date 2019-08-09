from __future__ import print_function
from geometri2D_hal356 import luasPersegiPanjang

def main():
    p = 10
    l = 8

    luas = luasPersegiPanjang(p, l)

    print("PERSEGI PANJANG")
    print("Panjang\t: ", p)
    print("Lebar\t: ", l)
    print("Luas\t= ", luas)

if __name__ == '__main__':
    main()
    