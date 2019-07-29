from __future__ import print_function

def main() :
    # input nilai x dan y
    print("Masukkan data koordinat :")
    x = int(raw_input("Masukkan nilai x :"))
    y = int(raw_input("Masukkan nilai y :"))

    info = "Koordinat (" + str(x) + "," + str(y) + ")berada pada kuadran"

    # memeriksa nilai x dan y 
    if x > 0 and y > 0 :
       print(info + "I")
    elif x < 0 and y > 0 :
       print(info + "II")
    elif x < 0 and y < 0  :
       print(info + "III") 
    else :
       print(info + "IV")

if __name__ == "__main__":
    main()


