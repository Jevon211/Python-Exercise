from __future__ import print_function
import math

def main():

    # menampilkan informasi program
    print("Informasi Suhu (Fahrenheit ke Celcius)\n")
    
    # input suhu dalam Fahrenheit
    F = float (raw_input("Masukkan suhu Fahrenheit :"))

    # melakukan conversi ke suhu C
    C = 5 * (F - 32)/9

    # menampilkan hasil konversi ke layar
    print("Fahrenheit \t:", F)
    print("Celcius \t:", C)

if __name__ == "__main__":
   main()