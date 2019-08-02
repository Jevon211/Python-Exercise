from __future__ import print_function

def main():
    list1 = [10, 20, 30]
    list2 = [10, 20]
    list3 = [10,20,30]

    print("list1: ", list1)
    print("list2: ", list2)
    print("list3: ", list3)

    a = cmp(list1, list3)
    b = cmp(list2, list3)
    c = cmp(list1, list2)

    print("\ncmp1: ", a)
    print("cmp2: ", b)
    print("cmp3: ", c)

if __name__ == '__main__':
    main()
    