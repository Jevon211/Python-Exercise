from __future__ import print_function
import numpy

def main():
    A, B = list(raw_input().split())
    
    C, D = list(raw_input().split())
   
    E = numpy.array([A, B])
    F = numpy.array([C, D])

    print (numpy.inner(E, F))
    print (numpy.outer(E, F))

if __name__ == '__main__':
    main()
    