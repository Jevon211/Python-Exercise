from __future__ import print_function

def main():
    # membuka file
    f = open("data.txt", "r")

    # membaca data 11 byte di dalam file
    s = f.read(11)

    print("DATA: ")
    print(s)

    # menutup file
    f.close()

if __name__ == '__main__':
    main()
    