Name = input("Tell us your Name :")
Year_of_Born = input("May i know your birth year:")

print("Hey Whats up",Name)
print("Today I am Going Tell your product that these company acutally earn")

Product_Name = input("Firstly Tell Your Product Name")
Product_Company = input("Tell Brand or company name that manufacture")

print("The",Product_Name,"of",Product_Company,"You used is great" )

Price = int(input("Now tell price of product"))
GstRate = int(input("Tell GST Rate (%) that levied on your Product"))

Gst_Amount = Price*GstRate/100
Revenue = Price - Gst_Amount


print("Revenue Earned by",Product_Company,"through per unit sold of is:",Revenue )









   


   