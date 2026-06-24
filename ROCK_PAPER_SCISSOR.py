print("welecome to game ROCK PAPER SCISSOR")
import time





rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game = [rock , paper , scissors]


while True:
    time.sleep(1)
    x = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
    x =int(x)
    
    if 0 <= x <= 2:
        print(game[x])
        break
    else:
        print("wrong option")
        continue


import random
y = random.randint(0,2)

print("Computer Choose")
print(game[y])
    


# x = user output , y = computer choice


if x == 0 and y == 2:
    print("You win!")
elif y == 0 and x == 2:
    print("You lose!")
elif y > x:
    print("You lose!")
elif x > y:
    print("You win!")
elif x == y:
    print("It's a draw!")






             