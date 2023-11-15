from initialization import Location
from initialization import Grid
import random

def lowly_connected():
    a = 0.5
    b = 0.3
    mu = 0.1
    N = 10000
    n_locations = 20
    grid1 = Grid(n_locations, N, a, b, mu)
    grid1.mobility_based_origin(0.1,False)

    for item in grid1.map:
        #print(item.ind)
        #print(item.connections)
        print("Sum of connections:", sum(item.connections.values()))
        print("S:",item.s)
        print("I:", item.i)
        print("")



def highly_connected():
    a = 0.5
    b = 0.3
    mu = 0.1
    N = 10000
    n_locations = 10
    grid1 = Grid(n_locations, N, a, b, mu)
    grid1.mobility_based_origin(0.1,True)

    for item in grid1.map:
        #print(item.ind)
        #print(item.connections)
        print("Sum of connections:", sum(item.connections.values()))
        print("S: ",item.s)
        print("I: ", item.i)
        print("")

    #grid1.random_orgin()
    #for item in grid1.map:
    #    
    #    print("")



def main():
    a = 0.5
    b = 0.3
    mu = 0.1
    N = 10000
    n_locations = 10

    grid1 = Grid(n_locations, N, a, b, mu)


    print(grid1.map[0].connections)


#main()

highly_connected()

#lowly_connected()
