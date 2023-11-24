---
tags:
  - programming-level-1-2
  - slss
  - y2023
---
# Functions

A function is a block of code that can be reused over and over again.

We can input data to the function. we refer to the data as **parameters.**

We describe the parameters in the docstring. A docstring (is short for document string) tells a human what the purpose of the function is.

We use the term **arguments** to describe the ACTUAL data that we put into the function.

```python
def area_of_a_square(sidelength: float):
	"""calculate and prinit the area of a square.
	Results are in units squared.
	
	Params:
	sidelength - length of one side of the square
	""""

	area = sidelength ** 2

	print(f"the are of a square with sidelength {sidelength} is: {area} square units")

area_of_a_square(12.2)
```

