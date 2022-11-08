# People list
people = ['Alex', (23, 178), 'Noah', (34, 189), 'Peter', (29, 175),
'John', (41, 185), 'Michelle', (35, 165)]

# Use for loop to print all information
for i in people:
  # Check if the elements type is tuple
  if type(i) is tuple: 
    # Iterate over this tuple
    for j in i: 
      # Print items of this tuple
      print(j) 
  else:
    # Print item if its type is not tuple
    print(i) 