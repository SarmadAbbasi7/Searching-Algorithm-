# Linear Search Implementation
def linear_search(arr, target):
  
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search Implementation
def binary_search(arr, target):
  
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # Check if target is at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    return -1


# Main Function
if __name__ == "__main__":
    # Example Array (sorted for Binary Search)
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]

    print("Array:", numbers)
    target = int(input("Enter the number to search: "))

    # Linear Search
    linear_result = linear_search(numbers, target)
    if linear_result != -1:
        print(f"Linear Search: Element found at index {linear_result}")
    else:
        print("Linear Search: Element not found.")

    # Binary Search
    binary_result = binary_search(numbers, target)
    if binary_result != -1:
        print(f"Binary Search: Element found at index {binary_result}")
    else:
        print("Binary Search: Element not found.")
