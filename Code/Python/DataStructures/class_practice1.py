class Person():
    
    
    def __init__(self,name,DOB,height,weight):
        self.name = name
        self.DOB = DOB
        self.height = height
        self.weight = weight

Darius = Person("Darius", "10/18/1995","6 foot", 185)

   
print(Darius.name)
print(Darius.DOB)  
print(Darius.weight)
print(Darius.height)

Darius.name = "Darius Smith"
print(Darius.name)
