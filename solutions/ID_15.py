# Lattice Paths
# Problem 15
#
# Starting in the top left corner of a 2x2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?

import math

def lattice_paths(grid_size: int) -> int:
    """
    Calculates the number of routes through a square grid of a given size,
    moving only right and down.

    This is a classic combinatorics problem. The number of paths is given by
    the central binomial coefficient (2n choose n), where n is the grid size.
    """
    n = grid_size
    return math.factorial(2 * n) // (math.factorial(n) * math.factorial(n))

if __name__ == '__main__':
    # For a 2x2 grid, the answer is 6.
    print(f"Number of routes for a 2x2 grid: {lattice_paths(2)}")
    # For a 20x20 grid, which is the problem to solve.
    print(f"Number of routes for a 20x20 grid: {lattice_paths(20)}")
