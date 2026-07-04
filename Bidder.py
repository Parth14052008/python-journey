import os
import time
import random
biding = {}

auction_items = {
    "Antique Pocket Watch": r"""
      .-------.
    .' 12  1 '.
   /11      2 \
  |10   o    3|
  |9         4|
   \8       5/
    '. 7 6 .'
      '-----'
""",

    "Vintage Typewriter": r"""
    ______________________
   | [] [] [] [] [] [] [] |
   | [] [] [] [] [] [] [] |
   |_______________________|
      |               |
      |_______________|
""",

    "Diamond Ring": r"""
       /\
      /  \
     / /\ \
     \ \/ /
      \  /
       \/
    ---()---
""",

    "Luxury Wristwatch": r"""
     .--------.
    / 12    1 \
   |9   o    3|
    \ 6____5 /
     '------'
        ||
        ||
""",

    "Gaming Laptop": r"""
     __________________
    |                  |
    |   GAMING RGB     |
    |__________________|
     \________________/
""",

    "Smartphone": r"""
     ___________
    |           |
    |           |
    |           |
    |     ○     |
    |___________|
""",

    "Electric Guitar": r"""
       O
       |
      /|\
     / | \
       |
      / \
     /___\
""",

    "Mountain Bike": r"""
      __o
    _ \<_
   (_)/(_)
""",

    "Painting by a Local Artist": r"""
    .-----------.
    | /\    /\  |
    |/  \__/  \ |
    |\        / |
    '-----------'
""",

    "Gold Coin": r"""
      .------.
    .'  GOLD '.
   |    ₹     |
    '._______.'
""",

    "Rare Comic Book": r"""
     ____________
    | COMIC BOOK |
    |  POW! BAM! |
    |____________|
""",

    "Designer Handbag": r"""
      _________
     /         \
    |           |
    |           |
     \_________/
""",

    "Professional Camera": r"""
      .--------.
     | []  [] |
     |   ()   |
     |________|
""",

    "Drone": r"""
      o-----o
        \_/
      o-----o
""",

    "PlayStation 5": r"""
      ||||||||
      || PS ||
      || 5  ||
      ||||||||
""",

    "MacBook Pro": r"""
     _______________
    |               |
    |   MacBook     |
    |      Pro      |
    |_______________|
      \___________/
""",

    "Leather Sofa": r"""
    __________________
   |                  |
   |__________________|
   |__________________|
""",

    "Royal Chess Set": r"""
        ♔
       /_\
      |___|
       | |
      _| |_
""",

    "Treasure Chest": r"""
      __________
     /_________/|
    |  $$$$$$ | |
    |_________|/
""",

    "Private Island Vacation Package": r"""
        🌴
       /|\
      /_|_\
   ~~~~~~~~~~~
"""
}



auction_items.update({

    "Crown": r"""
       _/^\_
      /     \
     | () () |
      \_===_/
""",

    "Castle": r"""
       |>>>|
     __|___|__
    |  _   _  |
    | | | | | |
    |_|_|_|_|_|
""",

    "Pirate Ship": r"""
        |\
       /| \
      /_|__\
    __|_____|__
    \_________/
""",

    "Robot": r"""
      .----.
     | [] []|
     |  --  |
     |______|
      /|  |\
     /_|__|_\
""",

    "Spaceship": r"""
        /\
       /  \
      |====|
      |====|
       \__/
        ||
""",

    "Rocket": r"""
        /\
       /  \
      |NASA|
      |    |
      |____|
       /||\
""",

    "Helicopter": r"""
    ----====----
        |  |
      __|__|__
     /  ___   \
""",

    "Sports Car": r"""
      ______
 ____/|_||_\`.__
( _          _  )
='-(_)--(_)--(_)-'
""",

    "Motorcycle": r"""
      __o
    _ \<_
   (_)/(_)
""",

    "Jet Fighter": r"""
       __|__
--o--o--(_)--o--o--
""",

    "Ancient Sword": r"""
        /\
        ||
        ||
        ||
       /__\
""",

    "Magic Wand": r"""
      *
      |
      |
      |
     / \
""",

    "Treasure Map": r"""
    .------------.
    | X      ~~~ |
    |   ~~~      |
    '------------'
""",

    "Crystal Ball": r"""
      .------.
     /        \
    |   ()     |
     \________/
""",

    "Knight Helmet": r"""
      .----.
     / .--.\
    | | [] ||
     \ '--'/
""",

    "Ancient Scroll": r"""
     .--------.
    /~~~~~~~~~~\
    \~~~~~~~~~~/
     '--------'
""",

    "Globe": r"""
      .----.
    .'      '.
   |  🌍 🌎  |
    '.______.'
""",

    "Golden Trophy": r"""
      .-===-.
     (  WIN )
      \_____/
        | |
      __| |__
""",

    "Treasure Key": r"""
      __
    _/o \____
   \_______/
       ||
""",

    "Magic Lamp": r"""
       __
     _(  )__
    /      _)
    \______/
"""
})

print("This is aution service where you can put bid ")
time.sleep(1)
print("Item will be visible on screen soon .....")
time.sleep(2)

item_name, item_art = random.choice(list(auction_items.items()))

name_of_item = f"\n🏆 Today's Auction Item: {item_name}\n"
picture = item_art

print(name_of_item)
print(picture)


import subprocess
def clean():
    subprocess.run("cls"if os.name == "nt" else "clear",shell=True)


def ques(name_of_person , bid_amount):
    
    if name_of_person in biding:
        print(f"This Name [{name_of_person}] already exist, You need different Name to add")
    
    while True:
        try:
            bid_amount = int(bid_amount)
            break
        except ValueError:
            try:
                bid_amount = float(bid_amount)
                break
            except ValueError:
                bid_amount = input("Invalid amount. Please enter a number: ")
                continue
    biding[name_of_person] = bid_amount
    print("Adding....")
    time.sleep(2)
    print(f"Added {name_of_person} with bid amount {bid_amount} successfully.")




def winner():
    highest_bid = max(biding.values())

    winners = []
    for name, bid in biding.items():
        if bid == highest_bid:
            winners.append(name)

    if len(winners) == 1:
        print(f"The winner is {winners[0]} with ₹{highest_bid}")
    else:
        print("It's a tie!")
        print(f"The tied bidders are: {', '.join(winners)}")
        print(f"Highest bid: ₹{highest_bid}")
   



while True:
    name = input(" TELL YOUR NAME : " ).strip().capitalize()
    bid = input("ENTER YOUR BID AMOUNT: ")
    ques(name_of_person=name,bid_amount=bid)
    control = True
    while True:
        yes_no = input("ANY OTHER PERSON AVAILABLE [ YES OR NO ]: ").strip().lower()
        if yes_no == "yes":
            print("Now get ready to give device to next person")
            print("Screen is clearing....")
            time.sleep(3)
            clean()
            print("Screen cleared succesfully , give device to other person ")
            print(name_of_item)
            print(picture)
            break
        elif yes_no== "no":
            clean()
            time.sleep(1)
            print("Now Lets see Who won")
            print("Checking Data....")
            time.sleep(2)
            winner()
            control = False
            break
        else:
            print("Wrong input Enter Yes or no ")
            continue
    if not control:
        break


    
        

    





