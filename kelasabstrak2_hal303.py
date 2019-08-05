from __future__ import print_function
from abc import ABCMeta, abstractmethod
import math

# mendefinisikan kelas abstrak
class Bangun3D(object):
    __metaclass__ = ABCMeta
    # mendefinisikan metode abstrak
    @abstractmethod
    def cetakData(self):
        pass
    @abstractmethod
    def hitungVolume(self):
        pass
    @abstractmethod
    def cetakVolume(self):
        pass

# mendefinisikan kelas konkrit yang merupakan turunan dari kelas abstrak
class Kotak(Bangun3D):
    def __init__(self, p, l=None, t=None):
        if l == None and t == None:
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
        print("Volume \t :", self.hitungVolume())

class Tabung(Bangun3D):
    def __init__(self, r, t):
        self.jarijari = r
        self.tinggi = t
    
    def cetakData(self):
        print("Jari-Jari\t :", self.jarijari)
        print("Tinggi\t :", self.tinggi)

    def hitungVolume(self):
        return math.pi * self.jarijari * self.jarijari * self.tinggi

    def cetakVolume(self):
        print("Volume\t =", self.hitungVolume())

def main():

    obj1 = Kotak(6, 5, 4)
    print("Balok")
    obj1.cetakData()
    obj1.cetakVolume()

    obj2 = Kotak(5, 5, 5)
    print("Kubus")
    obj2.cetakData()
    obj2.cetakVolume()

    obj3 = Tabung(3, 4)
    print("Tabung")
    obj3.cetakData()
    obj3.cetakVolume()

if __name__ == '__main__':
    main()
    

    
    



    
