# Functions Practice
# Emma
# 24 November 2023

def area_of_a_square(sidelength: float) -> float:
	"""calculate and print the area of a square.
	Results are in units squared.
	
	Params:
	sidelength - length of one side of the square
	"""

	area = sidelength ** 2

	return area


def print_area_of_a_square(sidelength: float):
	"""calculate and print the area of a square.
	Results are in units squared.
	
	Params:
	sidelength - length of one side of the square
	"""

	area = sidelength ** 2

	print(
		f"the area of a square with sidelength {sidelength} is: {area} square units"
		)


print(print_area_of_a_square(12.2))
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#   12.2 and 144
# Add the area of both squares

area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
print(area_of_squares)

# Question 1

def stars(number:int) -> str:
	"""Returns the number of stars
	
	Params:
	
	number - integer of the number of stars
	"""

	return number * "*"

print(stars(100))

# Question 2

def biggest_of_three(num_1:float, num_2:float, num_3:float ) -> float:
	"""Returns the biggest of the three numbers inputed.

	Params:
	num_1 - first number
	num_2 - second number
	num_3 - third number

	Returns:
	the biggest of the three numbers
	""" 
	
	if num_1 > num_2 > num_3 or num_1 > num_3 > num_2:
		return num_1
	elif num_2 > num_1 > num_3 or num_2 > num_3 > num_1:
		return num_2
	else:
		return num_3

print(biggest_of_three(3,4,5))
print(biggest_of_three(3,5,4))
print(biggest_of_three(5,4,3))

# Question 3

def pyramid(num_layers:int) -> int:
	"""Returns the number as the number of rows to form a pyramid
	
	Params:
	num_layers - the number of rows
	"""

	for i in range(num_layers):
		print("*" * (i + 1))

	return num_layers

print(pyramid(3))

# Question 4

def pyramid_mirror(num_layers_2:int) -> int:
	"""Returns the number as the number of rows to form a mirrored pyramid
	
	Params:
	num_layers - the number of rows
	"""

	for current_layer in range(1, num_layers_2 + 1):
		print(" " * (num_layers_2 - current_layer) + stars(current_layer))

	return num_layers_2
print(pyramid_mirror(5))