from __future__ import print_function

def generator(n):
    MAX = 2147483647
    while n < MAX:
            yield n
            n += 1
            
 g = generator (0)