from __future__ import print_function

def main():
    # menentukan banyak pengulangan 
    n = int(raw_input("Masukkan banyak pengulangan : "))

    #menentukan pengulangan
    i = 0
    while i <= n :
        print("Baris ke-%i : Hello word!" %i)
        i += 1

if __name__ == "__main__":
    main()
