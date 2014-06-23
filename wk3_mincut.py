import random
import copy
import sys

def contract(input):
    g = copy.deepcopy(input)
    next_id = max(g.iterkeys()) + 1
    cuts = {}
    while len(g) > 2:
        p1 = random.choice(g.keys())
        p2 = random.choice(g[p1].keys())
        merged = next_id
        cuts[merged] = cuts.pop(p1) if p1 in cuts else [p1]
        cuts[merged] += cuts.pop(p2) if p2 in cuts else [p2]
        g[p1].pop(p2)
        g[p2].pop(p1)
        for dest in g[p1].iterkeys():
            g[dest][merged] = g[dest].pop(p1)
        for dest in g[p2].iterkeys():
            g[dest][merged] = g[dest].get(merged, 0) + g[dest].pop(p2)
        g[merged] = g.pop(p1)
        for dest, cnt in g.pop(p2).iteritems():
            if dest == p1:
                continue
            g[merged][dest] = g[merged].get(dest, 0) + cnt
        next_id += 1
    return cuts.values(), g.values()[0].values()[0]

inputGraph = {}
i = 0
with open('wk3_test.txt') as f:
#with open('kargerMinCut.txt') as f:
    for line in f:
       i = i + 1
       items = line.split()
       edges = {}
       for edge in items[1:]:
           edges[int(edge)] = 1
       inputGraph[int(items[0])] = edges
print inputGraph
print len(inputGraph)
print i
min_cut = []
min_edges = 9999
for x in range (0,40000):
    cut, num_edges = contract(inputGraph)
    if num_edges < min_edges:
        min_edges = num_edges
print min_edges
    
    
