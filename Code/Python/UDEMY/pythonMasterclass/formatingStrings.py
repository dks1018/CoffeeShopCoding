print("I am going to show oyu how to use a format specifier")

bigNumber = 1234567.1234567
#input("Input a huge number with a decimal in it: ")

print(bigNumber)
print("Print the integer number %d" % (bigNumber))
print("Print the float number %f" % (bigNumber))
print("Print the first digits and only 3 after the decimal point %.3f" % (bigNumber))
print("Print the first digits and only 10 after the decimal point %.10f" % (bigNumber))
print("Print the first digits and only 3 after the decimal point %3.f" % (bigNumber))
print("% 10.3E"% (bigNumber))