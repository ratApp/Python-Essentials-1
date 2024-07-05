# 3.2.15   LAB   Collatz's hypothesis
#brief overveiw of collatz hypotheseis itself, what does it do etc.....

c0 = int(input("Enter a number: "))  # Prompt user input and assign it to a variable
count = 0    # Initialise count variable to 0
while c0 != 1:   # Until C0 is not equal to 1
  if c0%2 == 0:   # Check it c0 is even
    c0 = c0/2
  else:       # If c0 is odd
    c0 = 3* c0 + 1
  count += 1     # Increase the count by 1
  print("c0: ",c0)    
print("Steps: ",count)
  
  
