from __future__ import print_function

def main() :
    # menampilkan fungsi program
    print("Konversi jam ke detik\n")

    #input jam , menit, dan detik
    hh = int(raw_input("Masukkan nilai jam :"))
    mm = int(raw_input("Masukkan nilai menit :"))
    ss = int(raw_input("Masukkan nilai detik :"))

    # konversijam ke detik
    totaldetik = (hh*3600)+(mm*60)+ss

    # Menampilkan hasil konversi
    print("%d:%d:%d sama dengan %d detik" % (hh, mm, ss, totaldetik))

if __name__ == "__main__":
   main()