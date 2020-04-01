
#for i in range(1, 13):
 #   print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i , i ** 2, ** 3))
    
print("Pi is about: {0:12}".format(22 / 7))
print("Pi is about: {0:12f}".format(22 / 7))
print("Pi is about: {0:12.50f}".format(22 / 7))
print("Pi is about: {0:52.50f}".format(22 / 7))
print("Pi is about: {0:62.50f}".format(22 / 7))
print("Pi is about: {0:72.50f}".format(22 / 7))

print()
age = 24
print("My age is {0} years".format(age))

print("There are {0} in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

phoneBook = {
    'Darius': 24,
    'Katia' : 22,
    'Sydney': 17,
    'Darrell': 50,
    'Michele': 50,
}


for n in enumerate(phoneBook.items()):
    print(n)
for n in phoneBook:
    print(n,"=", phoneBook[n])
for n in phoneBook:
    print("{0}={1}".format(n, phoneBook[n]))
for n in phoneBook:
    print(str(n)+'='+str(phoneBook[n]))
for n in phoneBook:
    print(str(n),'=',str(phoneBook[n]))