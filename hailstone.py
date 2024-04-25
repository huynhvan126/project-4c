# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/24/2024
# Description: create the function definition for a hailstone sequence.
def hailstone(n):
    """Calculate the number of steps it takes to reach 1 in a Hailstone.
    n (int): the number of steps to reach the hailstone sequence."""
    if n <= 0
        return "Error - Input must be positive."
    step = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        step += 1
    return step
