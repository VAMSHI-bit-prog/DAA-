import time

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# ---------------- Main Program ----------------

# User Input
n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print("\nOriginal Array:", arr)

# Start Timer
start_time = time.perf_counter()

# Perform Merge Sort
merge_sort(arr)

# End Timer
end_time = time.perf_counter()

# Execution Time
execution_time = end_time - start_time

# Output
print("\nSorted Array:", arr)
print(f"Execution Time: {execution_time:.10f} seconds")

# Complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")

print("\nSpace Complexity:")
print("O(n)")
