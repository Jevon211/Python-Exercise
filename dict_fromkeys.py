from __future__ import print_function

def main():
    # mendefnisikan tuple t
    t = ('satu', 'dua', 'tiga')

    # membuat dictionary
    dict1 = dict.fromkeys(t, 40)

    print("dict1: ", dict1)

if __name__ == "__main__":
    main()