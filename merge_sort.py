my_list = [38, 27, 3, 43, 3, 3, 3, 9, 82, 10]


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    middle = len(lst)//2
    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_list(left, right)


def merge_two_list(left, right):
    
    result = []
    
    i = 0
    j = 0

    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if len(left) > i:
        result += left[i:]
    elif len(right) > j:
        result += right[j:]
    
    return result


print(merge_sort(my_list))

