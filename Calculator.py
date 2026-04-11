
num_1 = int(input("Enter First number: "))
sign = input("Enter symbol[+,-,*,/] that you want to perform: ")
num_2 = int(input("Enter second number: "))

if(sign == "+"):
    print(num_1 + num_2)
elif(sign == "-"):
    print(num_1 - num_2)
elif(sign == "*"):
    print(num_1 * num_2)
elif(sign == "/"):
    if(num_2 == 0):
        print("Cannot divide by zero")
    else:
        print(num_1 / num_2)
else:
    print("Invalid operator")

    
