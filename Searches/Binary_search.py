#Using ordered list of items, by starting the search at halfway, can discard greater/smaller set of values if item not found using pivot.
#Keep track of first and last points of the list to find mid point of list
def binary_search(ordered_list, item):
    first = 0
    last = len(ordered_list) - 1
    found = False

    while first <= last and not found:
        mid = (first+last)//2
        if ordered_list[mid] == item:
            return True
        else:
            if ordered_list[mid] < item:
                first = mid + 1
            else:
                last = mid - 1
    return found

test_list = [1,2,3,4,5,6,7,8,9,10,15,16,17,18]
print(binary_search(test_list, 12))