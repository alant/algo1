import random
m = 0
def quickSort(array, l, r):
    if l < r:
        pivot = partition(array, l, r)
        quickSort(array,l,pivot-1)
        quickSort(array,pivot+1,r)

def partition(array, l, r):
    global m
    #p = random.randint(l,r)
    
    mid = (r-l)/2

    array = [0,1,2]
    mid = 1
    l = 0
    r = 2
    di = {array[l]:l, array[mid]:mid, array[r]:r}
    p= di[sorted([array[l],array[mid],array[r]])[1]]
    array[p],array[r] = array[r],array[p]
#    m = m + r - l - 1
    p = l
    i = l-1
#    print ("l: %d, r: %d" % (l, r))
    for j in range(l,r):
        m += 1
#        print("p: %d, i: %d, j: %d" % (p, i, j))
        if array[j] < array[r]:
            i = i + 1
            array[i], array[j] = array[j], array[i]
#            print array
#    print("pivot value: ", p)
#    print("index i: ", i)
    #this is also different from lecture`
    array[i+1],array[r] = array[r],array[i+1]
    return i+1
    
inputArray = []
#with open('testArray.txt') as f:
with open('QuickSort.txt') as f:
    for line in f:
        inputArray.append(int(line))
print(inputArray)

quickSort(inputArray,0,len(inputArray)-1)
print(inputArray)
#print(result)
print m
