class person:
    age = 0
    initialAge = 24
    gender = "male"
    height = "6 foot 0 inches"

newPerson = person()
print(newPerson.age)
print(newPerson.height)

class people:
    def __init__(self,name,age):
        self.name = name
        self.age = age

new_people = people("Katia",22)
print(new_people.name)
print(new_people.age)

myself = people("Darius",24)
print(myself.name)
print(myself.age)

print("Hi my name is " + str(myself.name) + " and I am " + str(myself.age) + " years old.")