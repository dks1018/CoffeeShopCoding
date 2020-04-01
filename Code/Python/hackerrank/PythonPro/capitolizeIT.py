def solve(i):
    for x in i[:].split():
        i = i.replace(x, x.capitalize())
        i = "".join(i)
    return i
    
if __name__ == '__main__':
    s = input()

    result = solve(s)
    
    print(result)


# def solve(i):
#     for x in i[:].split(" "):
#         i = i.replace(x, x.capitalize())
#         i = "".join(i)
        
#         return i
    
# if __name__ == '__main__':
#     s = input()

#     result = solve(s)
    
#     print(result)
