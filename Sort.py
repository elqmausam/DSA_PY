from heapq import heapify, heappush, heappop

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def Print_LL(self):
        if self.head is None:
            print("1")

        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n = n.ref
    
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            if n.ref is not None:
                n = n.ref
            n.ref = new_node


LL1 = LinkedList()
LL1.add_begin(100)
LL1.add_begin(90)
LL1.add_end(95)
LL1.Print_LL()

        
        