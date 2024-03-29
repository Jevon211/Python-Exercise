from __future__ import print_function

def printlist(li):
    for e in li:
        print(e, end='')
    print()

def main():
    bilangan = xrange(20)
    genap = []
    ganjil = []

    for x in bilangan:
        if x % 2 == 0:
            genap.append(x)
        else:
            ganjil.append(x)

    print("Bilangan genap\t: ", end='')
    printlist(genap)
    print("Bilangan ganjil\t: ", end='')
    printlist(ganjil)

if __name__ == "__main__":
    main()
