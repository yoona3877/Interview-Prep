
def quickSort(arr):

    quickSortMain(arr, 0, len(arr)-1)
    return arr

def quickSortMain(arr, low, high):
    if low <= high:
        pivot = arr[(low+high)/2]
        partition_idx = partition(arr, low, high, pivot)
        quickSortMain(arr, low, partition_idx)
        quickSortMain(arr, partition_idx + 1, high)

def partition( arr, low, high, pivot):

    def swap(l, r):
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
    while low <= high:
        while arr[low] < pivot:
            low +=1
        while arr[high] > pivot:
            high -=1

        if low < high:
            swap(low, high)
            low+=1
            high -=1
    return low

if __name__ == "__main__":
    test_arr = [5,7,2,3,8,9,4]
    sorted_arr = quickSort(test_arr)
    print(sorted_arr)

