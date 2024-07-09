# 4.3.8   LAB   Converting fuel consumption
# A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

# In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.

# Your task is to write a pair of functions converting l/100km into mpg, and vice versa.

# The functions:

# are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;
# take one argument (the value corresponding to their names)
# Complete the code in the editor and run it to check whether your output is the same as ours.

# Here is some information to help you:




def liters_100km_to_miles_gallon(liters):
    meters = 100000     # 100 km = 100000 meters
    american_mile = meters / 1609.344  # 1 American mile = 1609.344 metres;
    american_gallon = liters / 3.785411784   # Calculate american gallon form liters

    miles_gallon = american_mile / american_gallon  # Calculate miles per gallon
    return miles_gallon    # Return miles per gallon value



def miles_gallon_to_liters_100km(miles):
    american_gallon = 1
    liters = american_gallon * 3.785411784  # 1 American gallon = 3.785411784 litres.
    meters = miles * 1609.344  # 1 American mile = 1609.344 metres;
    km_100 = meters /100000    # Calculate 100 km from meters

    liters_100km = liters / km_100  # Calculate liters per 100km 
    return liters_100km    # Return the liters per 100km value

#Expected output:

#60.31143162393162
#31.36194444444444
#23.52145833333333
#3.9007393587617467
#7.490910297239916
#10.009131205673757

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.1))
print(miles_gallon_to_liters_100km(23.5))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(60.3))

