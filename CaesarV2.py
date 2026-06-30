import time

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


print(logo)

time.sleep(1)


print("Welcome to caesar cipher")

time.sleep(1)
print("Ready??")
time.sleep(2)
print("I hope you are Ready")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def question():
    print("What do you want to do encrypt or decrypt?")
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
        if direction == "encode":
            break
        elif direction =="decode":
            break
        else:
            print("Error! You have to enter 'encode' or 'decode' ")
            continue

    text = input("Type your message:\n").strip().lower()

    while True:
        shift = input("Type the shift number:\n").strip().lower()
        if shift.isdigit():
            shift = int(shift)
            print("Correct! format")
            break
        else:
            print("Invalid entry. Input contains non-numeric characters.")
            continue

    time.sleep(1)
    if direction == "encode":
        print("Encoding.....")
    else :
        print("Decoding.....")

    time.sleep(2)
    
    def caesar(en_de_text,shiftNumber,encode_decode):
        output = ""
        if encode_decode == "decode":
                shiftNumber = -shiftNumber
        
        for letters in en_de_text:
            if letters not in alphabet:
                output+=letters
                continue



            shift_postion = alphabet.index(letters) + shiftNumber
            shift_postion %= len(alphabet)
            output+=alphabet[shift_postion]
        if encode_decode == "encode":
            print(f"Your encrupted text : {output} ")
        else:
             print(f"Your decrupted text : {output} ")

    caesar(en_de_text=text,shiftNumber=shift,encode_decode=direction)
    

 
question()

time.sleep(2)

while True:
    ques = input("Do You want to continue? [yes or no]\n").strip().lower()
    if ques == "yes":
        print("Lets Continue Again!")
        question()
        continue
    elif ques == "no":
        print("We see you again :)")
        break
    else:
        print("Wrong Output Enter Again!")
        continue


print("I Hope You love this Application")