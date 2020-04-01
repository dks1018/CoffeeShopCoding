n = int(input("How many scores?: "))
scores = []

for i in range(n):
    scores.append(input())

noDup = list(set(scores))
noDup.sort()

runnerUp = len(noDup) - 2
print("The Runner up is: ", noDup[runnerUp])
print(scores)
print(noDup)

# i = int(input())
# lis = list(map(int,raw_input().strip().split()))[:i]
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))

# print(max(lis))

# n = int(input())
# arr = list(map(int, input().split()))
# zes = max(arr)
# i=0
# while(i<n):
#     if zes ==max(arr):
#         arr.remove(max(arr))
#     i+=1
# print(max(arr))
