# def python_food():
#     width = 80
#     text = "Spam and eggs"
#     left_margin = (width - len(text)) // 2
#     print(" " * left_margin, text)


def center(*args, sep=":"):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text



s1 = center("Darius Smith")
print(s1)
s2 = center("Darius Kavon Smith")
print(s1)
s3 = center("Darius Korey Kavon Smith")
print(s1)
s4 = center(12,10)
print(s4)
s5 = center("Katia", "Darius", "Gilligan", "Smith")
print(s5)

# print("Darius", "Smith", "Katia", "Gilligan", sep=" ")


# with open("centered", mode='w') as centered_file:

# print(center_text("Darius Smith")
# print(center_text("Darius Kavon Smith")
# print(center_text("Darius Kavon Korey Smith")
# print(center_text(12)
# print(center_text("First", "second", 3, 4, "spam", sep=":")

# call the function
# center_text("Darius Smith", file=centered_file)
# center_text("Darius Kavon Smith", file=centered_file)
# center_text("Darius Kavon Korey Smith", file=centered_file)
# center_text(12, file=centered_file)
# center_text("First", "second", 3, 4, "spam", sep=":", file=centered_file)
