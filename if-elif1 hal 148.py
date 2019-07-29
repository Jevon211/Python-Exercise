from __future__ import print_function

def main():
    #masukkan integer
    x = int(raw_input("Masukkan bilangan bulat \t : "))

    #statement control
    if x > 0:
       print("%d adalah bilangan positif" % x)
    elif x == 0:
       print("%d adalah bilangan 0" % x)
    else:
       print("%d adalah bilangan negatif" % x)

if __name__ == "__main__":
    main()

    

