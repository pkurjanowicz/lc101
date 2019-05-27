def swap(x,y):
    x, y = y, x
    return x,y

def bubble_sort(alist):
    is_sorted = False
    while is_sorted is False:
        num_swaps = 0 
        for item in alist:
            if item > item + 1:
                item_a = item
                item_b = item +1
                swapped_values = swap(item_a,item_b)
                num_swaps = num_swaps + 1
    if num_swaps == 0:
        is_sorted == True

print(bubble_sort([3, 1]))   

#from test import testEqual
#testEqual(bubble_sort([0]), [0])  # Sorts a single element, returns same list
#testEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Sorted list is the same
#testEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
#testEqual(bubble_sort([4, 5, 3, 1, 2]), [1, 2, 3, 4, 5])
