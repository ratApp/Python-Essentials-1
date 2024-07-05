# 3.2.14   LAB   Essentials of the while loop

blocks = int(input("Enter the number of blocks: "))

block_used = 0
height = 0

if blocks > 0:
  top_layer = 1

while block_used < blocks:
  block_used += top_layer
  #height=+1
  print("block used: ",block_used)
  print("top_layer: ",top_layer)
  print("height: ",height)
  if block_used > blocks:
    break
  else:
    height+=1
    top_layer +=1
  
  


print("The height of the pyramid:", height)

