even = ""
odd = ""
t = int(input())
i = 0
for n in range(t):
    s = str(input())
    if s[i] % 2:
        even += s[i]
    else:
        odd += s[i]
i += 1
print(even,odd)

