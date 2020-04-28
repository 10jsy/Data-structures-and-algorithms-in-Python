def merge_sort(alist):
    if len(alist) > 1:
        #split list into midpoint, lefthalf and righthalf
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        #sort the left then right half
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = j = k = 0

        #copy data into temporary arrays
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]: #this line maintains algorithm stablility, ie maintains order of duplicate items
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        #check if any element was left
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
        
alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)

#Time complexity: best=O(n log(n))
#                 worst=O(n log(n))
#                 average=O(n log(n))
#Space complexity: worst=O(n)