from __future__ import print_function

def main():
    # membuka file
    f = open("data.txt", "r")

    # membaca data tiap baris
    while True:
        baris = f.readlines()
        if not baris:    #EOF(End of file):
            break
        print(baris, end='')

    # menutup file
    f.close()

if __name__ == '__main__':
    main()
    
