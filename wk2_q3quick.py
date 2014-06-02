from statistics import median
def quickSort(array, l, r):
    if l < r:
        #do partition thing
        p=partition(array, l, r)
        quickSort(array,l,p-1)
        quickSort(array,p+1,r)
    return array

def partition(array, l, r):
    p = l
    #go through list and move p to the right place
    i = l + 1
    for j in range(l+1,r):
        if array[j] < array[p]:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[p], array[i-1] = array[i-1], array[p]
    return i;
    
inputArray = []
with open('testArray.txt') as f:
    for line in f:
        inputArray.append(int(line))
        #print(inputArray)

result=quickSort(inputArray,0,len(inputArray)-1)
#print(inputArray)
print(result)
