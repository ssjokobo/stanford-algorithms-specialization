def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a another number: "))
    print(karatsuba(x, y))

def karatsuba(x, y):
    sx = str(x)
    sy = str(y)    

    if x < 10 or y < 10:
        return x * y

    maxlen = max(len(sx), len(sy))
    midlen = maxlen // 2
    
    a = int(sx[:-midlen])
    b = int(sx[-midlen:])
    c = int(sy[:-midlen])
    d = int(sy[-midlen:])

    s1 = karatsuba(a, c)
    s2 = karatsuba(b, d)
    s3 = karatsuba((a + b), (c + d))
    s4 = s3 - s2 - s1

    return (10**(midlen * 2))*s1 + (10**midlen)*s4 + s2


if __name__ == "__main__":
    main()