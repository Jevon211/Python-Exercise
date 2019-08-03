from __future__ import print_function

def is_leap(year):
    leap = False
    year = int(raw_input())
    

    if year % 4 == 0 and year % 100 != 0:
        print(leap)
    elif year % 400 == 0:
        print(leap)
    else :
        True

    return leap

def main():
    print (is_leap("%d", % year))

if __name__ == "__main__":
    main()
    