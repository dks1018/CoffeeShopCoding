myList = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

newString = " Mississippi ".join(numbers)

print(newString)

fruit = {
    "Orange":"Orange juicy citrus fruit",
    "Apple":"Red juicy friend",
    "Lemon":"Sour citrus fruit",
    "Lime":"Green sour fruit"
         }
veggies = {
    "Spinach":"Katia does not like it",
    "Brussel Sprouts":"No one likes them",
    "Brocolli":"Makes people gassy"
}

veggies.update(fruit)
print(veggies)

superDictionary = fruit.copy()
superDictionary.update(veggies)
print(superDictionary)

while True:
    user_input = str(input("Enter Fruit or Veggie: "))
    if user_input == "quit":
        break
    if user_input in superDictionary or fruit or veggies:
        print(superDictionary.get(user_input))
    if user_input not in superDictionary and fruit and veggies:
        print("Hey that item is not in the list, but let me add it for you!!")
        
        fruit_veggie = str(input("Enter your Fruit or Veggie: "))
        desc = str(input("Enter the taste: "))
        
        superDictionary[fruit_veggie] = desc
        print(superDictionary[fruit_veggie])