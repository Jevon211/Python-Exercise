from __future__ import print_function
import sys

class Array(object):
    def __init__(self, arr=[]):
        self.data = arr
    def salin(self):
        temp = Array(self.data)
        return temp
    def tambah(self, nilai):
        if self.data.count > 0:
            if type(self.data[0]) == type(nilai):
                self.data.append(nilai)
            else:
                print("Nilai yang ditambahkan harus sejenis")
                sys.exit(1)
    def ubah(self, indeks, nilai):
        self.data[indeks] = nilai
    def hapus(self, nilai):
        self.data.remove(nilai)
    def cari(self, nilai):
        return self.data.index(nilai)
