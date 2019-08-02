from __future__ import print_function

# mendefinisikan kelas

class Kotak(object):
    def __init__(self, p=0, l=0, t=0):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def setData(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi
    def cetakData(self):
        print("panjang\t: ", self.panjang)
        print("lebar\t: ", self.lebar)
        print("tinggi\t: ", self.tinggi)
        print("Volume\t =", self.hitungVolume())
    def cetakVolume(self):
        print("Volume\t =", self.hitungVolume())

def main():
    # membuat objek pertama dengan konstruktor tanpa
    # parameter
    kotak1 = Kotak(10, 8, 4)
    print("Objek pertama")
    kotak1.cetakData()
    kotak1.cetakVolume()

    kotak2 = Kotak(6, 5, 4)
    print("\nObjek Kedua")
    kotak2.cetakData()
    kotak2.cetakVolume()

if __name__ == '__main__':
    main()
    
    