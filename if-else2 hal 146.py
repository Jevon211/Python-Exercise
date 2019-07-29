from __future__ import print_function

def main():
    # masukkan nama hari
    namahari = ("minggu","senin","selasa","rabu","kamis","jumat","sabtu")

    # membuat prompt untuk tipe data string
    hari = raw_input("Masukkan nama hari : ")

    #compare hari
    if hari.lower() == namahari[0] or\
       hari.lower() == namahari[6]:
       print("%s adalah hari libur" % hari )
    else:
       print("%s adalah hari kerja (untuk karyawan)" % hari)

if __name__ == "__main__":
   main()

    


