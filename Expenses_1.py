print("Hello Today I am going to measure your all expenses")
name = input("Enter Your name : ")
symbol = input("Enter your Currency Symbol : ")
budget = int(input("Enter your budget : "))
month = input("Tell which month currently going on")
print("Hello Dear",name, "so your budget is" , budget )



while True:
	ques1 = input("Enter Yes if you enter your budget correct or no if incorrect : ").strip().lower()
	if (ques1 == "yes" ) :
		print("Thank you for confirmation")
		break
	elif (ques1 == "no"):
		print("Thank you for an update")
		break
	else:
		print("Invalid Answere Enter Yes or No only")
		continue


print("Now tell expense Category with amount in format (Expense : Amount) ")
print("If you want to add Your expenses enter 'Add' below ")
print("If you written all expenes Enter 'End' below ")

dic = {}

while True:
	ques2 = input("Enter 'Add' or 'End': ").lower()
	if(ques2 == "add"):
		data = input("Enter your expense Category with amount in format (Category , Expense : Amount) eg food,burger: 200 -- ").strip().lower()
		if ":" not in data :
			print("Format eror!")
			continue
		category , amount = data.split(":")
		category = category.strip()
		amount = amount.strip()
		if not amount.isdigit():
			print("Amount should be a number!")
			continue
		dic.update({category: int(amount)})
		continue
	elif(ques2 == "end" ):
		print("Thank You for sharing your details")
		break
	else:
		print("Invalid Answere Enter Only 'Add' or 'End' ")
		continue


print(dic)

print("you spend in most in category",max(dic,key=dic.get), "with amount", max(dic.values()))




sum_1 = sum(dic.values())
print("Your total expenses is :", sum_1, "in month of is", month)

print("Your Budget is :", budget)

if (sum_1 < budget ):
	surplus = budget - sum_1
	print("Nice you are in spending less than your budget i.e surplus budget and surplus which is left is :", surplus)
elif (sum_1 == budget):
	print("Good you basically spending eqally ")
else:
	deficit = sum_1 - budget
	print("Warning! You basically overspending i.e. deficit budget and deficit which is over spending is :" ,deficit)

print("You can search your expenes by our search tool")
print("Do you want me to search answere yes or no")

while True:
	ques3 = input("Do you want me to search yes or no only : ").lower()
	if (ques3 == "yes"):
		ques3_1 = input("Enter Your expense category: ").strip().lower()
		print(dic.get(ques3_1))
		break
	elif (ques3 == "no"):
		print("Thank you for telling us ")
		break
	else:
		print("invalid answere try yes or no only")
		continue