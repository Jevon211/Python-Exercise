from __future__ import print_function

def main() :
    try:
        filename = "contoh.txt"
        # membuka file
        f = open(filename)      #mungkin akan memunculkan eksepsi IOError

        # membaca file
        f.close()
    except IOError as e:
        print("File '%s' tidak ditemukan " % filename)
        sys.exit()

if __name__ == "__main__":
    main()