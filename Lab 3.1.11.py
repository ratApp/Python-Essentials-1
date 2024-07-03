# 3.1.11   LAB   Essentials of the if-else statement
# Income tax calculator

income = float(input("Enter an income: "))

if income <= 85528 :  # If income is smaller than or equal to 85528
  tax = 18/100 * income - 556.02   # Calculates tax
  if tax >= 0:    # Check if the tax is less than 0
    print("The tax is: ", round(tax,0), " thalers")   # Prints tax in thalers
  else:
    print("The tax is 0.0 thalers")  # If the tax is less than 0, print the value of tax 0
else:  # If income is more than 85528
  tax = 14839.02 + (income - 85528)*32/100   # Calculates tax
  print("The tax is: ", round(tax,0), " thalers")  # Prints tax in thalers

