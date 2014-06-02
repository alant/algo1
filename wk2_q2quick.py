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
    p = r
    array[p],array[l] = array[l],array[p]
#    m = m + r - l - 1
    i = l
#    print ("l: %d, r: %d" % (l, r))
    for j in range(l+1,r+1):
        m +=1
#        print("p: %d, i: %d, j: %d" % (p, i, j))
        if array[j] < array[l]:
            i = i + 1
            array[i], array[j] = array[j], array[i]
#            print array
#    print("pivot value: ", p)
#    print("index i: ", i)
    #this is also different from lecture`
    array[i],array[l] = array[l],array[i]
    return i
    
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
