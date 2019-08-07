from __future__ import print_function

def main():
    try:
        # membuka file
        f = open("data.txt: ", "w")

        try:
            # menulis data ke file
            f.write("Pemrograman Python")
        finally:
            f.close()

    except IOError:
        print("\nERROR: File tidak dapat" + "dibuka/ditulis")

if __name__ == '__main__':
    main()
    