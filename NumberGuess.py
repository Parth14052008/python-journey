import random
import os
import subprocess
import time

logo = r"""
___________                        _________                      __  .__    .__                 
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
          \/     |__|        \/          \/             \/     \/          \/        \//_____/   

"""





def clean():
    subprocess.run("cls"if os.name == "nt" else "clear",shell=True)


def typenumber():
    while True:
        try:
            num = input("Enter Number that you want \n")
            num = int(num)
            return num
        except ValueError:
            print("Wrong input — enter integers only")  
            continue 

run_program = True



    

def numbers_range(num1 , num2):
    number = []
           
    for i in range(num1,num2):
            number.append(i)
    return number




def lifeline(current_life, difficulty):
    if difficulty == "easy":
        current_life -= 1
    else:
        current_life -= 2

    return current_life




def Guess():
    life = 10
    print("If you choose 'easy' wrong answere deduct 1 and if 'hard' then wrong answeere deduct 2 and you have total 10 lives ")
    time.sleep(2)
    ques2 = input("Enter Diffculty of game [Easy or Hard]\n").strip().lower()
    print("Try to guess the number.")
    print(f"You have {life} lives.")
    while life > 0:
        word = True
        while word :
            try:
                guess_number = int(input("Enter Number : "))
                word = False
            except ValueError:
                print("Enter Intergers only")
                continue
                
        if guess_number < computer_choosen:
            life = lifeline(current_life=life,difficulty=ques2)
            print("It's low")
        elif guess_number > computer_choosen:
            life = lifeline(current_life=life,difficulty=ques2)
            print("It's high")
        else:
            print("You guessed it!")
            return

        if life <= 0:
            print("You lost the game.")
            print(f"The correct number was {computer_choosen}")
            return

        print(f"Lives remaining: {life}")

word_2 = True
while word_2:
    print(logo)
    time.sleep(2)
    print("Welcome to Game \n In this game you have to choose range and computer choose random number you have to guess it ")
    print("Ready?")
    time.sleep(2)
    print("I hope you were already ready")
    while run_program:
            print("Enter first number of the range:")
            first_num = int(typenumber())

            print("Enter last number of the range:")
            last_num = int(typenumber()) + 1

            while True:
                ques = input("Do you want to modify your range? Type yes or no:\n").strip().lower()

                if ques == "yes":
                    break  
                elif ques == "no":
                    run_program = False
                    break  # Breaks the inner loop; outer loop then stops

                else:
                    print("Invalid input. Please enter only yes or no.")
                    continue

    range_of_user = numbers_range(num1=first_num,num2=last_num)
    print("Computer is Chosing Number....")
    time.sleep(3)
    computer_choosen = random.choice(list(range_of_user))
    Guess()

    while True:
        play_again = input("Do you want to play again Enter yes or no \n").strip().lower()
        if play_again == "yes":
            clean()
            break
        elif play_again == "no":
            print("Thanks for Playing")
            word_2 = False
            break
            
        else:
            print("Wrong input Enter yes or no")
            continue




