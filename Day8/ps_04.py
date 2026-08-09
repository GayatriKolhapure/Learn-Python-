def sumNNumbers(n):
    if(n == 1):
        return 1
    return n + sumNNumbers(n-1)

print(sumNNumbers(5))