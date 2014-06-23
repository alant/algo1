ograph = {1:{2:3,3:3}, 2:{3:1, 4:2}, 3:{4:50}, 4:{}}

source='dijkstraData.txt'
N=6
def getG():
    G={}
    for i in range(1,N+1):
        G[i]=[]
    fin=open(source)
    for line in fin:
        v1=int(line.split()[0])
        v2=line.split()[1:]
        #print v2
        edges = {}
        for x in v2:
            arrow= x.split(',')
            #print arrow[0]
            #print arrow[1]
            edges[int(arrow[0])]=int(arrow[1])
        G[v1]=edges
        ## for x, y in v2
        ##     G[v1].append(x,y)
    fin.close()
    print G
    return G


def dijkstra(net, s, t):
    # sanity check
    if s == t:
        return "The start and terminal nodes are the same. Minimum distance is 0."
    if net.has_key(s)==False:
        return "There is no start node called " + str(s) + "."
    if net.has_key(t)==False:
        return "There is no terminal node called " + str(t) + "."
    # create a labels dictionary
    labels={}
    # record whether a label was updated
    order={}
    # populate an initial labels dictionary
    for i in net.keys():
        if i == s: labels[i] = 0 # shortest distance form s to s is 0
        else: labels[i] = float("inf") # initial labels are infinity
    from copy import copy
    drop1 = copy(labels) # used for looping
    ## begin algorithm
    while len(drop1) > 0:
        # find the key with the lowest label
        minNode = min(drop1, key = drop1.get) #minNode is the node with the smallest label
        # update labels for nodes that are connected to minNode
        for i in net[minNode]:
            if labels[i] > (labels[minNode] + net[minNode][i]):
                labels[i] = labels[minNode] + net[minNode][i]
                drop1[i] = labels[minNode] + net[minNode][i]
                order[i] = minNode
        del drop1[minNode] # once a node has been visited, it's excluded from drop1
    ## end algorithm
    # print shortest path
    temp = copy(t)
    rpath = []
    path = []
    while 1:
        rpath.append(temp)
        if order.has_key(temp): temp = order[temp]
        else: return "There is no path from " + str(s) + " to " + str(t) + "."
        if temp == s:
            rpath.append(temp)
            break
    for j in range(len(rpath)-1,-1,-1):
        path.append(rpath[j])
    return labels[t]
#    return "The shortest path from " + str(s) + " to " + str(t) + " is " + str(path) + ". Minimum distance is " + str(labels[t]) + "."



graph={}
graph=getG()
answer=[]
answer.append(dijkstra(graph, s=1, t=7))
answer.append(dijkstra(graph, s=1, t=37))
answer.append(dijkstra(graph, s=1, t=59))
answer.append(dijkstra(graph, s=1, t=82))
answer.append(dijkstra(graph, s=1, t=99))
answer.append(dijkstra(graph, s=1, t=115))
answer.append(dijkstra(graph, s=1, t=133))
answer.append(dijkstra(graph, s=1, t=165))
answer.append(dijkstra(graph, s=1, t=188))
answer.append(dijkstra(graph, s=1, t=197))
print answer