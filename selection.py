def selection_sort(inputArray):
    for i in range(0,len(inputArray)):
        min = i
        for j in range(i,len(inputArray)):
            if inputArray[j] < inputArray[min]:
                min = j
        if min != i:
            inputArray[min],inputArray[i] = inputArray[i],inputArray[min]
        print(inputArray)

selection_sort([5,4,3,2,1])
  
