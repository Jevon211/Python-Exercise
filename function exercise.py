from __future__ import print_function

def printNoLine(p):
    "Mencetak teks dan bilangan tanpa baris baru"
    print(p, end='')
    return          # opsional (bisa ditulis, bisa juga tidak)

def addByOne(p):
    "Menambah bilangan p dengan nilai 1"
    value = p + 1
    return value

# fungsi tanpa parameter :
 def clearscreen():
     os.system("cls")
     