# lab 2.6.9

# input a float value for variable a here
a = float(input("Enter a value of a:"))

# input a float value for variable b here
b = float(input("Enter a value of b:"))


# Using the While loop to protect the code from being divided by zero

while b == 0 :
  print("Please enter a value of b other than 0, Try again !!")
  b = float(input("Enter a value of b:"))
  #continue
else:
  # output the result of addition here
  print("\nResult:\nAddition of a and b: ", a + b)

  # output the result of subtraction here
  print("Subtraction of a and b: ",a - b)

  # output the result of multiplication here
  print("Multiplication of a and b: ",a * b)

  # output the result of division here
  print("Division of a and b: ",a / b)

print("\nThat's all, folks!")

