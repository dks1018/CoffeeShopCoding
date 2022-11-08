num = int(input())
b_num = bin(num)
counter = 0
answer = 0
answer2 = 0
for i in b_num:
    if(i == '1'):
        counter += 1
        answer += 1
    if(i == '0'):
        if(answer >= counter):
            counter = 0
        else:
            answer = counter
        
print(counter)
print(answer)
print(b_num)