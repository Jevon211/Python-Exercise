from __future__ import print_function
import math

# mendefinisikan kelas abstrak
class Bangun3D(object):
    # mendefinisikan metode abstrak
    def cetakData(self):
        raise NotImplementedError

    def hitungVolume(self):
        raise NotImplementedError

    def cetakVolume(self):
        raise NotImplementedError

# mendefnisikan kelas konkrit yang merupakan turunan dari kelas abstrak
class Kotak(Bangun3D):
    def __init__(self, p, l= None, t=None):
        if l == None and t == None:
            # jika berupa Kubus
            self.panjang = self.lebar = self.tinggi = p
        else:
            # jika berupa balok
            self.panjang = p
            self.lebar = l
            self.tinggi = t

    # mengimplementasikan metode cetakData()
    def cetakData(self):
        print("Panjang\t: ", self.panjang)
        print("Lebar\t: ", self.lebar)
        print("Tinggi\t: ", self.tinggi)

    # mengimplementasikan metode hitung volume()
    def hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi

    # mengimplementasikan metode cetakVolume()
    def cetakVolume(self):
        print("Volume kotak\t= ", self.hitungVolume())

class Tabung(Bangun3D):
    def __init__(self, r, t):
        self.jarijari = r
        self.tinggi = t

    def cetakData(self):
        print("jari-jari alas\t :", self.jarijari)
        print("tinggi tabung\t :", self.tinggi)

    def hitungVolume(self):
        return math.pi * self.jarijari * self.jarijari * self.tinggi

    def cetakVolume(self):
        print("Volume tabung\t :", self.hitungVolume())

def main():
    
    obj1 = Kotak(6, 5, 4)
    print("Balok")
    obj1.cetakData()
    obj1.cetakVolume()

    obj2 = Kotak(5, 5, 5)
    print("Kubus")
    obj2.cetakData()
    obj2.cetakVolume()

    obj3 = Tabung (3, 4)
    print("Tabung")
    obj3.cetakData()
    obj3.cetakVolume()

    

if __name__ == '__main__':
    main()
    



    

