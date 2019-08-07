from __future__ import print_function

def main():
    # membuka file
    f = open("data.txt", 'r')

    print("Sebelum file dibaca")
    print("Posisi file: ", f.tell())

    data1 = f.read(11)

    print("\nSetelah file dibaca 11 byte")
    print("data1: '", data1, "'")
    print("Posisi file: ", f.tell())

    data2 = f.read(7)
    print("\nSetelah file dibaca 7 byte")
    print("data2: '", data2, "'")
    print("Posisi file: ", f.tell())

if __name__ == '__main__':
    main()
    