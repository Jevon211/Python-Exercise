from __future__ import print_function
import sys      #untuk fungsi exit()
import math     #untuk fungsi sqrt()

def main():
    # menampilkan judul program
    print("Akar-akar persamaan kuadrat\n ")

    # input variabel
    a = int(raw_input("Masukkan var ke-1 :"))
    b = int(raw_input("Masukkan var ke-2 :"))
    c = int(raw_input("Masukkan var ke-3 :"))

    #menghitung diskriminan
    D = (b*b)-(4*a*c)

    if D < 0 :
        print("Akar-akar imajiner ")
        sys.exit(1) #keluar program
    elif D == 0 :
        x1 = (-b + math.sqrt (D)) / (2*a)
        x2 = x1
    else :
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)

    #Menampilkan akar persamaan
    print("\nx1 = %d" % x1)
    print("\nx2 = %d" % x2 )
 
if __name__ == "__main__":
   main()




