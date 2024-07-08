# 3.2.14   LAB   Essentials of the while loop

blocks = int(input("Enter the number of blocks: "))

block_used = 0  # Initiate variable to store used blocks
height = 0   # Initiate variable to store height

# There must be aleast 1 block to start a pyramid.
if blocks > 0:
    top_layer = 1  # If there is atleast 1 block, start from the top_layer

while block_used < blocks:  # Until used blocks are less than total blocks
  block_used += top_layer   # Add 1 on each iteration
  print("block used: ",block_used)  #test
  print("top_layer: ",top_layer)   #test
  print("height: ",height)   #test
  if block_used > blocks:    # if used blocks are more than the total blocks, break out of the loop
    break
  else:   
    height+=1    # Add 1 on height on each iteration
    top_layer +=1   # Add 1 on each layer on each iteration
  
  


print("The height of the pyramid:", height)
