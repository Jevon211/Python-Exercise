from __future__ import print_function

def main():
    # menampilkan fungsi program
    print("Mengonversi detik ke jam\n ")

    #input total detik
    totaldetik = int(raw_input("Masukkan total detik \t:"))
    
    # melakukan konversi
    mm = totaldetik // 3600
    sisadetik = totaldetik % 3600
    mm = sisadetik // 60
    ss = sisadetik % 60

    # menampilkan hasil konversi
    print("%d detik sama dengan %d:%d:%d" % (totaldetik, hh, mm, ss))

if __name__ == "__main__":
   main()