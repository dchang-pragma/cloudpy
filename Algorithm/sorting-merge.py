def mergeSort(alist):
    print("Splitting ",alist) # show splitting process
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid] # O(k)
        righthalf = alist[mid:]

        mergeSort(lefthalf) # split
        mergeSort(righthalf)
### start merging
        i=0 #left index
        j=0 # right index
        k=0 # alist index
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist) # show merging process

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)