from __future__ import print_function

def main():
    dict1 = {'satu':10, 'dua':20, 'tiga':30}
    dict2 = {'satu':10, 'dua':20}

    print("\ndict1: ", dict1)
    print("dict2: ", dict2)

    # sebelum elemen dihapus
    print("len(dict1): ", len(dict1))
    print("len(dict2): ", len(dict2))

    # setelah semua elemen dihapus
    dict1.clear()
    dict2.clear()

    print("\nlen(dict1): ", len(dict1))
    print("len(dict2): ", len(dict2))

if __name__ == '__main__':
    main()
    
    

