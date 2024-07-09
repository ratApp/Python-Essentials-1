# 4.3.4   LAB   A leap year: writing your own functions
# Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.

# The seed of the function is already shown in the skeleton code in the editor.

# Note: we've also prepared a short testing code, which you can use to test your function.

# The code uses two lists ‒ one with the test data, and the other containing the expected results. The code will tell you if any of your results are invalid.


def is_year_leap(year):
#   Leap Year Logic:

# 1. If a year is divisible by 4, it's a potential leap year.
# 2. However, if the year is divisible by 100, it's not a leap year unless the year is divisible by 400.
  if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
      return True  # Returns True if it's a leap year
  else:
      return False  # Returns False if it's not a leap year
    
# Test data
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

