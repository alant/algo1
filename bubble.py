def bubble_sort(inputArray):
    for i in range(0,len(inputArray)):
        for j in range(0,len(inputArray)-1):
            if inputArray[j]>inputArray[j+1]:
                inputArray[j],inputArray[j+1] = inputArray[j+1],inputArray[j]
                print(inputArray)

bubble_sort([5,4,3,2,1])
#print out 5
#print(len([5,4,3,2,1]))                
     
