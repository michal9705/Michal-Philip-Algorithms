# א
def partition_lomuto(a, key):
    pivot_value = key(a[-1])
    i = -1
    for j in range(len(a) - 1):
        if key(a[j]) <= pivot_value:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[-1] = a[-1], a[i + 1]
    return i + 1

# ב
def partition_hoare(a, key):
    pivot_value = key(a[0])
    i = -1
    j = len(a)
    while True:
        i += 1
        while key(a[i]) < pivot_value:
            i += 1
        j -= 1
        while key(a[j]) > pivot_value:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]
a1 = [8, 3, 7, 4, 9, 2]
a2 = a1.copy()

# Lomuto
idx_lomuto = partition_lomuto(a1, key=lambda x: x)
print("Lomuto:", a1, "Pivot index:", idx_lomuto)

# Hoare
idx_hoare = partition_hoare(a2, key=lambda x: x)
print("Hoare:", a2, "Partition index:", idx_hoare)