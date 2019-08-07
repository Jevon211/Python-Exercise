from __future__ import print_function
import os

def main():
    s = os.getcwd

    print("Direktori akfit: ", s)

    os.chdir("iCloud Drive/Documents/")

    s1 = os.getcwd

    print("\nSetelah direktori dubah")
    print("Direktori aktif: ")

if __name__ == '__main__':
    main()
    

