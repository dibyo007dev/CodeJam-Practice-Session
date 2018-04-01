def merge(left,right):
    result = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(alist):
    if len(alist)<= 1:
        return alist
    
    mid= len(alist)//2

    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])

    return merge(left,right)

arr = [1,2,-1,5,0,9,65,32,7,3,6,3,1]

print(mergeSort(arr))
