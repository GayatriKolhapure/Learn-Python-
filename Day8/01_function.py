# a = 78
# b = 45
# c = 30

# avg = (a+b+c)/3
# print(avg)


#functions w/o arguments

#function defination
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    avrg = (a+b+c)/3
    print(avrg)


#function call
avg()


#functions with arguments
#functions default value
def goodDay(name, ending="Thanks"):
    print("Good Day...", name)
    print(ending)
    return "done"



goodDay("Harry", "Thank You")
c = goodDay("Rohan")
print(c)


