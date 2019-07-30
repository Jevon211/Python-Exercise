from __future__ import print_function

def main():
    str1 = " Python"
    str2 = "Python33"
    str3 = "--PYTHON--"

    print("\nstr1 : ", str1)
    print("str1.lstrip(): ", str1.lstrip())

    print("\nstr2: ", str2)
    print("str2.rstrip(): ", str2.rstrip('3'))

    print("\nstr3: ", str3)
    print("str3.strip: ", str3.strip('-'))

if __name__ == '__main__':
    main()
    