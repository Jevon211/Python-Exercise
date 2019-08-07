from __future__ import print_function

def main():
    # membuka file
    f = open("data.txt", "r")

    data = f.readlines()

    # mengambil elemen dari list
    for elemen in data:
        print(elemen, end='')

    f.close()

if __name__ == '__main__':
    main()
    