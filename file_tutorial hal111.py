from __future__ import print_function

def main():
    # mengakses file
    f = open("sample.txt")  #mengambilkan objek file
    line = f.readline()     #membaca baris pertama
    while line :
        print(line, end='')
        line = f.readline       #membaca baris berikutnya

    # menutup file
    f.close()

if __name__ == "__main__":
   main()