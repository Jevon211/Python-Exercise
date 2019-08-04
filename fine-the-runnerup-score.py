from __future__ import print_function





def main():
    a =[]
    n = map(int, raw_input().split())
    for i in range (1, n+1):
        b = int(raw_input())
        a.append(b)
    a.sort()

    print (a[n-2])


if __name__ == '__main__':
    main()
    