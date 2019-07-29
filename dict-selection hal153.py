from __future__ import print_function

# mendefinisikan fungsi tambah()
def tambah (a, b):
    return a + b

# fungsi kurang()
def kurang (a, b):
    return a - b

# fungsi kali()
def kali (a, b):
    return a * b

# fungsi bagi()
def bagi (a, b):
    return a / b

def main():
    a = float(raw_input("Masukkan bilangan ke-1: "))
    b = float(raw_input("Masukkan bilangan ke-2: "))
    op = raw_input("Masukkan operator : ")

    # membuat dictionary yang nilainya berupa fungsi
    d = {
        '+' : tambah (a, b),
        '-' : kurang (a, b),
        'x' : kali (a, b),
        ':' : bagi (a,b)
    }

    print("\n%f %s %f = %f" % (a, op, b , d[op]))

if __name__ == "__main__":
    main()