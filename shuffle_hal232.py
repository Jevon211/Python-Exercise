from __future__ import print_function
import random

def main():
    li1 = [10, 20, 30, 40, 50]
    li2 = ['Joni','Arif','Ridho','Awan']

    # sebelum diacak
    print("li1: ", li1)
    print("li2: ", li2)

    # setelah diacak
    print("random.shuffle(li1): ", random.shuffle(li1))
    print("random.shuffle(li2): ", random.shuffle(li2))

if __name__ == '__main__':
    main()
    