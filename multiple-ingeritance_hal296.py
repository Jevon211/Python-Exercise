from __future__ import print_function
# mendefinisikan kelas induk pertama
class Induk1(object):
    def __init__(self, a):
        self.a = a
    def cetakA(self):
        print("Nilai a\t= ", self.a)

# mendefinisikan kelas induk kedua
class Induk2(object):
    def __init__(self, b):
        self.b = b
    def cetakB(self):
        print("Nilai b\t= ", self.b)

# mendefinisikan kelas turunan
class Anak(Induk1, Induk2):
    def __init__(self, a, b, c):
        # memanggil induk1 init
        Induk1.__init__(self, a)
         

        #memanggil induk2 init
        Induk2.__init__(self, b)
        self.c = c

    def cetakC(self):
        print("Nilai c\t= ", self.c)

def main():
    # membuat objek dari kelas Anak
    obj = Anak(111, 222, 333)

    # memanggil metode kelas Induk1 dari obj
    obj.cetakA()

    # memanggil induk 2
    obj.cetakB()

    # memanggil anak
    obj.cetakC()

if __name__ == '__main__':
    main()
    
