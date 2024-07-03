# Lab 3.2.7 
#scenario
#do you know what mississippi is? well, it's the name of one of the states and rivers in the united states. the mississippi river is about 2,340 miles long, which makes it the second longest river in the united states (the longest being the missouri river). it's so long that a single drop of water needs 90 days to travel its entire length!

#the word mississippi is also used for a slightly different purpose: to count mississippily.

#if you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.

#the idea behind it is that adding the word mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one mississippi, two mississippi, three mississippi" will take approximately an actual three seconds of time! it's often used by children playing hide-and-seek to make sure the seeker does an honest count.

#your task is very simple here: write a program that uses a for loop to "count mississippily" to five. having counted to five, the program should print to the screen the final message "ready or not, here i come!"

#use the skeleton we've provided in the editor.

#  extra info  
#note that the code in the editor contains two elements which may not be fully clear to you at this moment: the import time statement, and the sleep() method. we're going to talk about them soon.

#for the time being, we'd just like you to know that we've imported the time module and used the sleep() method to suspend the execution of each subsequent print() function inside the for loop for one second, so that the message outputted to the console resembles an actual counting. don't worry - you'll soon learn more about modules and methods.

#expected output:

#1 mississippi
#2 mississippi
#3 mississippi
#4 mississippi
#5 mississippi
#ready or not, here i come!

import time

# Write a for loop that counts to five.
for i in range(1,6): 
    print("#",i," mississippi")# Body of the loop - print the loop iteration number and the word "Mississippi".
    time.sleep(1)# Body of the loop - use: time.sleep(1)

# Write a print function with the final message.
print("ready or not, her i come!")

