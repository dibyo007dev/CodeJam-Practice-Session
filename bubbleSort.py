def bubbleSort(alist):
    for i in range(1,len(alist)):
        for j in range(len(alist)-i):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    return alist;

print(bubbleSort([5,24,6,1,5,2,5,1,89,23]))