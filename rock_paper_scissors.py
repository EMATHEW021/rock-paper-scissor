import random

scissors = """
    _____
---'   ___)____
       ________)
       ________)
       (___)
_____(___)
"""

paper = """
    __________
---'   _______)
       ________)
       ________)
       ________)
___________)
"""

rock =  """
    ______
---'   (___)
      ( ____)
       (_____)
       (____)
______(___)
"""
images= [rock,paper,scissors]
user = int(input("What do you choose ? 0 for Rock, 1 for Paper or 2 for scissors:\n"))
if user >=3 or user < 0 :
    print("Invalid, you lose")
   
else:
    print(images[user])
    
    computer = random.randint(0,2)
    
    print("computer chose:")
    print(images[computer])
    
    if user == 0 and computer == 2:
        print("You win")
    elif user == 0 and computer == 1 :
        print("you lose")
    elif computer == user :
        print("its a draw")
    elif user == 1 and computer == 0:
        print("you win")
    elif user == 1 and computer == 2:
        print("You lose")
    elif user == 2 and computer == 0:
        print("you lose")
    elif user == 2 and computer == 1:
        print("You win")
    else:
        print("its not among the choice, you lose!!!")