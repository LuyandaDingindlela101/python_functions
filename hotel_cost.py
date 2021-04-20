#   Task - Compulsory
#   1. Define a function called hotel_cost with one argument nights as input. The hotel costs R140 per night.
#   2. Define a function called plane_ride_cost that takes a string, city, as input.
#   3. Define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car:
#       3.1. Every day you rent the car costs R40 pep day.
#       3.2. If you rent the car for 7 or more days, you get R50 off your total(cost-=50).
#       3.3. If you rent the car for 3 or more days, you get R20.
#       3.4. You cannot get both of the above discounts. Return  that cost.
#
#   4. Define a function called trip_cost that takes two arguments, city and days. Your function return the sum of
#       calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city)
#       functions.
#       4.1. Modify your trip_cost function definition. Add a third argument, spending_money. Modify what the trip_cost
#            function does. Add the variable ‘spending_money’ to the sum that it returns.

#   FUNCTION LETS YOU KNOW HOW MUCH IT WILL COST TO STAY AT A HOTEL FOR THE GIVEN AMOUNTS OF NIGHTS
def hotel_cost(nights):
    return "R" + str(140 * nights)


#   RETURNS THE PRICE OF YOUR PLANE TICKET DEPENDING ON THE city YOU ARE GOING TO
def plane_ride_cost(city):
    #   CREATE A DICTIONARY WITH THE CITY AS A KEY AND THE PRICE AS THE VALUE
    cities = {
        "Cape Town": 2500,
        "Durban": 2300,
        "JHB": 2000,
        "BFN": 1800
    }

    #   ASSIGN price TO THE GIVEN city
    price = cities.get(city)

    # IF price IS NOT None, MEANING THE city ENTERED EXISTS IN THE DICTIONARY
    if price is not None:
        #   RETURN THE price
        return "R" + str(price)
    else:
        #   IF THE GIVEN city ISN'T IN THE DICTIONARY, RETURN THE FOLLOWING
        return str(city) + " isn't in our data base"


#   RETURNS THE COST OF RENTING A CAR DEPENDING ON THE AMOUNT OF days
def rental_car_cost(days):
    #   IF YOU RENT OFR ONLY 2 DAYS, THEN NO DISCOUNT
    if 0 < days < 2:
        price = 40 * days
    #   IF YOU RENT FOR 3 - 6 DAYS, YOU GET R20 OFF
    elif 3 < days < 6:
        price = (40 * days) - 20
    #   IF YOU RENT FOR MORE THAN 7 DAYS, YOU GET R50 OFF
    else:
        price = (40 * days) - 50

    return "R" + str(price)


#   RETURNS THE TOTAL AMOUNT THE TRIP IS GONNA COST YOU DEPENDING ON THE city YOU GO TO, HOW MANY days YOU GONNA RENT A
#   CAR AND HOW MUCH spending_money YOU WANNA HAVE
def trip_cost(city, days, spending_money):
    # PRICE IS THE SUM OF THE FOLLOWING FUNCTIONS
    return "R" + str(rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money)
