def selection_sort(inputArray):
    for i in range(1,len(inputArray)):
        j = i
        while (j>0) and inputArray[j-1] > inputArray[j]:
            inputArray[j-1],inputArray[j] = inputArray[j],inputArray[j-1]
            j-=1
            print(inputArray)

selection_sort([5,4,3,2,1])
     
