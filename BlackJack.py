import random
import time


logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

def cardchooser():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_pickup = random.choice(list(cards))
    return card_pickup

  

def rules_for_com(compScore,playscore):
    if compScore == playscore:
        return "Draw"
    elif compScore == 21:
        return "You lose , Dealer has Blackjack"
    elif playscore == 21:
        return "You win , You has Blackjack"
    elif playscore > 21:
        return "You Lose Game "
    elif compScore> 21:
        return "You win Game"
    elif compScore > playscore and compScore < 21:
        return "You Lose"
    elif playscore > compScore and playscore < 21:
        return "You win "
    


def score_count(cardvalue_comp , cardvalue_play):
    total_of_comp = 0
    total_of_play = 0
    for score_of_comp in cardvalue_comp:
        total_of_comp +=score_of_comp
    for score_of_play in cardvalue_play:
        total_of_play+=score_of_play
    return total_of_comp , total_of_play 
    
    






def Game():
    comp_card = []
    play_card = []
    comp_card.append(cardchooser())
    comp_card.append(cardchooser())
    play_card.append(cardchooser())
    play_card.append(cardchooser())
    while True:
        compscores, playscores = score_count(cardvalue_comp=comp_card, cardvalue_play=play_card)
        time.sleep(1)
        print(f"You have :{play_card} Your Current score : {playscores}\n Computer First Card : {comp_card[0]}")

        if playscores > 21 and 11 in play_card:
            play_card[play_card.index(11)] = 1
            compscores, playscores = score_count(cardvalue_comp=comp_card, cardvalue_play=play_card)

        if playscores >= 21:
            decide = rules_for_com(compScore=compscores, playscore=playscores)
            print(decide)
            print(f"Dealer card : {comp_card}, Dealer score : {compscores}")
            print(f"Your card : {play_card}, Dealer score : {playscores}")
            break
        card_pickup = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()

        if card_pickup == "y":
            play_card.append(cardchooser())
            print("Giving you cards...")
            time.sleep(2.5)
            continue

        elif card_pickup == "n":
            while compscores < 16:
                print("Now Dealer Playing....")
                time.sleep(2)
                comp_card.append(cardchooser())
                compscores, playscores = score_count(cardvalue_comp=comp_card, cardvalue_play=play_card)
                continue
            time.sleep(2)
            decide = rules_for_com(compScore=compscores, playscore=playscores)
            print(decide)
            print(f"Dealer card : {comp_card}, Dealer score : {compscores}")
            print(f"Your card : {play_card}, Dealer score : {playscores}")
            break

        else:
            print("wrong input")
            continue

            
            
while True:
    time.sleep(2)
    ques = input("Do You want to Play  ?\n[yes or no]\n").strip().lower()
    if ques == "yes":
        print("Giving you cards...")
        time.sleep(2)
        Game()
        time.sleep(2)
        continue
    elif ques == "no":
        print("Thanks for Playing Game")
        break
    else:
        print("Wrong Input ")
        continue
        



        






# print(Com)
# while True:




    


    