from __future__ import print_function

# mendefinisikan kelas Node (simpul)
class Node:
     def __init__(self, element, next=None):
         self.element = element
         self.next = next

# mendefinisikan kelas Linkedlist
class Linkedlist:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    def isEmpty (self) :
        return self.size == 0
    def addFirst(self, element) : 
        if self.isEmpty():
            self.front = Node(element)
            self.back = self.front
        else :
            temp = self.front
            self.front = Node (element, temp)
        self.size += 1
    def addLast (self, element):
        if self.isEmpty():
           self.front = Node(element)
           self.back = self.front
        else :
            self.back.next = Node(element)
            self.back = self.back.next
        self.size += 1
    def printList(self):
        print("Isi linked list:")
        current = self.front
        while current != None:
            print (current.element)
            current = current.next

def main():
    #membuat objek dari kelas LinkeList
    li = Linkedlist()

    #menambah elemen di awal
    li.addFirst(10)

    #menambah elemen di akhir
    li.addLast(20)
    li.addLast(30)

    #menambah elemen di akhir
    li.addFirst(90)

    #menampilkan semua nilai node dalam lnked list
    li.printList()

if __name__ == "__main__":
   main()