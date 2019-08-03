from __future__ import print_function

def main():
    n = int(raw_input())

    for i in range (1, n + 1):
        n += 1
        print(i, end='')

if __name__ == '__main__':
    main()
    