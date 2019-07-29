from __future__ import print_function

def main():
    bilangan = int(raw_input("Masukkan bilangan bulat: "))

    # memeriksa bilangan, genap atau tidak
    if bilangan %2 == 0 :
       print("%d adalah bilangan genap" % bilangan)

if __name__ == "__main__":
    main()

    