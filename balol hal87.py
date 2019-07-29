from __future__ import print_function

def main():
    # menampilkan informasi program
    print("Volume dan Luas permukaan program\n")

    # input panjang lebar tinggi
    p = float (raw_input("Masukkan panjang :"))
    l = float (raw_input("Masukkan lebar :"))
    t = float (raw_input("Masukkan tinggi"))

    # hasil kalkulasi
    V = p*l*t
    LP = 2 * (p*l + p*t + l*t)

    # menampilkan hasil
    print("Volume balok adalah \t: ", V)
    print("Luas permukaan balok adalah \t:", LP)

if __name__ == "__main__":
   main()


