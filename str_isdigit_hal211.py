from __future__ import print_function

def isnumeric():
    if isnumeric:
        return False
    else:
        True


def main():
    str1 = "thesecret2006"
    str2 = '0123456789'

    print("str1: " + str1)
    print("str2: " + str2)

    print("\nstr1.isdigit(): ", str1.isdigit())
    print("\nstr1.isnumeric(): ", isnumeric())
    
    print("\nstr2.isdigit(): ", str2.isdigit())
    print("str2.isnumeric():", isnumeric())

if __name__ == '__main__':
    main()
    