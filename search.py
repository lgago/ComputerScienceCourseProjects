'''CS2420 Summer Block 1 2020. Completed by Luis Gago with no help from other students. This file has a rating of 9.28 and passed all unit tests.'''

from time import perf_counter
import math
import random
from recursioncounter import RecursionCounter


def linear_search(lyst, target):
    '''A Sequential/Linear Search Algorithm'''
    if not isinstance(target, int):
        raise ValueError("target must be an integer")
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("list passed to linear search algorithm must only contain integers")

    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return True
        position += 1
    return False

def binary_search_helper(lyst, target, low, high):
    '''aids in the obfuscation of the binary_search function by performing calculation of mid'''
    RecursionCounter()
    if high >= low:
        mid = (low + high) // 2
        if lyst[mid] == target: 
            return True
        elif lyst[mid] > target: 
            return binary_search_helper(lyst, target, low, mid-1) 
        else:
            return binary_search_helper(lyst, target, mid+1, high)
    else:
        return False

def recursive_binary_search(lyst, target):
    '''Here calculate the low and high values and pass them into binary_search_helper. BSH is where the recursion occurs.'''
    if not isinstance(target, int):
        raise ValueError("target must be an integer")
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("list passed to binary search algorithm must only contain integers")

    low = 0
    high = len(lyst) - 1
    return binary_search_helper(lyst, target, low, high)

def jump_search(lyst, target):
    '''This function uses jump search to find the target value in a lyst'''
    if not isinstance(target, int):
        raise ValueError("target must be an integer")
    if not all(isinstance(x, int) for x in lyst):
        raise ValueError("list passed to binary search algorithm must only contain integers")

    low = 0
    interval = int(math.sqrt(len(lyst)))
    for i in range(0, len(lyst), interval):
        if lyst[i] < target:
            low = i
        elif lyst[i] == target:
            return True
        else:
            break # bigger number is found
    c_var = low
    for j in lyst[low:]:
        if j == target:
            return True
        c_var += 1
    return False


def main():
    '''This main function is used to run all of the algorithms and display the search time results'''
    ### sorted(random.sample(range(10000000), 5000000))
    random.seed(100)
    lyst = sorted(random.sample(range(10000000), 5000000))
    first_element = lyst[0]
    middle_element = lyst[2499999]
    last_element = lyst[4999999]
    none_element = -1

########################### Search for the first element.
    print("Searching for a number at the start of the array.")

    start_linear = perf_counter()
    linear_response = linear_search(lyst, first_element)
    end_linear = perf_counter()
    elapsed_linear = end_linear - start_linear
    print("Linear search returned", linear_response, "in", elapsed_linear, "seconds")

    start_binary = perf_counter()
    binary_response = recursive_binary_search(lyst, first_element)
    end_binary = perf_counter()
    elapsed_binary = end_binary - start_binary
    print("Binary search returned", binary_response, "in", elapsed_binary, "seconds")

    start_jump = perf_counter()
    jump_response = jump_search(lyst, first_element)
    end_jump = perf_counter()
    elapsed_jump = end_jump - start_jump
    print("Jump search returned", jump_response, "in", elapsed_jump, "seconds\n")


    ################### Search for the middle element.
    print("Searching for a number in the middle of the array.")

    start_linear = perf_counter()
    linear_response = linear_search(lyst, middle_element)
    end_linear = perf_counter()
    elapsed_linear = end_linear - start_linear
    print("Linear search returned", linear_response, "in", elapsed_linear, "seconds")

    start_binary = perf_counter()
    binary_response = recursive_binary_search(lyst, middle_element)
    end_binary = perf_counter()
    elapsed_binary = end_binary - start_binary
    print("Binary search returned", binary_response, "in", elapsed_binary, "seconds")

    start_jump = perf_counter()
    jump_response = jump_search(lyst, middle_element)
    end_jump = perf_counter()
    elapsed_jump = end_jump - start_jump
    print("Jump search returned", jump_response, "in", elapsed_jump, "seconds\n")


    ############ Search for last element
    print("Searching for a number at the end of the array.")

    start_linear = perf_counter()
    linear_response = linear_search(lyst, last_element)
    end_linear = perf_counter()
    elapsed_linear = end_linear - start_linear
    print("Linear search returned", linear_response, "in", elapsed_linear, "seconds")

    start_binary = perf_counter()
    binary_response = recursive_binary_search(lyst, last_element)
    end_binary = perf_counter()
    elapsed_binary = end_binary - start_binary
    print("Binary search returned", binary_response, "in", elapsed_binary, "seconds")

    start_jump = perf_counter()
    jump_response = jump_search(lyst, last_element)
    end_jump = perf_counter()
    elapsed_jump = end_jump - start_jump
    print("Jump search returned", jump_response, "in", elapsed_jump, "seconds\n")

    ############ Search for an element that doesn't exist in the array 
    print("Searching for a number not in the array")

    start_linear = perf_counter()
    linear_response = linear_search(lyst, none_element)
    end_linear = perf_counter()
    elapsed_linear = end_linear - start_linear
    print("Linear search returned", linear_response, "in", elapsed_linear, "seconds")

    start_binary = perf_counter()
    binary_response = recursive_binary_search(lyst, none_element)
    end_binary = perf_counter()
    elapsed_binary = end_binary - start_binary
    print("Binary search returned", binary_response, "in", elapsed_binary, "seconds")

    start_jump = perf_counter()
    jump_response = jump_search(lyst, none_element)
    end_jump = perf_counter()
    elapsed_jump = end_jump - start_jump
    print("Jump search returned", jump_response, "in", elapsed_jump, "seconds")


if __name__ == '__main__':
    main()
