from __future__ import print_function

def main():
    # menampilkan judul program
    print("Menentukan maksimal dua bilangan\n ")

    #input dua variabel
    a = int (raw_input("Masukkan Var-1 \t: "))
    b = int (raw_input("Masukkan Var-2 \t: "))

    # Mencari nilai max dari kedua variabel

    if a > b : 
        maks = a
    else:
        maks = b`

    # Menampilkan variabel maksimal 
    print("\nNilai maksimum adalah %d" % maks)

if __name__ == "__main__":
  main()
