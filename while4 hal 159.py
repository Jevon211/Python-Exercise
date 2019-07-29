from __future__ import print_function

def main():
    # Menentukan pengulangan
    ch = 'a'
    while ch <= 'z' :  
       print("%c :  Hello World ! " %ch)
       ch = chr(ord(ch) + 1)

if __name__ == "__main__":
    main()