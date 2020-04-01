if __name__ == '__main__':
    n = int(input())
    t = 1
    varNum = ''
    
    while n > 0:
        varNum += str(n - n + t) + ' '
        t += 1
        n -= 1
    print(varNum)
    

n = int(input("Enter Num: "))
varNum1 = ''

for i in range(n+1):
    varNum1 += str(i) + ' '
print(varNum1)