# Lab 2.4.9

# Expected output
# 7.38 miles is 11.88 kilometers
# 12.25 kilometers is 7.61 miles

kilometers = 12.25
miles = 7.38

# 1 mile is equal to approximately 1.61 kilometers

miles_to_kilometers = miles * 1.61     #  miles multiplied by 1.61 outputs distance in kilometers
kilometers_to_miles = kilometers / 1.61  # kilometer divived by 1.61 outputs distance in miles

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")    #round function rounds the output to 2 decimal
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles") 


