#example python assessment

#q1) - create a variable called numOne and assign it with a float of 2
numOne = float(2)

#2) Create another varaible called numTwo and assign it with a float of 5
numTwo = float(5)

#3) create a third variable called numSum which captures the sum of numOne and numTwo
numSum = numOne + numTwo

#4) take an input from the user called numUser
numUser = float(input("Enter a number: "))

#5)a create a variable called highNumber with the value assigned to 10
highNumber = 10

#5b perform a decision within the code which will output "High Number" 
#if the product of numUser and numSum is greater than highNumber
#and "Low Number" if smaller than 10 
p = numUser * numSum
if p > highNumber:
  print("High number")
elif p < highNumber:
  print("Low number")

#6) using a for loop create a list called firstList with the numbers 1-20 stored in it
firstList = []
for num in range(1,21):
  firstList.append(num)

#7) create a second list called secondList which stores the value of the corresponding 
#index in the first list multiplied by 2. e.g. [2,4,6,8....]
secondList = []
for num in firstList:
  secondList.append(num * 2)

#8) create a third list called boolList which stores whether each element in secondList
#is higher than highNumber (True) or lower (False)
boolList = []
for num in secondList:
  if num > highNumber:
    boolList.append(True)
  elif num < highNumber:
    boolList.append(False)
        
print(boolList)
#Question 9 will be once we have completed Mod 41 and Mod 42 review Tuesday


#9a) create a func called numPrint that outputs a list of numbers between a starting 
#number and a finish number. The function should have two parameters startNumber and endNumber
#def numPrint(startNumber, endNumber):
 #   return list(range(startNumber +1, endNumber))

#print(numPrint(12, 25))

def numPrint(startNumber, endNumber):
  return list(range(startNumber,endNumber+1))


#9b) once you have done 9a, make a change so that if the user doesnt input an end number 
#it automatically uses 10
def numPrint(startNumber, endNumber=10):
  return list(range(startNumber,endNumber+1))


#10)create a function which takes in a list of numbers as an argument. It then returns the number
#of odd numbers within the list. For example [3,4,5] should return 2

def numList(list):
  counter = 0
  for num in list:
    if num%2 != 0:
      counter += 1
  return counter
    

#11) create a tuple which stores the following values 3,4,6,5,3,5,7,8,5
tup1 = (3,4,6,5,3,5,7,8,5)

#12) The values shown in question 10 refer to the number of goals scored by the following players 
#Rooney, Vardy, Heskey, Owen, Grielish, Sterling, Pele, Maradona, Walker
#Create a second tuple which stores these players
tup2 = ("Rooney", "Vardy", "Heskey", "Owen", "Grielish", "Sterling", "Pele", "Maradona", "Walker")

#13)) using the above tuples, link them via a dictionary.
#for example, Rooney:3, Vardy:4 etc. You should use your two tuples to construct the 
#dictionary

    #dictionary key is equal to value of tuple players and 
    #dictionary value is equal to value of tuple 1
    
    #dictionary[tuple1[i]] = tuple_players[i]
dict = {}
for i in range(len(tup2)):
  #dict.update({tup2[i] : tup1[i],})
  dict[tup2[i]] = tup1[i]

print(dict)
  

