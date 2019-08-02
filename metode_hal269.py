from __future__ import print_function

class Kotak(object):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi
    def cetakData(self):
        print("Panjang\t: ", self.panjang)
        print("Lebar\t: ", self.lebar)
        print("Tinggi\t: ", self.tinggi)
    def cetakVolume(self):
        print("Volume\t= ", self.hitungVolume())

def main():
    # membuat objek pertama
    kotak1 = Kotak(6, 4, 3)

    # menggunakan objek pertama
    print("Object kotak1")
    kotak1.cetakData()
    kotak1.cetakVolume()

    # membuat objek kedua
    kotak2 = Kotak(5, 3, 2)
    
    # menggunakan ibjek kedua
    print("\nObject kotak2")
    kotak2.cetakData()
    kotak2.cetakVolume()

if __name__ == '__main__':
    main()
    


    