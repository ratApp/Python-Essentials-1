tupl = tuple('Python World!')
print(tupl[:1])
print(tupl[::-3])

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

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

my_list = [x * x for x in range(5)]

print(my_list)

lst = [i for i in range(-1, -2)]
print(lst)

dd = {"1": "0", "0": "1"}
for x in dd.values():
    print(x, end="")

lst1 = [[x for x in range(3)] for y in range(3)]
print(lst1)

for r in range(3):
    for c in range(3):
        if lst1[r][c] % 2 != 0:
            print("#")