def numberGuess(alist, key):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == key :
            found = True
        else:
            if key < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

testList = [0, 4, 9, 10, 34, 76, 89]

print(numberGuess(testList, 10))