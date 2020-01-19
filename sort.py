
testArray = [21,345,46,72,1235,45,3,24,7]

def merge(array1,array2):
    tempArray = []
    i = j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            tempArray.append(array1[i])
            i += 1
        else:
            tempArray.append(array2[j])
            j += 1
    if i == len(array1):
        for item in array2[j:]:
            tempArray.append(item)
    else:
        for item in array1[i:]:
            tempArray.append(item)
    return tempArray

def mergerSort(list):
    if len(list) <= 1:
        return list
    middle = len(list) // 2
    left = mergerSort(list[ : middle])
    right = mergerSort(list[middle : ])
    return merge(left,right)

def partition(array, left, right):
    pivotKey = array[left]
    while left < right:
        while left < right and pivotKey <= array[right]:
            right -= 1
        array[left] = array[right]
        while left < right and pivotKey >= array[left]:
            left += 1
        array[right] = array[left]
    array[left] = pivotKey
    return left

def quickSort(array, left, right):
    if left < right:
        pivot = partition(array,left,right)
        quickSort(array, left, pivot - 1)
        quickSort(array, pivot + 1, right)
    return array

print(quickSort(testArray,0,len(testArray) - 1))