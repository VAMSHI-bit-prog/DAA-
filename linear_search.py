import time

# Linear Search Function
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# User Input
n = int(input("Enter number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

# Start Timer
start = time.perf_counter()

result = linear_search(arr, key)

# End Timer
end = time.perf_counter()

# Output
if result != -1:
    print(f"\nElement found at index {result}")
else:
    print("\nElement not found")

print(f"Execution Time: {end - start:.10f} seconds")

# Complexity
print("\nTime Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")

print("\nSpace Complexity:")
print("O(1)")