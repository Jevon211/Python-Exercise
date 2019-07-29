from __future__ import print_function

x = set([1, 2, 3])
y = set([3, 4])
a = x | y              # union
print(a)

b = x & y              # intersection
print(b)

c = x - y              # difference
print(c)

d = x ^ y              # symetric difference
print(d)

