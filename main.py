from initialization import Location
from initialization import Grid
import random




def main():
    a = 0.5
    b = 0.3
    mu = 0.1
    N = 10000
    n_locations = 10

    grid1 = Grid(n_locations, N, a, b, mu)
    print(grid1.map[0].connections)


main()


