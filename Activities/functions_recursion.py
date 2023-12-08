# Functions and Recursion
# Emma
# 6 December 2023

import time

def factorial(num: int) -> int:
    """returns the result of the number's factorial using recursion
    
    Params:
        num - number we're calculating 

    Returns:
        result
    """
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return factorial(num-1) * num

def fib(n:int) -> int:
    """Calculates and returns the nth Fibonacci number."""

    if n in [1, 2]:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

def fib_itr(n: int) -> int:
    """Returns the nth Fibonacci number.
    Calculates this iteratively."""
    last_num, num, result = 0, 1, 0

    for _ in range(n-1):
        result = last_num + num

        num, last_num = result, num

    return result

time_initial = time.perf_counter()
fib_itr(20)
time_final = time.perf_counter()

print(f"Iterative: {time_final - time_initial}")

time_initial = time.perf_counter()
fib(20)
time_final = time.perf_counter()

print(f"Recursive: {time_final - time_initial}")