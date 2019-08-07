from __future__ import print_function

def main():
    # membuka file
    f = open("data.txt", "r")

    # membaca seluruh baris, dan menampungnya ke dalam objek list
    data = f.readlines()

    print(data)

    f.close()

if __name__ == '__main__':
    main()
    