from __future__ import print_function

def main():
    dict1 = {'satu':10, 'dua':20, 'tiga':30}

    a = dict1.items()
    b = dict1.keys()
    c = dict1.values()

    print("\ndict.items  : ", a)
    print("dict.keys   : " , b)
    print("dict.values : ", c)

if __name__ == '__main__':
    main()
    
