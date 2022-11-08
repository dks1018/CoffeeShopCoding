class Node:
    def __init__(self,data,next=None): #constructor
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    
    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

#creating a single node
first = Node(3)
print(first.data)

# linked list with a single node
a = LinkedList()
a.head = Node(88)
print(a.head.data)

# using insert method to add nodes
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.printLL()