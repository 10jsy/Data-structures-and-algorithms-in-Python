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

test_list = [11,5,7,23,4,2,6,4,63,7,4,44]
print(sequential_search(test_list, 11))