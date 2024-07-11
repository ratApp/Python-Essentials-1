tupl = tuple('Python World!')
print(tupl[:-7])

def fun(a=3,b=2):
  return a ** b

print(fun(2))

for i in range(2):
  print(i)

def fun(*val):
  print(val)

lst=[1,2,3,4,5]
number = 400
fun(lst,number)


lst = [1,2]*5
print(lst)

row = ['WHITE_PAWN' for i in range(8)]

print(row)

dict1 = {"John":1234, "Fruit":"Apples"}
dict2 = { "Fruit":"Apples","John":1234}

print(dict1 == dict2)

str = "Hello Python!"
print(len(str))
str = str[-7:len(str)]
print(str)
print(len(str))

val =16
print("hi") if val < 15 else print("bye")

for i in range(1,4):
  print(i)
  break
else:
  print("hi")
