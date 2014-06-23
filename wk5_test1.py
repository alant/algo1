source='dijkstratest1.txt'
N=4
def getG():
    G={}
    for i in range(1,N+1):
        G[i]=[]
    fin=open(source)
    for line in fin:
        v1=int(line.split()[0])
        v2=line.split()[1:]
        print v2
        for x in v2:
            arrow= x.split(',')
            print arrow[0]
            print arrow[1]
            edge = {}
            edge[int(arrow[0])]=int(arrow[1])
            G[v1].append(edge)
        ## for x, y in v2
        ##     G[v1].append(x,y)
    fin.close()
    print G
    return G


getG()
