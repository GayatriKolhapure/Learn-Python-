# c/5 = (f-32)/9
# c = 5 *((f-32)/9)


f = int(input("Enter temperature in F: "))

def f_to_c(f):
    c = 5 * ((f - 32)/9)
    return c




print(f"{round(f_to_c(f), 2)} deg C")