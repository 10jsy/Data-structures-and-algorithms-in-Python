def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        pos = index

        while pos > 0 and alist[pos-1] > current_value:
            alist[pos] = alist[pos-1]
            pos = pos - 1
        
        alist[pos] = current_value

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)

#Time complexity: best=O(n)
#                 worst=O(n^2)
#                 average=O(n^2)
#Space complexity: worst=O(1)