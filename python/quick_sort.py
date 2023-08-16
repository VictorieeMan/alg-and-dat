"""Created: 2023-08-14
Quick Sort algorithm
*Recursive
*In-place => uses the same memory place as the original array
*Worst  O(n^2)
*Avg    O(n log(n))
"""

def listSwap(list, idx1, idx2):
    """Help function for partition func
    Swaps to elements in a given list, and two indicies of elements to swap.
    """
    try:
        (list[idx1], list[idx2]) = (list[idx2], list[idx1])
    except IndexError:
        print("Index out of range, list length: ", len(list), "given indicies: ", idx1, idx2)

def partition(arr, l, r, order):
    """Help function for quick-sort
    Quick Sorts the given array on the interval range [l,r]
    """
    # i = l         # Init iterator variable, done in for-loop arg.
    piv = arr[r]      # Setting last elem in range as pivot element
    left_p = l - 1  # end index of left partion

    if(order == 0):
        # Ascending order sorting
        for i in range(l,r):
            if arr[i] < piv:
                left_p += 1
                listSwap(arr, left_p, i)

    elif(order == 1):
        # Descending order setting
        for i in range(l,r):
            if arr[i] > piv:
                left_p += 1
                listSwap(arr, left_p, i)
    else:
        # Bad argument given
        raise Exception("Only ascending (0) and descending (1) sort is allowed, other argument given: ", order)
    
    # Put pivot between partions
    part_idx = left_p + 1
    arr = listSwap(arr, part_idx, r)

    return part_idx

def quick_sort(arr, l, r, order=0):
    """An implementation of the quick sort algorithm
    arr    array
    l      left bound index sort
    r      right bound index sort
    order  0 for ascending [0,1,2,...] and 1 for descending [2,1,0,...]

    The array arr will be sorted on the interval [l,r]
    """
    if(l<r):
        # Partition into a lower and upper bound
        part_idx = partition(arr, l, r, order)

        # Sort lower bound
        quick_sort(arr, l, part_idx - 1, order)

        # Sort upper bound
        quick_sort(arr, part_idx + 1, r, order)
        
# Test array, with unordered numbers
arr = [57,61,83,59,29,60,12,62,63,49,91,-1,-4]
# arr = [3,2,1,5,4,2]
print("unsorted:\t",arr,)

quick_sort(arr, 0, len(arr)-1, 0)
print("sorted_asc:\t",arr)

quick_sort(arr, 0, len(arr)-1, 1)
print("sorted_desc:\t",arr,"\n")