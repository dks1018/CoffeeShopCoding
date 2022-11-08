import random

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
            
            
    def revLL(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

#creating a single node
# first = Node(3)
# print(first.data)

# linked list with a single node
a = LinkedList()
a.head = Node(0)
# print(a.head.data)

# using insert method to add nodes
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
a.insert(6)

#generate random number and insert them into the linked list
counter = 0
while counter < 5:
    n = random.randint(1,100000)
    a.insert(n)
    counter += 1
    
a.printLL()
print("-" * 70)
a.revLL()
a.printLL()

