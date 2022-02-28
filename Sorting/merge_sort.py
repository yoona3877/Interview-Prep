def mergeSort(arr):

    return mergeSortMain(arr, 0, len(arr) -1)

def mergeSortMain(arr, leftStart, rightEnd):

    if leftStart < rightEnd:
        m = (leftStart + rightEnd) /2
        leftSorted = mergeSortMain(arr, leftStart, m)
        rightSorted = mergeSortMain(arr, m+1, rightEnd)

        return merge(leftSorted, rightSorted)

def merge(leftSorted, rightSorted):
    if not leftSorted or rightSorted:
        return leftSorted or rightSorted

    temp = []

    l, r = 0,0
    while l < len(leftSorted) and r < len(rightSorted):
        if leftSorted[l] < rightSorted[r]:
            temp.append(leftSorted[l])
            l +=1
        else:
            temp.append(rightSorted[r])
            r +=1

    while l < len(leftSorted):
        temp.append(leftSorted[l])
        l +=1
    while r < len(rightSorted):
        temp.append(rightSorted[r])
        r +=1
    return temp

if __name__ == "__main__":
    test_arr = [5,3,8,7,9,4,1]
    sorted_arr = mergeSort(test_arr)
    print(sorted_arr)
