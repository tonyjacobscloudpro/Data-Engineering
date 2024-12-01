# Code snippets have comments describing how each algorithm works, its time/space complexity, and when to use it. 

# sorting_algorithms.py

# 1. Bubble Sort
# - How it works: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# - Time Complexity: Best: O(n), Average/Worst: O(n^2)
# - Space Complexity: O(1) (in-place)
# - When to use: Rarely used in real applications due to inefficiency. Good for small datasets or teaching purposes.
print("1. Bubble Sort")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted:", unsorted_list)
print("Sorted:", bubble_sort(unsorted_list))

# 2. Selection Sort
# - How it works: Repeatedly selects the smallest element from the unsorted section and moves it to the sorted section.
# - Time Complexity: Best/Average/Worst: O(n^2)
# - Space Complexity: O(1) (in-place)
# - When to use: Suitable for small datasets. Minimizes swaps, making it memory-efficient in constrained systems.
print("\n2. Selection Sort")
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

unsorted_list = [64, 25, 12, 22, 11]
print("Unsorted:", unsorted_list)
print("Sorted:", selection_sort(unsorted_list))

# 3. Insertion Sort
# - How it works: Builds the sorted array one element at a time by inserting elements into their correct position.
# - Time Complexity: Best: O(n), Average/Worst: O(n^2)
# - Space Complexity: O(1) (in-place)
# - When to use: Efficient for small or nearly sorted datasets. Useful for incremental sorting as new data arrives.
print("\n3. Insertion Sort")
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

unsorted_list = [12, 11, 13, 5, 6]
print("Unsorted:", unsorted_list)
print("Sorted:", insertion_sort(unsorted_list))

# 4. Merge Sort
# - How it works: Divide-and-conquer algorithm. Splits the list into halves, sorts each half, and merges them.
# - Time Complexity: Best/Average/Worst: O(n log n)
# - Space Complexity: O(n) (requires auxiliary space for merging)
# - When to use: Suitable for large datasets and scenarios requiring stable sorting.
print("\n4. Merge Sort")
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

unsorted_list = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted:", unsorted_list)
print("Sorted:", merge_sort(unsorted_list))

# 5. Quick Sort
# - How it works: Uses a "pivot" element to partition the array into smaller and larger elements, then sorts recursively.
# - Time Complexity: Best/Average: O(n log n), Worst: O(n^2) (poor pivot selection)
# - Space Complexity: O(log n) (in-place recursion)
# - When to use: General-purpose sorting for most datasets. Not suitable when stability is required.
print("\n5. Quick Sort")
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

unsorted_list = [10, 7, 8, 9, 1, 5]
print("Unsorted:", unsorted_list)
print("Sorted:", quick_sort(unsorted_list))

# 6. Heap Sort
# - How it works: Builds a binary heap from the input data, then extracts elements in sorted order.
# - Time Complexity: Best/Average/Worst: O(n log n)
# - Space Complexity: O(1) (in-place)
# - When to use: Efficient in memory-constrained environments with deterministic performance.
print("\n6. Heap Sort")
def heap_sort(arr):
    import heapq
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

unsorted_list = [4, 10, 3, 5, 1]
print("Unsorted:", unsorted_list)
print("Sorted:", heap_sort(unsorted_list))

# 7. Counting Sort
# - How it works: Counts occurrences of each value and uses the counts to place elements in order.
# - Time Complexity: Best/Average/Worst: O(n + k), where k is the range of input values.
# - Space Complexity: O(k) (requires auxiliary array)
# - When to use: Suitable for integers or categorical data with a small range.
print("\n7. Counting Sort")
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i, val in enumerate(count):
        sorted_arr.extend([i] * val)
    return sorted_arr

unsorted_list = [4, 2, 2, 8, 3, 3, 1]
print("Unsorted:", unsorted_list)
print("Sorted:", counting_sort(unsorted_list))

# 8. Radix Sort
# - How it works: Processes digits of numbers starting from the least to the most significant using counting sort.
# - Time Complexity: Best/Average/Worst: O(nk), where k is the number of digits.
# - Space Complexity: O(n + k)
# - When to use: Efficient for sorting large datasets of integers with a fixed number of digits.
print("\n8. Radix Sort")
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

unsorted_list = [170, 45, 75, 90, 802, 24, 2, 66]
print("Unsorted:", unsorted_list)
print("Sorted:", radix_sort(unsorted_list))

# End of Examples
print("\nAll sorting algorithm examples executed successfully!")
