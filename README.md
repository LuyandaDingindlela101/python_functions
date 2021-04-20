#   DISTANCE _FROM_ZERO
Write a function called distance_from_zero, with one argument (choose any argument name you like). If the type of the argument is either int or float, the function should return the absolute value of the function input. Otherwise, the function should return “Nope”.

#   HOTEL_COST
   1. Define a function called hotel_cost with one argument nights as input. The hotel costs R140 per night.
   2. Define a function called plane_ride_cost that takes a string, city, as input.
   3. Define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car:
       3.1. Every day you rent the car costs R40 pep day.
       3.2. If you rent the car for 7 or more days, you get R50 off your total(cost-=50).
       3.3. If you rent the car for 3 or more days, you get R20.
       3.4. You cannot get both of the above discounts. Return  that cost.
   4. Define a function called trip_cost that takes two arguments, city and days. Your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.
       4.1. Modify your trip_cost function definition. Add a third argument, spending_money. Modify what the trip_cost function does. Add the variable ‘spending_money’ to the sum that it returns.

#   LEAP_YEAR
   Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

   In the Gregorian calendar, three conditions are used to identify leap years:
       The year can be evenly divided by 4, is a leap year, unless:
       The year can be evenly divided by 100, it is NOT a leap year, unless:
       The year is also evenly divisible by 400. Then it is a leap year.