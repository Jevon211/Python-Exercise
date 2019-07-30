from __future__ import print_function
import random

def main():
    li = [10, 20, 30, 40, 50]

    print("li: ", li)

    print("Pemanggilan pertama: ")
    print("random.choice(li): ", random.choice(li))

    print("\nPemanggilan kedua: ")
    print("random.choice(li): ", random.choice(li))

    print("\nPemanggilan ketiga: ")
    print("random.choice(li): ", random.choice(li))

if __name__ == '__main__':
    main()
    