import time

# Quick Sort Function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# User Input
n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print("\nOriginal Array:", arr)

# Start Timer
start_time = time.perf_counter()

# Perform Quick Sort
sorted_arr = quick_sort(arr)

# End Timer
end_time = time.perf_counter()

# Execution Time
execution_time = end_time - start_time

# Output
print("\nSorted Array:", sorted_arr)
print(f"Execution Time: {execution_time:.10f} seconds")

# Complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n^2)")

print("\nSpace Complexity:")
print("Average Case : O(log n)")
print("Worst Case   : O(n)")
