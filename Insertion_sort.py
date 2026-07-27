import time

# User Input
n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print("\nOriginal Array:", arr)

# Start Timer
start_time = time.perf_counter()

# Insertion Sort
for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

# End Timer
end_time = time.perf_counter()

# Execution Time
execution_time = end_time - start_time

# Output
print("\nSorted Array:", arr)
print(f"Execution Time: {execution_time:.10f} seconds")

# Complexity
print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")

print("\nSpace Complexity:")
print("O(1)")
