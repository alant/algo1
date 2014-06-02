import random

def contraction_algo(vertices, edges):
    '''
    Karger's recursive randomized algorithm for finding the min cut with Pr[1/n(n-1)] of success.
    This must be called many times to guarantee an overall high probability of success.
    '''
    # Check if base case conditions are met (there is 1 edge left)
    if len(edges) == 1:
        return edges[0][2];    # Return the parallel edge count of the last remaining edge.

    # Pick a random edge from the remaining edges.
    rand_edge = random.randint(0, len(edges) - 1)
    # Combine vertices with the common edge.
    if edges[rand_edge][0] < edges[rand_edge][1]:
        vert1 = edges[rand_edge][0]        # Head vertex
        vert2 = edges[rand_edge][1]        # Tail vertex
    else:
        vert1 = edges[rand_edge][1]        # Head vertex
        vert2 = edges[rand_edge][0]        # Tail vertex

    print "vert1, 2:"
    print vert1, vert2
    
    # Reassign the edges to vert1 and remove vert2.
    i = 0
    while len(edges) > i:        # TODO --- Go through only the edges that vert2 keeps track of.
        if vert2 in edges[i][:2]:    # Don't include the parallel edges count.
            if vert1 in edges[i][:2]:    # Delete self-loops
                edges.pop(i)
            else:
                if vert2 == edges[i][0]:
                    vert3 = edges[i][1]
                else:
                    vert3 = edges[i][0]
                    # Check if an edge already exists between vert1 and vert3. If so, add 1 to the parallel lines count and remove redundant edge.
                found_duplicate_edge = False
                for edge in edges:
                    if vert1 in edge[:2] and vert3 in edge[:2]:
                        edge[2] += edges[i][2]
                        found_duplicate_edge = True
                        break
                if found_duplicate_edge == False:
                    if vert3 == edges[i][0]:
                        edges[i][1] = vert1
                    else:
                        edges[i][0] = vert1
                        i += 1
                else:
                    edges.pop(i)
        else:
            i += 1
    new_verts = []
    for i in range(len(vertices)):
        if i != vert2:
            new_verts.append(vertices[i])
    # Remember that parallel lines are possible
    # i.e     I need to add in a counter for each edge element which keeps track of the number of parallel lines to the edge.

    # Feed the new vertices and edge values into a recursive call of this function.
    # i.e. return contraction_algo(vertices, edges)
    
    print "new verts:"
    print new_verts
    print "new edges:"
    print edges
    
    return contraction_algo(new_verts, edges)

with open('wk3_test.txt') as f:
    data = [map(int, line.split()) for line in f]
#    for row in data:
#        print row
    inputVert = []
    inputEdges= []
    for vortex in data:
        inputVert.append(vortex[0])
        for vortex2 in vortex[1:]:
            inputEdge = []
            inputEdge = [vortex[0],vortex2,1]
            print inputEdge
            inputEdges.append(inputEdge)
    print inputVert
    print inputEdges
    minCut = contraction_algo(inputVert,inputEdges)
    for x in range(0, 256):
        retryMincut = 9999
        retryMinCut = contraction_algo(inputVert,inputEdges)
        if retryMincut < minCut :
            minCut = retryMincut
    print minCut