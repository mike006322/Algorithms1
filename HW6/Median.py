# 2 heaps, HeapLow and HeapHigh, both with extract min but HeapLow will input numbers as negative
# HeapHigh.heaplist[1] = min element in HeapHigh
# -1*HeapLow.heaplist[1] = max element in HeapLow
# HeapHigh.currentSize = the size of heap high
# HeapLow.currentSize = the size of heap Low
# say that Heap High will always contain the median when they are different

from heap import MikesFirstHeap

HeapLow = MikesFirstHeap()
HeapHigh = MikesFirstHeap()

medians = []
count = 0
def addMedian():
    global medians
    medians.append(HeapHigh.heapList[1])
    #= (medians + HeapHigh.heapList[1]) % 10000
    global count
    count += 1
    #print('Now HeapHigh has ', HeapHigh.currentSize, ', HeapLow has ', HeapLow.currentSize)
    #print('meadians gets ', HeapHigh.heapList[1], ' from HeapHigh')
    
def addAverage():
    global medians
    medians.append(-HeapLow.heapList[1])
    #= (medians + (HeapHigh.heapList[1] + -HeapLow.heapList[1]) / 2) % 10000
    global count
    count += 1
    #print('Now HeapHigh has ', HeapHigh.currentSize, ', HeapLow has ', HeapLow.currentSize)
    #print('meadians gets ', (HeapHigh.heapList[1] + -HeapLow.heapList[1])/2, ' average of HeapHigh and HeapLow' ) 

for j in open('Median.txt', 'r'):
    i = int(j)
    #print('==> Add ',i, ' HeapHigh has ', HeapHigh.currentSize, ', HeapLow has ', HeapLow.currentSize)
    if HeapHigh.currentSize == 0:
        HeapHigh.insert(i)
        addMedian()
    elif HeapHigh.currentSize == HeapLow.currentSize:
        if i >= HeapHigh.heapList[1]:
            HeapHigh.insert(i)
            addMedian()
        else:
            HeapLow.insert(-i)
            j = HeapLow.extractMin()
            HeapHigh.insert(-j)
            addMedian()
    elif HeapHigh.currentSize > HeapLow.currentSize:
        if i >= HeapHigh.heapList[1]:
            HeapHigh.insert(i)
            j = HeapHigh.extractMin()
            HeapLow.insert(-j)
            addAverage()
        else:
            HeapLow.insert(-i)
            addAverage()
    
def modsum(L, m):
    result = 0
    for number in L:
        result = (result+number)%m
    return result
    
print(modsum(medians, 10000), count, len(medians))
    