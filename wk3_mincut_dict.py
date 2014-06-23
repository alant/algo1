import random

#inputG = {}
vertices = []
edges = []

def randomContract(inGraph):
    if len(inGraph) == 2:
        return (inGraph.itervalues().next()).values()[0]
    else:
        #HINT: Note that you'll have to figure out an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction. But you should also think about more efficient implementations.
        #edge contraction
        #randomly select an edge
        #outEdge = random.choice(inGraph.keys())
        #creating a new graph
        #randomContract(newGraph)
        pass

with open('wk3_test2.txt') as f:
    for line in f:
        items = line.split()
        num = int(items[0])
        vertices.append(num)
        edgesC = items[1:]
        for edge in edgesC:
            num1 = int(items[0])
            num2 = int(edge)
            edges.append([num1,num2,1])
    print vertices
    print edges
    testOut = random.choice(edges)
    print testOut
#mincut=randomContract(inputG)
print mincut
