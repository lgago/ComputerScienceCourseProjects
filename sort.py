'''Project 2 CS2420 Summer Block 1 2020. Completed by Luis Gago with no help from other students.'''
import random
import array
from time import perf_counter
from recursioncounter import RecursionCounter


def quicksort(lyst):
    '''The initial quicksort function that helps obfuscate the actual processes behind this sort'''
    if type(lyst) != list:
        raise ValueError("list passed into quicksort must be of type list")
    quicksort_helper(0, len(lyst) - 1, lyst)
    return lyst

def quicksort_helper(low, high, lyst):
    '''This function helps with the recursion needed for the Quicksort'''
    RecursionCounter() #needed for unittesting
    if low < high:
        pivot_location = partition(low, high, lyst)
        quicksort_helper(low, pivot_location - 1, lyst)
        quicksort_helper(pivot_location + 1, high, lyst)

def partition(low, high, lyst):
    '''Partition items in the list so that all items less than the pivot are moved to the left of the pivot'''
    #Find the pivot and exchange it with the last item
    middle = (low + high) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[high]
    lyst[high] = pivot
    # Set boundary point to first position
    boundary = low
    #Move items less than pivot to the left
    for index in range(low, high):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    #Exchange the pivot item and the boundary item
    swap(lyst, high, boundary)
    return boundary

def swap(lyst, item_i, item_j):
    '''Exchanges item i and item j'''
    lyst[item_i], lyst[item_j] = lyst[item_j], lyst[item_i]

def mergesort(lyst):
    '''main function for the mergesort'''
    if type(lyst) != list:
        raise ValueError("list passed into mergesort must be of type list")
    #lyst list being sorted
    # copyBuffer temporary space needed during merge
    copy_buffer = array.array("i", range(0, len(lyst)))
    mergesort_helper(lyst, copy_buffer, 0, len(lyst) - 1)
    return lyst

def mergesort_helper(lyst, copy_buffer, low, high):
    '''helper function for mergesort'''
    #lyst list being sorted
    #copybuffer temp space needed during merge
    #low, high bounds of sublist
    # middle, midpoint of sublist
    RecursionCounter() #needed for unittesting
    if low < high:
        middle = (low + high) // 2
        mergesort_helper(lyst, copy_buffer, low, middle)
        mergesort_helper(lyst, copy_buffer, middle + 1, high)
        merge(lyst, copy_buffer, low, middle, high)

def merge(lyst, copy_buffer, low, middle, high):
    '''helper function for mergesort_helper'''
    #lyst list that is being sorted
    #copybuffer temp space needed during the merge process
    #low beginning of first sorted sublist
    #middle end of first sorted sublist
    # middle + 1 beginning of second sorted sublist
    # high end of second sorted sublist
    # initialize i1 and i2 to the first items in each sublist
    i_1 = low
    i_2 = middle + 1
    #interleave items from the sublists into the copybuffer in such a way that order is maintined
    for i in range(low, high + 1):
        if i_1 > middle:
            copy_buffer[i] = lyst[i_2]
        elif i_2 > high:
            copy_buffer[i] = lyst[i_1]
        elif lyst[i_1] < lyst[i_2]:
            copy_buffer[i] = lyst[i_1]
        else:
            copy_buffer[i] = lyst[i_2]
            i_2 += 1
    for i in range(low, high + 1):
        lyst[i] = copy_buffer[i]

def selection_sort(lyst):
    '''selection sort function'''
    if type(lyst) != list:
        raise ValueError("list passed into selection_sort must be of type list")
    item_i = 0
    while item_i < len(lyst) - 1:
        minIndex = item_i
        item_j = item_i + 1
        while item_j < len(lyst):
            if lyst[item_j] < lyst[minIndex]:
                minIndex = item_j
            item_j += 1
        if minIndex != item_i:
            swap(lyst, minIndex, item_i)
        item_i += 1
    return lyst


def insertion_sort(lyst):
    '''insertion sort function'''
    if type(lyst) != list:
        raise ValueError("list passed into insertion_sort must be of type list")
    item_i = 1
    while item_i < len(lyst):
        item_to_insert = lyst[item_i]
        item_j = item_i - 1
        while item_j >= 0:
            if item_to_insert < lyst[item_j]:
                lyst[item_j + 1] = lyst[item_j]
                item_j -= 1
            else:
                break
        lyst[item_j + 1] = item_to_insert
        item_i += 1
    return lyst

def is_sorted(lyst):
    '''checks if a list is sorted, if it is a list, and if it is only ints'''
    if type(lyst) != list:
        raise ValueError("list passed into is_sorted must be of type list")
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("list passed to linear search algorithm must only contain integers")
    # using naive method to
    # check sorted list
    i = 1
    while i < len(lyst):
        if(lyst[i] < lyst[i - 1]):
            return False
        i += 1
    return True

def main():
    '''This main function is used to run all of the algorithms and display the sort time results'''
    data_size = 1000
    random.seed(0)
    data = random.sample(range(data_size * 3), k=data_size)
    data_size_sorted = 1000
    random.seed(1)
    data_sorted = random.sample(range(data_size_sorted * 3), k=data_size_sorted)
    test = data_sorted.copy()
    is_sorted(test)
    test = sorted(test)
    is_sorted(test)

########################### Search for the first element.
    selection_lyst = data.copy()
    print("starting selection sort")
    start_selection = perf_counter()
    selection_sort(selection_lyst)
    end_selection = perf_counter()
    elapsed_selection = end_selection - start_selection
    print("selection_sort duration:", elapsed_selection, "seconds")

    insertion_lyst = data.copy()
    print("starting insertion sort")
    start_insertion = perf_counter()
    insertion_sort(insertion_lyst)
    end_insertion = perf_counter()
    elapsed_insertion = end_insertion - start_insertion
    print("insertion_sort duration:", elapsed_insertion, "seconds")

    merge_lyst = data.copy()
    print("starting mergesort")
    start_merge = perf_counter()
    mergesort(merge_lyst)
    end_merge = perf_counter()
    elapsed_merge = end_merge - start_merge
    print("mergesort duration:", elapsed_merge, "seconds")

    quick_lyst = data.copy()
    print("starting quicksort")
    start_quick = perf_counter()
    quicksort(quick_lyst)
    end_quick = perf_counter()
    elapsed_quick = end_quick - start_quick
    print("quicksort duration:", elapsed_quick, "seconds")

    time_lyst = data.copy()
    print("starting timesort")
    start_time = perf_counter()
    sorted(time_lyst)
    end_time = perf_counter()
    elapsed_time = end_time - start_time
    print("timesort duration:", elapsed_time, "seconds")

if __name__ == '__main__':
    main()
