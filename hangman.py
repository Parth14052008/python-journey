import random
import time
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("Hello , Welcome to Game Hangman")
word_list = ["aardvark", "baboon", "camel","apple", "banana", "camera","dragon", "garden", "market", "pocket", "awkward", "bagpipes", "crypt", "dwarf", "fishhook","vortex", "wizard", "zombie", "whiskey", "safari","pixel","unknown","unworthy", "twelfths", "unzip", "vaporize",]
time.sleep(1)
print("Let me choose Word and You have To guess it")
time.sleep(2)
chosen_word = random.choice(word_list)


placeholder = " "
word_length = len(chosen_word)
for postion in range(word_length):
    placeholder +="_"

print(placeholder)
lives = 7
photo = -1
correct_letters = []

while lives > 0:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess not in chosen_word:
        print(stages[photo])
        lives -= 1
        photo-=1
        print("Lives left:", lives)
        continue
        
    elif guess == chosen_word:
        print("You guessed it!")
        break
    else :
        correct_letters.append(guess)
        for letter in chosen_word:
            if letter in correct_letters:
                display += letter

            else:
                display += "_"
        print(display)
        
        continue


if lives == 0 :
    print(f"You Lost it correct word is : {chosen_word}")
            
print("Thank You For Playing Hangman")






    