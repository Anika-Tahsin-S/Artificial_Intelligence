from queue import PriorityQueue

with open('Heuristic_Value.txt', 'r') as f:
   lines = f.readlines()

GRAPH = {}
# Nested dictionary
for s in lines: 
    split_line = s.rstrip().split(" ") # splitted each value
    first = split_line[0].strip()
    GRAPH[first] = {} # kept the 0 indexing of each line as key
    
    pairs = [] # new list
    # now items in split_line will take values from 0 (which is now index 1 from original) to line's end with increment sequence 2
    for i in range(0, len(split_line[2:]), 2):
        pairs.append(split_line[2:][i:i+2]) # pairing up, starting from index 2, stops after +2 for each pair
    #print(pairs)

    for pair in pairs:
        city = pair[0].strip()
        val = pair[1].strip()
        GRAPH[first].setdefault(city, val) # default dictionary

#print(GRAPH)

# Hueristic value to Bucharest
def getHeuristics():
    heuristics = {}
    for i in lines:
        node_heuristic_val = i.split()
        heuristics[node_heuristic_val[0]] = int(node_heuristic_val[1])
    return heuristics


def a_star(source, destination):

    straight_line = getHeuristics()
    
    priority_queue, visited = PriorityQueue(), {} # Taking empty parameters
    priority_queue.put((straight_line[source], 0, source, [source])) # Putting heuristic source city index, initial 0, A* source and it's index
    visited[source] = straight_line[source] # here every visited source is the city's visited w/ heuristic

    while not priority_queue.empty(): # when priority queue is not empty
        (heuristic, cost, vertex, path) = priority_queue.get() # we get the heuristic value, cost, each vertex and the path city
        if vertex == destination: # now here the vertex is our given destination
            return heuristic, cost, path # then we are returning it's heurtic and path

        for next_node in GRAPH[vertex].keys(): # Now for the next_node (the keys) after the vertex 
            current_cost = (cost) + int(GRAPH[vertex][next_node]) # Calculating curr_cost = 0 + next_node cost
           
            heuristic = current_cost + straight_line[next_node] # the curr_cost + that next_node's heuristic
      
            if not next_node in visited or visited[next_node] >= heuristic: # now if the next_node not is visited or >= heuristic we got
                visited[next_node] = heuristic # assigning it equal
                priority_queue.put((heuristic, current_cost, next_node, path + [next_node])) # outting the new values we got from calc in the priority_queue



print('Start Node :', end=' ') # Arad
source = input().strip()
print('Destination :', end=' ') # Bucharest
goal = input().strip()

if source not in GRAPH or goal not in GRAPH:
    print('\nNO PATH FOUND')
else:
    heuristic, cost, optimal_path = a_star(source, goal)
    
    # print('\nPath:', ' -> '.join(city for city in optimal_path))
    # print('Total Distance =', heuristic, 'km')

    with open("output_file.txt", 'w') as f:
        f.write('Path: ')
        f.write(' -> '.join(city for city in optimal_path))
        f.write('\nTotal Distance = ')
        f.write('{}'.format(heuristic))
        f.write(' km')
        f.close()