''''
1 for snake
-1 for water
0 for gun

'''

import random

# Game setup
comp = random.choice([-1, 0, 1])
yourChc = input("Enter your choice (S for Snake, W for Water, G for Gun): ").upper()

youDict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Handle invalid inputs gracefully
if yourChc not in youDict:
    print("Invalid choice! Please enter S, W, or G.")
else:
    you = youDict[yourChc]

    print(f"\nYour Choice: {reverseDict[you]}")
    print(f"Computer Choice: {reverseDict[comp]}\n")

    # Game logic
    if comp == you:
        print("It's a Draw! 🤝")
    elif (comp == -1 and you == 1) or (comp == 1 and you == 0) or (comp == 0 and you == -1):
        print("You Win! 🎉")
    else:
        print("You Lose! 😞")
    




