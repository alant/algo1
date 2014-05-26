def mergeSort(array):
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
            if leftArray[i] < rightArray[j]:
                array[k] = leftArray[i]
                i=i+1
            else:
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
               

inputArray = [5,4,3,2,1,6]
mergeSort(inputArray)
print(inputArray)
