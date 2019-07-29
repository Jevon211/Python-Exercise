from __future__ import print_function

def main():
   # membuat list
   buah = ["durian", "mangga", "apel"]
   print("Sebelum dihapus:")
   print(buah)

   # menghapus elemen dari list
   buah.remove("durian")
   buah.remove("apel")

   # menampilkan hasil setelah dihapus
   print("\nSetelah dihapus:")
   print(buah)

if __name__ == "__main__":
   main()
   