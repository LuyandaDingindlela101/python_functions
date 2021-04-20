#   Task
#   Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise
#   return False.

#   In the Gregorian calendar, three conditions are used to identify leap years:
#       The year can be evenly divided by 4, is a leap year, unless:
#       The year can be evenly divided by 100, it is NOT a leap year, unless:
#       The year is also evenly divisible by 400. Then it is a leap year.

#   DEFINE THE is_leap FUNCTION
def is_leap(year):
    #   CREATE is_leap VARIABLE TO HOLD BOOLEAN VALUE
    #   MAKE THE DEFAULT VALUE FALSE
    leap = True
    #   TEST THE FIRST CASE, YEAR MUST BE EVENLY DIVISIBLE BY 4
    if year % 4 == 0:
        #   TEST THE OTHER CASES, YEAR MUST BE NOT EVENLY DIVISIBLE BY 100 OR YEAR MUST BE EVENLY DIVISIBLE BY 100
        if year % 100 != 0 or year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = False

    return leap


#   CALL THE FUNCTION
print(is_leap(600))


