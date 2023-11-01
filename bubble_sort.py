# list = [2,132,2,654,43,66,32]

# def buble_sort(lst):
#     n = len(lst)

#     for i in range(n):
#         for j in range(n - i - 1):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     print(lst)

# buble_sort(list)


my_list = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(lst):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                swapped = True
    return lst

print(bubble_sort(my_list))