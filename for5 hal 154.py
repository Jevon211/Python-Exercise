from __future__ import print_function

def main():
    # menggunakan for menggunakan indeks karakter
    for i in range(ord('a'), ord('d')):
        print("%c: Hello World!" % chr(i))

if __name__ == "__main__":
    main()

