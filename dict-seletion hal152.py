from __future__ import print_function

def main() : 
    # membuat dictionary
    hari = {
             1 : "Minggu",
             2 : "Senin",
             3 : "Selasa",
             4 : "Rabu",
             5 : "Kamis",
             6 : "Jumat",
             7 : "Sabtu"
           }
    nohari = int(raw_input("Masukkan nomor hari : "))
    
    print("Hari ke-%d adalah %s" % (nohari,hari[nohari]))

if __name__ == "__main__":
    main()