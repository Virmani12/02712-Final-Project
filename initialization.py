import random

class Location:

    def __init__(self, N, n_locations, ind):
        self.n = N
        self.s = N
        self.i = 0
        self.r = 0
        self.ind = ind

        #setting up connections that skips over itself
        self.connections = {i: 0 for i in range(n_locations) if i != ind}


class Grid:

    def __init__(self, n_locations, N, a, b, mu):

        self.map = []
        self.n_locations = n_locations
        self.n = N
        self.alpha = a
        self.beta = b
        self.mu = mu


        #Setting up initial population sizes per location, providing number of total locations, and index of each location
        n = self.n
        for i in range(n_locations):
            rand_n = random.randint(0,n)
            self.map.append(Location(rand_n, self.n_locations, i))
            n -= rand_n
    
        self.setup_connections()
        self.random_orgin()

    def setup_connections(self):


        #For each location, get random split of connections to non-connections
        # For each list of connections, assign random "c" value for that connection between 0 and the population size of j
        for loc in self.map:

            split = random.uniform(0,1)

            print("split:",split)
            j_connections = random.sample(loc.connections.keys(), int(split*(self.n_locations-1)))

            for j in j_connections:
                loc.connections[j] = random.randint(1,self.map[j].n)
        
    #This function sets a random starting point for the pandemic by assigning its I value to 1 and decremening its S value
    def random_orgin(self):

        rand_start = random.randint(0,self.n_locations)
        self.map[rand_start].i = 1
        self.map[rand_start].s -= 1


