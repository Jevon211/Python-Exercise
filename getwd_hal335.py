from __future__ import print_function
import os

def main():
    # mendapatkan informasi tentang direktori aktif
    s = os.getcwd()

    print("Direktori aktif: ", s)

if __name__ == '__main__':
    main()
    