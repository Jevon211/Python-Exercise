from __future__ import print_function

def main():
    #menentukan judul program
    print("Menghitung Nilai Faktorial\n")

    #meminta user memasukkan bilangan
    #yang akan dihitung faktorialnya
    n = int(raw_input("Masukkan nilai variabel : "))

    if n < 0 :
        print("n\Bilangan tidak boleh negatif")
        sys.exit(1)
    
    faktorial = 1 #mula2 faktorial bernilai 1 ( 0! = 1)

    #menghitung faktorial
    print("%d! = " % n, end = '')
    i = n
    while i >= 1:
       if i != 1:
           print ("%d x " % i, end='')
       else :
           print ("%d = " % i, end='')
       faktorial *= i;
       i-= 1;  #decrement

    #menampilkan hasil
    print("faktorial : ", faktorial)

if __name__ == "__main__":
   main()
