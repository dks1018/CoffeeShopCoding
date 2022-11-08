# People dictionary
people_dict = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175)}
people_dict["John"] = (41, 185)
people_dict["Michelle"] = (35, 165)

# Construct for loop to print information about people
for i in people_dict.keys():
  print("Name:", i)
  print("Age:", people_dict[i][0])
  print("Height:", people_dict[i][1])
  # Please, do not delete the delimiter below
  print("---------")