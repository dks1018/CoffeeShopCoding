

# open files for reading
crypto1 = open("C:\\Users\\Darius\\Desktop\\BlackhatChallenge\\BlackHatChallenge1.txt","r")
crypto2 = open("C:\\Users\\Darius\\Desktop\\BlackhatChallenge\\BlackHatChallenge2.txt","r")
crypto3 = open("C:\\Users\\Darius\\Desktop\\BlackhatChallenge\\BlackHatChallenge3.txt","r")
crypto4 = open("C:\\Users\\Darius\\Desktop\\BlackhatChallenge\\BlackHatChallenge4.txt","r")
crypto5 = open("C:\\Users\\Darius\\Desktop\\BlackhatChallenge\\BlackHatChallenge5.txt","r")

# Set variables
letter_count = 0
word_count = 1
content1 = crypto1.read()
content2 = crypto2.read()
content3 = crypto3.read()
content4 = crypto4.read()
content5 = crypto5.read()

# Loops through the contents of the files
# Letter_count is the count of letter in the file
for i in content1:
    letter_count += 1
print("Crypto file 1:",letter_count)
    
for i in content2:
    letter_count += 1
print("Crypto file 2:",letter_count)

for i in content3:
    letter_count += 1
print("Crypto file 3:",letter_count)

for i in content4:
    if i == " ":
        word_count += 1
    letter_count += 1
print("Crypto file 4:",letter_count,"letters and",word_count,"words." )

for i in content5:
    letter_count += 1
print("Crypto file 5:",letter_count)




# ABCs = "abcdefghijklmnopqrstuvwxyz"
# newABCs = ''


# first = ABCs[0] 
# end1 = ABCs[len(ABCs)-1]
# end = len(ABCs) - 1
# end2 = ABCs[-1]
# print(end,end1,end2, first)
# print(ABCs)


# print(newABCs)

# for shift in ABCs:
#     if shift == first:
#         newABCs = ABCs.replace(first, end2)
#     if shift == end2:
#         newABCs = ABCs.replace(end2,first)
# print(newABCs)

# shifter = 0
# position = ABCs[shifter]
# next_position = ABCs[shifter + 1]
# first_letter = ABCs[0]

# while shifter <= 26:
#     newABCs = ABCs.replace(position,next_position)
#     shifter += 1
    

# first_newABCs = newABCs[0]
# newABCs = newABCs + first_letter
# newABCs = newABCs[:1] + newABCs[2:]
# # newABCs = newABCs.capitalize()
# # newABCs = newABCs.replace(first_newABCs,"")
# # newABCs = newABCs.lower()
# print(newABCs)

def caesar_cipher(ABCs):
    shifter = 0
    position = ABCs[shifter]
    next_position = ABCs[shifter + 1]
    first_letter = ABCs[0]

    while shifter <= 26:
        newABCs = ABCs.replace(position,next_position)
        shifter += 1
    
    first_newABCs = newABCs[0]
    newABCs = newABCs + first_letter
    newABCs = newABCs[:1] + newABCs[2:]
    
    return newABCs

ABCs = str(input("Enter the message that your like to encrypt: ").strip())
raw_input = int(input("How many times would you like to shift the message? "))
counter = 0
while counter < raw_input:
   ABCs = caesar_cipher(ABCs) 
   counter += 1
   print(ABCs)
   
   
   
crypto1.close()
crypto2.close()
crypto3.close()
crypto4.close()
crypto5.close()