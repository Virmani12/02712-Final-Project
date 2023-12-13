import random
import numpy as np

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

        #Random distribution of fractions to determine location population sizes (to prevent skewness)
        rand_distr = np.random.dirichlet(np.ones(n_locations),size=1)
        pop_sum = 0

        #for each location, set its population size to be rand_fraction*N, 
        # where the last location is just the difference between n and the sum of the rest of the population sizes
        # this is done to prevent rounding errors from exceeding the total population size
        for i in range(n_locations):
            if i == n_locations-1:
                loc_size = n - pop_sum
                self.map.append(Location(loc_size, self.n_locations, i))
            else:
                loc_size = int(rand_distr[0][i]*n)
                self.map.append(Location(loc_size, self.n_locations, i))
                pop_sum += loc_size
    
            
        self.setup_connections()

    def setup_connections(self):

        #For each location, get random split of connections to non-connections
        # For each list of connections, assign random "c" value for that connection between 0 and the population size of j
        for loc in self.map:
            valid_locs = []
            for other_loc in self.map:
                if other_loc.ind != loc.ind:
                    if other_loc.n > 0:
                        valid_locs.append(other_loc)
        

            split = random.uniform(0,1)

            #print("split:",split)
            j_connections = random.sample(valid_locs, int(split*len(valid_locs)))

            for j in j_connections:
                #print("Size: ",self.map[j.ind].n)
                if self.map[j.ind].n == 1:
                    loc.connections[j.ind] = 1
                else:
                    loc.connections[j.ind] = random.randint(1,self.map[j.ind].n)
    

        
    #This function sets a random starting point for the pandemic by assigning its I value to 1 and decremening its S value
    def random_orgin(self):

        rand_start = random.randint(0,self.n_locations-1)
        rand_i = random.uniform(0,0.1)
        self.map[rand_start].i = self.map[rand_start].n*rand_i
        self.map[rand_start].s -= self.map[rand_start].n*rand_i

    def mobility_based_origin(self, threshold, highly):
        #This function takes the top X-percentile of highly or lowly connected regions (based on total number of outgoing connections) 
        # and sets their starting infection value to 1 while decreasing their susceptible by 1
            #highly = True if getting top X-percentile of highly connected locations, False if getting top X-percentile of lowly connected locations
            #threshold = top X-percentile to set as origin

        connection_count = {}

        for loc in self.map:
            connection_count[loc.ind] = sum(loc.connections.values())

        sorted_counts = sorted(connection_count.items(), key=lambda x: x[1], reverse=highly)
        threshold = int(len(sorted_counts)*threshold)
        top_keys = [item[0] for item in sorted_counts[:threshold]]

        for key in top_keys:
            self.map[key].i +=1
            self.map[key].s -=1
    
    def edit_connections(self,threshold):
        connection_count = {}

        for loc in self.map:
            connection_count[loc.ind] = sum(loc.connections.values())

        sorted_counts = sorted(connection_count.items(), key=lambda x: x[1], reverse=True)
        threshold = int(len(sorted_counts)*threshold)
        top_keys = [item[0] for item in sorted_counts[:threshold]]

        for loc in self.map:
            if loc.ind in top_keys:
                loc.connections = {i: 0 for i in range(self.n_locations) if i != loc.ind}
            else:
                for key in top_keys:
                    loc.connections[key] = 0


