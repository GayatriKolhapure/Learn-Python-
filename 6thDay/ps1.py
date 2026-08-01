a = int(input("Enter your number  "))
b = int(input("Enter your number  "))
c = int(input("Enter your number  "))
d = int(input("Enter your number  "))

if(a > b and a > c and a > d):
    print("A is greatest Number...", a)
elif(b > c and b > a and b > d):
    print("B is greatest Number...", b)
elif(c > a and c > b and c > d):
    print("C is greatest Number...", c)
else:
    print("D is greatest Number...", d)

