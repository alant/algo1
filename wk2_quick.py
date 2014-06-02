def quickSort(array, l, r):
    if l < r:
        pivot = partition(array, l, r)
        quickSort(array,l,pivot-1)
        quickSort(array,pivot+1,r)

def partition(array, l, r):
    p = r
    i = l-1
    print ("l: %d, r: %d" % (l, r))
    for j in range(l,r):
#        print("p: %d, i: %d, j: %d" % (p, i, j))
        if array[j] < array[p]:
            i = i + 1
            array[i], array[j] = array[j], array[i]
#        print array
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
