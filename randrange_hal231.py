from __future__ import print_function
import random

def main():
    # mengambil nilai acak 1 - 100
    print("random.randrange(1, 100): ", random.randrange(1, 100))

    # mengambil nilai acak 1 - 1000
    print("random.randrange(1, 1000): ", random.randrange(1, 1000))

    # mengambil nilai acak -100 - 0
    print("random.randrange(-100, 0): ", random.randrange(-100, 0))

if __name__ == '__main__':
    main()
    