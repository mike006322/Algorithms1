file = open('IntegerArray.txt', 'r')
a = []
for i in range(100000):
    a.append(file.readline())


inv = 0
def mergeSort(alist):

    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
                
            else:
                alist[k]=righthalf[j]
                j=j+1
                global inv
                inv += len(lefthalf)-i
                
                #print(len(lefthalf)-i)
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            
            inv += len(lefthalf)-i
            k=k+1
    #print("Merging ",alist)


alist = [6,5,4,3,2,1]
mergeSort(a)
#print(alist)
print(inv)


