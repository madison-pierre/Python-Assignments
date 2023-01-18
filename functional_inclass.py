# Dr Michaels
# 11/1/21
# functional_inclass.py

from functools import reduce


# Create a function that takes as input two arrays of integers and returns an array containing the GCD of each corresponding pair of values.
# For the GCD function you may make use of a recursive definition (not a while loop based one)
# BONUS if you create a lambda version of GCD (hint it also utilizes recursion)
def function_one(array_one, array_two):
    return "function one!"


# Create a function that will compare each corresponding pair of elements in the input arrays.
# It will then return whichever array had the most "victories" (the most occurrences of its item being greater than the corresponding input array
def function_two(array_one, array_two):
    return "Function two!"

# Function three will return the item that occurs the highest number of times in the input array
# HINT: Use a dictionary to store the number of occurrences of each item 
# You may wish to define a helper function to assist in this
def function_three(array_one):
    return "Function three!"

# Function four will take as input two arrays and return a matrix (2D array)
# You will take each value from the first array and perform an operation with each value of array two. 
# If the value in array two is greater than the value from array one, we return the values multiplied together (val1 * val2).
# If the value in array two is less than the value from array one, we will return the negation (val * -1) of the value in array one.
# If the two values are equal, we return the value squared.
def function_four(array_one, array_two):
    return "Function four!"



def main():
    print("This file contains implementation of the three functions in our functional in class assignment")
    print("We will use the following arrays to test our functions")
    array_one = [1,2,3,4,5,6,7,8,9,10]
    array_two = [5,8,18,12,2,3,49,12,21,55]
    array_three = [15,86,21,48,75,12,54,32,19,25]
    array_four = [121,144,287,54,123,42,98,144,210,110]
    array_five = [121, 145, 286, 55, 123, 41, 97, 145, 211, 109]
    array_six = [1,2,3,4,5,1,2,3,4,1,2,3,2,1,2,1,2,3,5,4,3,2,1,1,2,3,3]
    print("Array one: %s" % array_one)
    print("Array two: %s" % array_two)
    print("Array three: %s" % array_three)
    print("Array four: %s" % array_four)
    print("Array five: %s" % array_five)
    print("Array six: %s" % array_six)
    print("Calling function one with arrays one and two: %s" % function_one(array_one, array_two))
    print("It should return the following result: [1, 2, 3, 4, 1, 3, 7, 4, 3, 5]")
    print("Calling function one with arrays two and three: %s" % function_one(array_three, array_two))
    print("It should return the following result: [5, 2, 3, 12, 1, 3, 1, 4, 1, 5]")
    print("Calling function one with arrays three and four: %s" % function_one(array_three, array_four))
    print("It should return the following result: [1, 2, 7, 6, 3, 6, 2, 16, 1, 5]")
    
    print("\n\n*******************************************")
    print("We will now call function two! This function compares the contents of two arrays and returns a string declaring the \"victor\"")
    print("Calling function two with arrays one and two:\n%s" % function_two(array_one, array_two))
    print("It should return:\nThe array with the most victories is: [5, 8, 18, 12, 2, 3, 49, 12, 21, 55]")
    print("Calling function two with arrays five and four:\n%s" % function_two(array_four, array_five))
    print("It should return:\nThe arrays had an equal number of victories!")
    
    print("\n\n*******************************************")
    print("Now for function three! It will return the item which has the highest number of total occurrences in the input array")
    print("Calling function three with array six! The result is %s" % function_three(array_six))
    print("It should return: 2")
    
    print("\n\n*******************************************")
    print("Now for function four! It will take as input two arrays and return a matrix (2D array)")
    print("Calling function four with arrays two and three!\n%s" % function_four(array_two, array_three))
    print("It should return:\n[[75, 430, 105, 240, 375, 60, 270, 160, 95, 125], [120, 688, 168, 384, 600, 96, 432, 256, 152, 200], [-15, 1548, 378, 864, 1350, -12, 972, 576, 342, 450], [180, 1032, 252, 576, 900, 144, 648, 384, 228, 300], [30, 172, 42, 96, 150, 24, 108, 64, 38, 50], [45, 258, 63, 144, 225, 36, 162, 96, 57, 75], [-15, 4214, -21, -48, 3675, -12, 2646, -32, -19, -25], [180, 1032, 252, 576, 900, 144, 648, 384, 228, 300], [-15, 1806, 441, 1008, 1575, -12, 1134, 672, -19, 525], [-15, 4730, -21, -48, 4125, -12, -54, -32, -19, -25]]")
    print("Calling function four with arrays four and five!\n%s"% function_four(array_four, array_five))
    print("It should return:\n[[14641, 17545, 34606, -55, 14883, -41, -97, 17545, 25531, -109], [-121, 20880, 41184, -55, -123, -41, -97, 20880, 30384, -109], [-121, -145, -286, -55, -123, -41, -97, -145, -211, -109], [6534, 7830, 15444, 2970, 6642, -41, 5238, 7830, 11394, 5886], [-121, 17835, 35178, -55, 15129, -41, -97, 17835, 25953, -109], [5082, 6090, 12012, 2310, 5166, -41, 4074, 6090, 8862, 4578], [11858, 14210, 28028, -55, 12054, -41, -97, 14210, 20678, 10682], [-121, 20880, 41184, -55, -123, -41, -97, 20880, 30384, -109], [-121, -145, 60060, -55, -123, -41, -97, -145, 44310, -109], [13310, 15950, 31460, -55, 13530, -41, -97, 15950, 23210, -109]]")



main()