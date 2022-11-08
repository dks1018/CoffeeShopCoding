def split_join(s1):
    s1 = s1.split()
    s = "-".join(s1)
    return s

def main():
    user1 = str(input("Type your name with a space: "))
    
    join = split_join(user1)
    print(join)
    
if __name__ == '__main__':
    main()