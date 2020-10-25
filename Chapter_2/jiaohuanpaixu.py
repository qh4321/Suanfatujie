def selectSort(arr):

    lenth = len(arr)
    for i in range(lenth-1):
        for j in range(i+1, lenth):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(selectSort([4,2,5,6,7,9,1,8,3,10]))