from heapq import heappush, heappop

lowH =[]
highH = []
#source ='wk6_test2_1.txt'
source ='Median.txt'

f = open(source)
i = 0
first = 0
second = 0
medianSum = 0

for line in f:
    num = int(line.strip())
    i = i + 1
    if i == 1:
        first = num
        medianSum = medianSum + first
    if i == 2:
        second = num
        if first > second:
            first, second = second, first
        heappush(lowH, -first)
        heappush(highH, second)
        medianSum = medianSum + first
                
    if i > 2:
        if num < highH[0]:
            heappush(lowH, -num)
        else:
            heappush(highH,num)

        #if the heaps are not balanced, balance them
        # move from low to high
        if (len(lowH) - len(highH)) > 1:
            heappush(highH, -heappop(lowH))
        #move from high to low
        if (len(highH) - len(lowH)) >1:
            heappush(lowH, -heappop(highH))
        #figure out the median add to medianSum
        if len(highH) > len(lowH) :
            median = heappop(highH)
            heappush(highH, median)
        else :
            median = -heappop(lowH)
            heappush(lowH, -median)
        medianSum = medianSum%10000 + median            
        
#    print num
      #heappush(lowH, num)

      
#print lowH
#print highH
print medianSum
