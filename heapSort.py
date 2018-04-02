def swap(val1, val2):
    temp = val1
    val1 = val2
    val2 = temp

def max_heapify(alist,i):
    l= i
    r= 2*i

    if(l< len(alist) and alist[l]>alist[i]):
        largest = l
    else:
        largest=i

    if(l< len(alist) and alist[r]>alist[largest]):
        largest = alist[r]

    if(largest != i ):
        swap(alist[i],alist[largest])
        max_heapify(alist,largest)

def build_max_heap(alist):
    heap_size = len(alist)
    for i in range(len((alist/2)-1, 0)):
        max_heapify(alist,i)

def heap_sort(alist):
    build_max_heap(alist)
    for i in range(len(alist)-1, 1):
        swap(alist[0],alist[i])
        max_heapify(alist,0)

heap_sort([2,5,2,6,0,6,5,3,7,4,62])