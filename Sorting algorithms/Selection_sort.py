def selection_sort(alist):
    for i in range(len(alist)): #traverse whole list
        #find minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j
        #swap minimum found with first element
        alist[i], alist[min_index] = alist[min_index], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)

#Time complexity: best=O(n^2)
#                 worst=O(n^2)
#                 average=O(n^2)
#Space complexity: worst=O(1)