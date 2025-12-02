def dual_pivot_partition(arr, low, high):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    pivot1 = arr[low]
    pivot2 = arr[high]

    i = low + 1
    lt = low + 1
    gt = high - 1

    while i <= gt:
        if arr[i] < pivot1:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot2:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    # העברת ה-pivot למקום הנכון
    arr[low], arr[lt - 1] = arr[lt - 1], arr[low]
    arr[high], arr[gt + 1] = arr[gt + 1], arr[high]

    return lt - 1, gt + 1  # מחזירים את המיקומים של שני ה-pivot