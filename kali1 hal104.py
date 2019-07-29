from __future__ import print_function

def main() :
    # menampilkan judul program 
    print(" Mengalikan dua bilangan")

    #meminta user memasukan bilangan
    a = int(raw_input("\nMasukkan var ke-1 : "))
    b = int(raw_input("\nMasukkan var ke-2 : "))

    #menghitung perkalian bilangan
    hasilkali = 0
    for i in range (0, b):
        hasilkali += a 
    
    #menampilkan hasil kali
    print("\n%d x %d = %d" % (a, b, hasilkali))

if __name__ == "__main__":
   main()