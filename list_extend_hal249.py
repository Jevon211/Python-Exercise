from __future__ import print_function 

def main():
    list1 = [10, 20, 30]

    print("Sebelum ditambah: ")
    print("list1: ", list1)

    # menambah elemen berupa list
    list1.extend([40, 50])
    list1.extend((60, 70, 80))

    print("Setelah ditambah: ")
    print("list1: ", list1)

if __name__ == '__main__':
    main()
    