from __future__ import print_function

# data sebagai [object]
type(12)
<type 'int'>

type(99.99)
<type 'float'>

type("Python")
<type 'string'>

type([1,2,3])
<type 'list'>

# kode sebagai [object]

# fungsi
def pangkat(a, b):
    return a * * b
type(pangkat)
<type 'function'>

# kelas
class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
type(Titik)
<type 'classobj'>

# instance
A = Titik(5,4)
type(A)
<type 'instance'>

# setiap objek memilik identitas, tipe, dan nilai.

a = 12
id(a)    #menampilkan identitas atau alamat memori objek
20708412

type(a)  #menampilkan tipe objek
<type 'int'>

print(a) #menampilkan nilai objek
12

# objek yang nilainya dapat diubah = objek list dan dictionary ( mutable )
# objek yang nilainya tidak dapat diubah = bilangan, string, dan tuple ( immutable )

# membuat objek list
li = [1,2,3]
id(li)          #menampilkan alamat memori
30665104
li      # menampilkan nilai
[1, 2, 3]

# mengubah nilai
li.extend([4,5,6,7])
id(li)              #menampilkan alamat memori
30665104
li          #menampilkan nilai
[1, 2, 3, 4, 5, 6, 7]

# membuat objek int
a = 12

id(a)  # menampilkan alamat memori
20708412

a      # menampikkan nilai 
12

# membuat objek baru (bukan mengubah nilai)
a = 15

id(a)   #menampilkan alamat memori
20708376

a       #menampilkan nilai
15

# membuat objek tuple ( immutable )
# elemennya lisy (mutable), nilai yang dapat diubah hanya elemennya saja

# membuat objek tuple
t = (['01','Pensil'],['02','Spidol'])

t 
(['01','Pensil'],['02','Spidol'])

# mengubah nilai elemen
t[0][1] = 'Penghapus'

t
(['01','Penghapus'], ['02','Spidol'])
