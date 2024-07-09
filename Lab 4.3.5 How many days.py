# 4.3.5   LAB   How many days: writing and using your own functions
# Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given year-month pair (while only February is sensitive to the year value, your function should be universal).

# The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

# Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). It may be very helpful. We encourage you to use a list filled with the months' lengths. You can create it inside the function ‒ this trick will significantly shorten the code.

# We've prepared a testing code. Expand it to include more test cases.

# ****** Function: is_year_leap *************************
def is_year_leap(year):
#   Leap Year Logic:

# 1. If a year is divisible by 4, it's a potential leap year.
# 2. However, if the year is divisible by 100, it's not a leap year unless the year is divisible by 400.
  if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
      return True  # Returns True is it's a leap year
  else:
      return False  # Returns False is it's not a leap year

# ****** Function: days_in_month ************************
def days_in_month(year, month):
    months_length = [31,28,31,30,31,30,31,31,30,31,30,31]   # list of months length in common year
    months_length_leap = [31,29,31,30,31,30,31,31,30,31,30,31]  # List of months lenght in leap year
    months = [1,2,3,4,5,6,7,8,9,10,11,12]  # List of months in numeric form
    
    for i in range(12):   # Iterate over numbers from 0 to 11
        if month == months[i]:  # Check if the number is in the range of 12
            if is_year_leap(year) == True:   # Check if the given year is a leap year
                return months_length_leap[i]  # Return months length if the year is a leap year
            else:
                return months_length[i]   # Return months length if the year is not a leap year
     
# ****** Given test code *******************************  
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
