from __future__ import print_function

class Kotak(object):
    def __init__ (self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

    def hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi

    def cetakData(self):
        print("Panjang\t :", self.panjang)
        print("Lebar\t: ", self.lebar)
        print("Tinggi\t: ", self.tinggi)

    def cetakVolume(self):
        print("Volume\t= ", self.hitungVolume())

# mendefinisikan kelas turunan(subClass)
class KortakWarna(Kotak):
    def __init__(self, p, l, t, w):
        # memanggil Kotak.__init__()
        super(KortakWarna, self).__init__(p, l, t)
        # menambah atribut baru
        self.warna = w

    def cetakData(self):
        super(KortakWarna, self).cetakData()
        print("Warna\t: ", self.warna)


def main():

    kotakwarna1 = KortakWarna(6, 5, 4, "merah")

    kotakwarna1.cetakData()
    kotakwarna1.cetakVolume()

if __name__ == '__main__':
    main()
    

    
