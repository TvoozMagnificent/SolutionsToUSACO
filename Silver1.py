
dictionary = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve(graph):

    count = 0
    flag = 1

    if len(graph) == len({*graph.values()}) == len(dictionary): # length of graph is length of targets --> made of pure loops
        if graph == {i: i for i in dictionary}: return 0 # we are already done, nothing needed
        else: return-1 # impossible

    while graph: # while not finished

        path = []
        possible = [vertex for vertex in graph if vertex not in graph.values()] # sources
        if possible: current = possible[0] # if there is a source, use a source
        else: current = [*graph][0] # else use a random vertex, since we only have pure loops left
        while current not in path: # follow down the path
            path.append(current) # add current node
            if current not in graph: break # no next node: just a tree
            current = graph.pop(current) # delete vertex and follow down
        if current == path[-1]: # happens either when we have a self loop or a sink
            count += len(path) - 1 # length - 1 moves
        elif current == path[0]: # happens when we used a random vertex and finds a pure loop
            count += len(path) + 1 # length + 1 moves
        else: # unpure loop
            count += len(path) # length moves

    return count # return number of moves

def do():
    f=input();t=input() # get input
    graph={}
    for F,T in zip(f,t):
        if F in graph:
            if graph[F]==T:continue # the same character, ignored
            else:return-1 # impossible
        graph[F]=T
    return solve(graph) # solve

for _ in range(int(input())):print(do()) # do
