from __future__ import print_function

def main():
    #menampilkan fungsi program
    print("Mencari maks dari tiga variabel \n ")
    
    #input tiga variabel
    a = int (raw_input("Masukkan var ke-1 : "))
    b = int (raw_input("Masukkan var ke-2 : "))
    c = int (raw_input("Masukkan var ke-3 : "))

    # menentukan nilai maks
    if a > b:
        if a > c :
           maks = a
    else: 
        if b > c :
           maks = b
        else:
           maks = c
    
    #menampilkan nilai maksimum dari ketiga variabek
    print("Nilai maksumum adalah \t: %d" % maks)

if __name__ == "__main__":
   main()

    