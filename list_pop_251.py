from __future__ import print_function

def main():
    list1 = [10, 20, 30, 40, 50]
    
    print("Sebelum diambil")
    print("list : ", list1)

    list1.pop()
    list1.pop()

    print("\nSetelah diambil")
    print("list1: ", list1)

if __name__ == '__main__':
    main()
    