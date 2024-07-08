# 4.3.6   LAB   Day of the year: writing and using your own functions
# Your task is to write and test a function which takes three arguments (a year, a month, and a day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

# Use the previously written and tested functions. Add your own test cases to the code.


def is_year_leap(year):
#   Leap Year Logic:

# 1. If a year is divisible by 4, it's a potential leap year.
# 2. However, if the year is divisible by 100, it's not a leap year unless the year is divisible by 400.
  if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
      return True  # Returns True is it's a leap year
  else:
      return False  # Returns False is it's not a leap year

def days_in_month(year, month):
    months_length = [31,28,31,30,31,30,31,31,30,31,30,31]   # list of months length in common year
    months_length_leap = [31,29,31,30,31,30,31,31,30,31,30,31]  # List of months lenght in leap year
    months = [1,2,3,4,5,6,7,8,9,10,11,12]  # List of months in numeric form
    
    for i in range(12):   # Iterate over numbers from 0 to 11
        if months[i] == month:  # Check if the number is in the range of 12
            if is_year_leap(year) == True:   # Check if the given year is a leap year
                return months_length_leap[i]  # Return months length if the year is a leap year
            else:
                return months_length[i]   # Return months length if the year is not a leap year

def day_of_year(year, month, day):
    if month in range(1,13):     # Checks if the month is within 1 to 12, 'None' is returened otherwise
      if day <= days_in_month(year, month):  # Check if the correct day is entered as per month/year, 'None' is returened otherwise
          day_yr = 0  # Initialise variable for day of year
          for m in range(1,13):   #Iterate over the range of months
              if m == (month):   # Check if m is the given month
                  break    # Break the loop
              else:
                  day_yr += days_in_month(year,m)    # Add days of year with days in month in each iteration
          return day_yr+day   # Return days of year adding the final months days
       

#Test code
print("Day of the year: ",day_of_year(2000, 12, 31))
print("Day of the year: ",day_of_year(2016, 12, 31))
print("Day of the year: ",day_of_year(2016, 12, 21))   # Incomplete month
print("Day of the year: ",day_of_year(1987, 12, 31))
print("Day of the year: ",day_of_year(1987, 12, 1))    # Start of month
print("Day of the year: ",day_of_year(1900, 12, 31))
print("Day of the year: ",day_of_year(12, 12, 31))     # Two digit year
print("Day of the year: ",day_of_year(1987, 13, 31))    # Wrong value of month
print("Day of the year: ",day_of_year(1900, 12, 50))    # Wrong value of day of month




