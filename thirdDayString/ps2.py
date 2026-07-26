letter = '''Dear <|Name|>, 
You are selected!
<|Date|>...!'''

name = input("Enter Your Name...")
date = input("Enter a Date..")

print("__________________________")
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
