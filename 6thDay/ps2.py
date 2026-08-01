math = int(input("Enter your Math marks  "))
phy = int(input("Enter your Physics marks "))
chem = int(input("Enter your Chemistry marks "))

if(math > 33 and phy > 33 and chem > 33):
    percent = (100*(phy+chem+math))/300
    if(percent >= 40):
        print("PASS...")
else:
    print("Fail")