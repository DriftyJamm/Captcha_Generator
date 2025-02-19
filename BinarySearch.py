def binary(arr, target):
    left = 0
    right = len(arr)-1
    while(left <= right):
        mid = left + (right-left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            arr[mid] = arr[mid] + 1
        else:
            arr[mid] = arr[mid] - 1
            
    return -1

arr = [1,3,5,7,9,11]
target = 9

search = binary(arr, target)
print(f"Element found at index {search}" if search != -1 else "Element not found")
