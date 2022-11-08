fruit = {
    "Orange":"Orange juicy citrus fruit",
    "Apple":"Red juicy friend",
    "Lemon":"Sour citrus fruit",
    "Lime":"Green sour fruit"
         }

# print(fruit.items())
f_tuple = tuple(fruit.items())
# print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)
    
print(dict(f_tuple))
ordered_key = list(fruit.keys())
ordered_key.sort()
for f in ordered_key:
    print(f + " - " + fruit[f])

ordered_key = sorted(list(fruit.keys()))
for f in ordered_key:
    print(f + " - " + fruit[f])

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

for val in fruit.values():
    print(val)

print('-' * 40)
for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print('-' * 40 )

while True:
    dict_keys = input("Please enter a fruit: ")
    if dict_keys == "quit":
        break
    if dict_keys in fruit:
        description = fruit.get(dict_keys)
        print(description)
    else:
        print("We don't have a " + dict_keys)

print(fruit)
print(fruit["Lemon"])
fruit["Pair"] = "An odd shaped apple that is green"
print(fruit)
del fruit["Lemon"]
print(fruit)
fruit.clear()
print(fruit)