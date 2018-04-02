def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotVal= alist[first]

    leftmark = first+1
    rightmark = last
## Endpoint for while loop
    done = False
    while not done:
        while leftmark<= rightmark  and alist[leftmark]<= pivotVal:
            leftmark +=1
        while leftmark <= rightmark and alist[rightmark]>= pivotVal:
            rightmark -=1
        
        if(leftmark>rightmark):
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

arr = [4,1,4,2,6,38,3,435,9,88,23,7546,23,65,2]

quickSort(arr)

print(arr)