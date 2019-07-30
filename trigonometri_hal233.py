from __future__ import print_function
import math

def main():
    sudut = 90  # dalam derajat

    y = math.sin(math.radians(sudut)) #sin
    x = math.degrees(math.asin(y))  #arcsin

    print("sin 90: ", y)
    print("arcsin 1: ", x)

if __name__ == '__main__':
    main()
    