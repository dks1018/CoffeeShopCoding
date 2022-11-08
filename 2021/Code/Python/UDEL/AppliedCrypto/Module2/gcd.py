
counter = 0

def gcd(a,b):
    global counter
    print(a,b,counter)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    gcd(8,13)

if __name__ == "__main__":
    main()