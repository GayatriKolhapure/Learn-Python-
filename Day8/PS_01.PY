def greatestNum():
    a = int(input("Enter a number..."))
    b = int(input("Enter a number..."))
    c = int(input("Enter a number..."))
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    else:
        return c



print(greatestNum())