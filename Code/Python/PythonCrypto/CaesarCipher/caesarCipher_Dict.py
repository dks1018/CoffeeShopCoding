#in a dicitonary
message = "Do your best with this message"
message.upper()

ABC = {
    1:"A",2:"B",3:"C",4:"D",5:"E",
    6:"F",7:"G",8:"H",9:"I",10:"J",
    11:"K",12:"L",13:"M",14:"N",15:"O",
    16:"P",17:"Q",18:"R",19:"S",20:"T",
    21:"U",22:"V",23:"W",24:"X",25:"Y",
    26:"Z"
}
letter = ''
shift = int(input("How many characters would you like to shift: "))
for i in message:
    for k,v in ABC.items():
        k = k + shift
        print(k,v,sep=":")
    
# ABC = [
#     "A","B","C","D","E","F",
#     "G","H","I","J","K","L",
#     "M","N","O","P","Q","R",
#     "S","T","U","V","W","X",
#     "Y","Z"
# ]
# shift = int(input("How many characters would you like to shift: "))

# i = 0
# while i <= shift:
#     del ABC[i]
#     i += 1

# # just add shift to everynumebr until 13
# # after 13 
