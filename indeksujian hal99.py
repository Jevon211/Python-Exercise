from __future__ import print_function

def main():
    # menentukan judul program
    print("Menentukan indeks ujian\n")

    #input variabel
    uts = int(raw_input("Masukkan nilai uts :"))
    uas = int(raw_input("Masukkan nilai uas :"))

    #penentuan Nilai Indeks
    na = (0.65 * uas) + (0.35 * uts)

    if na >= 80 :
        indeks = 'A'
    elif na >= 70 :
        indeks = 'B'
    elif na >= 55 :
        indeks = 'C'
    elif na >= 40 :
        indeks = 'D'
    else :
        indeks = 'E'
    
    #menampilkan nilai indeks dan nilai akhir 
    print("\nNilai akhir : %0.2f" % na)
    print("Nilai indeks = %c" % indeks)

if __name__ == "__main__":
   main()