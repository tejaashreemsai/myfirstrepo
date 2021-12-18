import random
print("Your in a Dark room in a Mysterious castle.")
print("In front of you are three doors. You must choose one.")
playerChoice = random.randint(0,5)
print("Your lucky choice",playerChoice)
if playerChoice == 1:
     print("You find a room full of treasure. You're rich!")
     print("GAME OVER, YOU WIN!")
elif playerChoice == 3:
    print("The door opens and an angry orge hits you with his club.")
    print("GAME OVER, YOU LOSE!")
elif playerChoice == 2:
    print("you go into the room and find a sleeping dragon.")
    print("The dragon wakes up and eats you. You are delicious.")
    print("GAME OVER, YOU LOSE!")
else:
    print("Sorry, you didn't enter 1,2 or 3!")
print("Run the game again to have another go.")
