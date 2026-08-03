n = int(input("Enter a number: "))

for i in range(2, n-1):
    if(n % i) == 0:
        print(n, "is Not Prime...")
        break;
else:
    print(n, "is a Prime number...")

