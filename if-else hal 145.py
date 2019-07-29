from __future__ import print_function

def main():
    # input untuk tipe integer
    bilangan = int(raw_input("Masukkan bilangan bulat :"))

    # membuat bilangan bulat / ganjil
    if bilangan % 2 == 0 :
       print("%d adalah bilangan genap" % bilangan)
    else :
       print("%d adalah bilangan ganjil" % bilangan)

if __name__ == "__main__":
   main()
       



