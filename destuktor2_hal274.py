from __future__ import print_function

# mendefinisikan kelas
class MyFile(object):
    def __init__(self, namafile):
        # mengakses file
        self.file = open(namafile)
    def __del__(self):
        # menutup file
        print("\n\nMenutup file...")
        self.file.close()
    def bacadata(self):
        for baris in self.file:
            print(baris, end=" ")

def main():
    # membuat objek dar kelas MyFile
    f = MyFile("Users/jevonedmund/matkul2.txt")

    # memanggil1 metode bacadata()
    f.bacadata

if __name__ == '__main__':
    main()
    