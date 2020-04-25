#Goes through each element in a list and returns boolean True/False if item is found in list.
#Keep note of position and True/False

def sequential_search(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            return True
        else:
            pos += 1
    return found

def ordered_sequential_search(orderedlist, item):
    pos = 0
    found = False

    while pos < len(orderedlist) and not found:
        if orderedlist[pos] == item:
            return True
        elif orderedlist[pos] > item:
            return False
        else:
            pos += 1
    return found

test_list = [11,5,7,23,4,2,6,4,63,7,4,44]
test_ordered_list = [1,2,3,4,5,6,7,9,10,11,12]
print(sequential_search(test_list, 11))
print(ordered_sequential_search(test_ordered_list, 8))