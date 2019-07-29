from __future__ import print_function

def main():
    #menentukan judul program
    print("Menghitung Nilai rata-rata")

    #menyiapkan list
    data = [] #menampung list angka 

    #jumlah bilangan (data) yang akan diinput
    n = int(raw_input("Masukkan jumlah data n :"))

    print() #spasi baris

    jumlah = 0
    for i in range (0,n) :
       #meminta user mengisi data bilangan
       temp = int(raw_input("Masukkan data bilangan :"))
    
    #menambah bilangan ke dalam list
    data.append(temp)

    #menghitung jumlah total bilangan
    jumlah += data[i]

    #menghitung rata-rata
    rata2 = jumlah / n

    #menampilkan hasil rata
    print("hasil rata2 adalah : %d" % rata2)

if __name__ == "__main__":
   main()

