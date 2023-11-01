my_list = [3, 6, 8, 10, 1, 2, 1]

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[len(lst) // 2]

    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort(my_list))
