from functools import reduce
from functools import partial
import random

some_val = 0

def increment():
	global some_val
	some_val += 2

def increment2(my_val):
	return (my_val + 2)

def my_add(a,b):
	return a + b

def power(base, exp):
	return base ** exp

def main():
	print("This program will demonstrate a number of functional and non-functional design principles.\n")
	global some_val
	increment()
	print("some_val is currently %d" % some_val)
	some_val = 15
	increment()
	print("some_val is currently %d" % some_val)
	my_val = 5
	print("After calling increment2 my_val is currently %d" % increment2(my_val))
	
	print("\nWe will now display objects as functions")
	my_plus = my_add
	print("We are using my_add to add 5 and 10: %d" % (my_add(5,10)))
	print("We are using my_plus to add 5 and 10: %d" % (my_plus(5,10)))
	
	print("\nLet us look at Lambda functions. Lambda functions are in-line function definitions")
	print("This line will add 8 and 7 together: %d" % ((lambda a,b: a + b)(8,7)))
	print("The above print statement defined an add function inside the print statement")
	print("The majority of our lambda usages will be a bit more complex :)")
	print("One of the main uses of lambda is to provide brief functions to operations from functools")
	print("We will look at map (now standard), reduce, partial and filter today")
	my_data = [1,2,3,4,5,6,7,8,9,10]
	squared_data = map(lambda a: a ** 2, my_data)
	print(squared_data)
	print("The above data doesn't display well does it!")
	print("We must wrap it inside a list call to make it viewable as normal")
	print(list(squared_data))
	print("We can pass in regular functions to map as well")
	add_data = map(increment2, my_data)
	print(list(add_data))
	my_names = ['Adam', 'Bob', 'Carla', 'Dawn', 'Eric']
	nick_names = ['Gamer1', 'Senator2', 'Professor3', 'Student4', 'Sleeper5']
	secret_names = list(map(lambda x: random.choice(nick_names), my_names))
	print(secret_names)
	
	print("\nThe next operator is reduce. This will compress a list into one value")
	print("The first one we will look at is simulating a factorial")
	red_factorial = reduce(lambda x, y: x * y, my_data, 1)
	print("Our simulated factorial is: %d" % red_factorial)
	print("We will make a list of 10 random numbers and then use reduce to pull out the max and min value")
	random_nums = []
	for i in range(10):
		random_nums.append(random.randint(1,100))
		
	print("Our random list is: %r" % random_nums)
	print("The max val from random_nums is: %d" % (reduce(lambda a,b: a if a > b else b, random_nums)))
	print("The min val from random_nums is: %d" % (reduce(lambda a,b: a if a < b else b, random_nums)))
	
	print("\nThe second to last thing we shall test today is the idea of making partial functions")
	print("This means that instead of assigning everything in the function call, we hold a few values constant")
	cube = partial(power, exp = 3)
	print("Using power(5,3) we get: %d" % power(5,3))
	print("Using cube(5) we get: %d" % cube(5))

	print("\nLastly we shall look at filtering!")
	print("Filter works as you would expect, it returns a subset matching some condition")
	even = list(filter(lambda a: a % 2 == 0, random_nums))
	odd = list(filter(lambda a: a % 2 == 1, random_nums))
	print("Our even filter is: %r" % even)
	print("Our odd filter is: %r" % odd)

main()