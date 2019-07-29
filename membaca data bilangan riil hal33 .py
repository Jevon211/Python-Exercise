from __future__ import print_function

def main():
    # membuat prompt untuk tipe data float
    bilriil = float(input("Masukkan bilangan riil"))

    # menggunakan variabel untuk melakukan perhitungan
    hasil = bilriil*2

    # menampilkan nilai variabel
    print("Bilangan yang dimasukkan adalah %f" % bilriil)
    print("%f x 2 = %f " % (bilriil, hasil))

if __name__ == "__main__":
   main()