def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last): # first=0 and last=len-1
    if first<last:

        splitpoint = partition(alist,first,last) # return the splitpoint

        quickSortHelper(alist,first,splitpoint-1) #left list
        quickSortHelper(alist,splitpoint+1,last) #right list


def partition(alist,first,last):
    pivotvalue = alist[first] # default; use first in the list as pivot value

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else: # exchange
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first] #split point exchange
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark #split point

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)