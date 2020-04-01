n = int(input().strip())

numbers = str(bin(n)[2:]).split('0')
lenghts = [len(num) for num in numbers]
print(max(lenghts))

numbers = str("{0:b}".format(n)).split('0')

n = int(input().strip())
print(max(len(length) for length in bin(n)[2:].split('0')))

#Since bin(5) will produce '0b101', with [2:] we get rid of the initial '0b'

n = int(input().strip())
print(max(map(len, bin(n)[2:].split("0")))
      
# First, they convert the number to binary.
# As bin() returns binary numbers but with '0b' as prefix.
# That's why we only used [2:0]. 
# Now we spilt our number from wherever 0 occurs. 
# e.g. : 1101101110 : [11,11,111] We 'll have a list of this kind, 
# At last we return who has maximum length.