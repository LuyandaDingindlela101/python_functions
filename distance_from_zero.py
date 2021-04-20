#   Write a function called distance_from_zero, with one argument (choose any argument name you like). If the type
#   of the argument is either int or float, the function should return the absolute value of the function input.
#   Otherwise, the function should return “Nope”.

#   DEFINE THE distance_from_zero FUNCTION
def distance_from_zero(to_test):
    #   TEST FOR THE int AND float DATA TYPES
    if type(to_test) == int or type(to_test) == float:
        # IF TRUE, RETURN THE ABSOLUTE VALUE
        return abs(to_test)
    else:
        # OTHERWISE RETURN "Nope"
        return "Nope"


#   CALL THE FUNCTION
print(distance_from_zero("what?"))

