splitInv = 0
def mergeSort(array):
    global splitInv
    inversion = 0
    if (len(array) > 1):
        midPoint = len(array)/2
        leftArray = array[:midPoint]
        rightArray = array[midPoint:]
        ## testArray = [1,2,3,4]
        ## print(testArray[2:])
        ## print(testArray[:2])
        mergeSort(leftArray)
        mergeSort(rightArray)
        i=0
        j=0
        k=0
        while (i<len(leftArray)) and (j<len(rightArray)):
            inversion = inversion + countInversion(leftArray)
            inversion = inversion + countInversion(rightArray)
                        
            if leftArray[i] < rightArray[j]:
                array[k] = leftArray[i]
                i=i+1
            else:
                splitInv = splitInv + len(leftArray)-i
                array[k] = rightArray[j]
                j=j+1
            k=k+1

        while (i<len(leftArray)):
            array[k] = leftArray[i]
            i=i+1
            k=k+1

        while (j<len(rightArray)):
            array[k] = rightArray[j]
            j=j+1
            k=k+1
    else:
        return array
    return splitInv

def countInversion(iArray):
    inv=0
    for i in range(0,len(iArray)):
        pass
    return 0

inputArray = []
with open('IntegerArray.txt') as f:
    for line in f:
        inputArray.append(int(line))
#print(inputArray)

result=mergeSort(inputArray)
#print(inputArray)
print(result)