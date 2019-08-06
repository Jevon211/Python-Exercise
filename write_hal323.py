from __future__ import print_function

def main():
    # membuka file
    f = open("data.txt", "w")

    # menulis data ke dalam file
    f.write("Pemrograman Python\n")
    f.write("2015")

    # menutup file
    f.close()

if __name__ == '__main__':
    main()
    