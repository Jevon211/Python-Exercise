from __future__ import print_function

def main():

    # menampilkan informasi prgram
    print(" Menukar Nilai antar Variabel\n")

    # input nilai
    a = (raw_input("Masukkan var 1 : "))
    b = (raw_input("Masukkan var 2 : "))
    

    # Menampilkan data sebelum diswap
    print("\nSebelum menukar nilai")
    print("Var ke-1  \t: ", a)
    print("Var ke-2  \t: ", b)

    # rumus swap
    c = a
    a = b
    b = c

    # menampilkan variabel setelah diswap
    print("\nVariabel swap")
    print("Var ke-1 \t:", a)
    print("Var ke-2 \t:", b)

if __name__ == "__main__":
   main()