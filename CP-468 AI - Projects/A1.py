"""
CP-468 Assignment 1 Part 2

    Authors:
        Sahil Khasnobish - 190990560

    Description: 
        - This program aims to retrieve city data including city names and 
        coordinates from a csv file. This data is imported into a data frame which includes
        columns such as latitude and longitude.
        - A distance matrix is created and filled with zeros, which then is filled with
        the euclidean distances using the helper function def euclidean_distance(i,j)
        - dfs() function performs depth first search calling the recursive function
        dfs_alg()
        - Names of the city path and final shortest total distance is the result
        - bfs() function perfroms breadth first search algorithm on the list of cities
            -The final result is names of cities travelted and total distance travelled

    Depth First Search Analysis
        - COMPLETENESS
            - In the travelling salesman problem, since it is a finite space, depth
            first search is complete as it visits each city.
        - COST OPTIMALITY
            - Not cost optimal, finds the first available solution, visits
            each city and goes back to the starting point.
        - TIME COMPLEXITY
            - Recursive step is O(n), inside each recursive call we iterate through all
            cities which is O(n).
            - Therefore time complexity is O(n^2)
        - SPACE COMPLEXITY
            - Branching factor, b, is 49.
            - Maximum depth m, is at level 49.
            - Therefore the space complexity is O(bm)

    Breadth First Search Analysis
        - COMPLETENESS
            -For the travelling salesman problem BFS would be conisdered complete. The algorithm
            will eventually travel to all the cities
        - COST OPTIMALITY
            - BFS Is not cost optimal, it explores all possible perumations of the cities making it
            impractical for large instances of the TSP.
        - TIME COMPLEXITY
            - Time complexity for TSP is O((n-1)!) where n is the number of cities.
            Total possible permutations of cities is (n-1)!
        - SPACE COMPLEXITY
            - Space required is proportional to the number of nodes in the search space.
            The space complexity is also exponential, O((n-1)!)
"""

import pandas as pd
import numpy as np

data = pd.read_csv(r'city_data_50.csv')  # Reads CSV file
df = pd.DataFrame(data)                 # Imports data into dataframe
cities = data["description"].copy()     # Cities
df = pd.DataFrame(data, columns=['latitude', 'longitude'])  # Longitude and Latitude
city_data = df.values  # Data containing city coordinates


"""
    def euclidean_distance(i,j)
    - Using index values i and j, calculates the euclidean distance by
    subtracting the jth city's coordinates and ith city's coordinates
"""


def euclidean_distance(x, y):
    # Calculates Euclidean Distance and saves into variable result
    result = np.sqrt(np.sum((city_data[y] - city_data[x]) ** 2))
    return result


"""
    This part fills the distance matrix with the euclidean distances
"""
distance_matrix=np.zeros(((df.values).shape[0],(df.values).shape[0]))  # Filling matrix
for i in range((df.values).shape[0]):
    for j in range((df.values).shape[0]):
        distance_matrix[i, j] = euclidean_distance(i, j)  # fill matrix with distance
"""
    def dfs(i,j)
    - Initializes visited array, this array contains cities that have been visited
    - Initializes distance variables, contains the total distance travelled
    - Initializes root_node, this is the node to perform recursion on
        - set to zero as we start from the first city which is Montgomery
        - this is updated each recursive call
    - function calls the recursive helper function dfs_alg()
"""


def dfs():
    visited = []  # initialize visited array
    distance = 0  # initialize distance variable
    root_node = 0  # initialize root_node
    dfs_alg(distance_matrix, root_node, visited, distance)  # call helper recursive function to perform dfs
    return


"""
    def dfs_alg(distance_matrix, root_node, visited, distance)
    - Performs Depth First Search starting at the root node
    - Each recursive call begins with appending the node into the visited array
    - The distance is updated, along with the city the function is currently at
    - It iterates through all other cities, every city is adjacent to every other
    city
    - root_node is updated if a neighbour is not in the visited array, and 
    dfs_alg() is called again
    - Once the function has arrived at the last city, it prints the shortest distance 
"""


def dfs_alg(distance_matrix, root_node, visited, distance):
    visited.append(root_node)  # append node to visited array
    distance += distance_matrix[0][root_node]  # update the distance

    print(cities[root_node])  # Display the city we are currently at
    if root_node == 49:  # If we have arrived at the final city, print the final distance
        print("\nSHORTEST DISTANCE = ", distance)
    for n in range(len(cities)):  # Iterate through cities
        if n not in visited:  # If a city has not been visited, update root node and perform dfs again
            root_node = n  # update root node
            dfs_alg(distance_matrix, root_node, visited, distance)  # call recursive function

    return distance  # return final distance

"""
    def bfs()
    - Initializes explored array, this array contains cities that have been visited
    - Initializes distance variables, contains the total distance travelled
    - Initializes start, this is the root node in which the algorithm starts from
        - set to zero as we start from the first city which is Montgomery
    -Initializes n, this is the number of cities
"""

def bfs():

    distance = 0
    start = 0

    print("\nThe shortest route using breadth first search algorithm is:\n")
    n = len(cities)
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == 49:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = cities[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in range(n): #Using in range because all the neighbours are each others neighbours already
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                neighbour+=1 #Move to arbituary next node/city since all nodes are connected 
                distance += distance_matrix[neighbour][start]
                print(new_path, cities[neighbour])

                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == 49: #In this case make last city the end node
                    print("\nSHORTEST DISTANCE = ", distance)
                    return
                   
            explored.append(node)
   


# Perform Depth First Search


dfs()


# Perform Breadth First Search

bfs()