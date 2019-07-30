from __future__ import print_function

def main():
    dict1 = {'dua': 20, 'satu':10, 'tiga':30}
    dict2 = {'dua': 20, 'satu':10}
    dict3 = {'dua': 20, 'satu':10, 'tiga':30}

    print("dict1: ", dict1)
    print("dict2: ", dict2)
    print("dict3: ", dict3)

    print("\ncmp(dict1, dict3): ", cmp(dict1, dict3))
    print("cmp(dict2, dict3): ", cmp(dict2, dict3))
    print("cmp(dict1, dict2): ", cmp(dict1, dict3))

if __name__ == '__main__':
    main()
    