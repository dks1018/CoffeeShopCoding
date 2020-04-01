message = "Lets go ahead and reverse this message bruh"
revMessage = ''
i = len(message) - 1

while i >= 0:
    revMessage = revMessage + message[i]
    i = i - 1  
print(message,revMessage, sep="\n")