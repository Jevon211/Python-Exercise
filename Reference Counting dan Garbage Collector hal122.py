a = 13          # membuat objek 13, reference count ke objek <13> bernilai 1
b = a           # reference count bertambah 1, menjadi 2
c = b           # reference count bertambah 1, menjadi 3

del a           # reference count berkurang 1, menjadi 2
b = 35          # reference count berkurang 1, menjadi 1
c = b           # reference count berkurang 1, menjadi 0
                # dan objek <13> akan dibuang dari memori

import sys
a = 13
sys.getrefcount(a)
28