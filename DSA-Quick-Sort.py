# A function to perform partition operation and return pivot index
def partition(arry, low, high):
    # Choosing the last element as pivot
    pivot = arry[high]  # pivot
    
    # Initialize i (index of smaller element)
    i = low - 1 

 # Traverse through all elements
    for j in range(low, high):
        # If current element is smaller or equal to pivot
        if arry[j] <= pivot:
            # Increment i, and swap current element with element at i
            i += 1
            arry[i], arry[j] = arry[j], arry[i] 

    # Swap the pivot element with the element at index i+1
    arry[i + 1], arry[high] = arry[high], arry[i + 1]

    # Return the pivot index
    return i + 1


# A recursive function to implement Quick Sort
def quick_sort(arr, low=0, high=None):
    # If high is not provided, assume it is the last index
    if high is None:
        high = len(arr) - 1

    # If low is less than high, then there is a sub-array to be sorted
    if low < high:
        # Partition the array around a pivot
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after the pivot
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

# Testing the code
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quick_sort(my_array)
print("Sorted array is:", my_array)
#   Sorted array is: [5, 11, 12, 22, 25, 34, 64, 90]



