
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]  # Choose the last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot
    
    # Recursively sort sub-arrays
    return quickSort(left) + [pivot] + quickSort(right)

# Test the Quick Sort algorithm
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
sorted_arr = quickSort(arr)
print("Sorted array:", sorted_arr)
