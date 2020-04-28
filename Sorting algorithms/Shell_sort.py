def shell_sort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)
        sublistcount = sublistcount // 2

def gap_insertion_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current_value = alist[i]
        position = i

        while position >= gap and alist[position-gap] > current_value:
            alist[position] = alist[position-gap]
            position = position-gap

        alist[position] = current_value

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)