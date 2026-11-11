arr = [7,7,2,3,7,1,2,3,7,8,9,4,3]
n= len(arr)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    if not swapped:
        break
print("Sorted array:", arr)

