def bubble_sort(alist):
    for num in range(len(alist)-1, 0, -1):
        for i in range(num):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i] 

sort_list = [5,8,1,3,4,88,11,3,15,666,7,18,81,444]
bubble_sort(sort_list)
print(sort_list)

#Time complexity: best = O(n)
#                 average = O(n^2)
#                 worst = O(n^2)
#Space complexity: worst = O(1)