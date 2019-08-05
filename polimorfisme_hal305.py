from __future__ import print_function
from abc import ABCMeta, abstractmethod
import math

# mendefinisikan kelas abstrak
class Bangun3D(object):
    def cetakData(self):
        raise NotImplementedError

    def hitungVolume(self):
        raise NotImplementedError

    def cetakVolume(self):
        raise NotImplementedError

class Kotak(Bangun3D):
    def __init__ (self, p, l = None, t = None):
        if l == 0 and t == 0:
            self.panjang = self.lebar = self.tinggi = p
        else:
            self.panjang = p
            self.lebar = l
            self.tinggi = t

    def cetakData(self):
        print("Panjang\t :", self.panjang)
        print("Lebar\t :", self.lebar)
        print("Tinggi\t :", self.tinggi)

    def hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi

    def cetakVolume(self):
        print("Volume\t =", self.hitungVolume())

class Tabung(Bangun3D):
    def __init__(self,r, t):
        self.jarijari = r
        self.tinggi = t

    def cetakData(self):
        print("Jari - jari\t :", self.jarijari)
        print("Tinggi\t :", self.tinggi)

    def hitungVolume(self):
        return math.pi * self.jarijari * self.jarijari * self.tinggi

    def cetakVolume(self):
        print("Volume\t =", self.hitungVolume())

def main():
    obj = Kotak(6, 5, 4)
    print("Balok")
    obj.cetakData()
    obj.cetakVolume()

    del obj  # menghapus obj secara manual

    obj = Kotak(5, 5, 5)
    print("Kubus")
    obj.cetakData()
    obj.cetakVolume()

    del obj

    obj = Tabung(3, 4)
    print("Tabung")
    obj.cetakData()
    obj.cetakVolume()

if __name__ == '__main__':
    main()
    

