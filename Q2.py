# סעיף ב' — פונקציה שבודקת סידור
def is_sorted(a, key):
    for x, y in zip(a, a[1:]):
        if key(x) > key(y):
            return False
    return True


# סעיף א' + עדכון לסעיף ב' — merge שבודק שהרשימות ממוינות
def merge(a, b, key):
    # בדיקה שהרשימות אכן ממוינות
    if not is_sorted(a, key) or not is_sorted(b, key):
        return None

    i, j = 0, 0
    result = []

    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result

if __name__ == "__main__":
    a = [(1, "a"), (5, "b"), (10, "c")]
    b = [(2, "x"), (6, "y"), (9, "z")]

    print(merge(a, b, key=lambda x: x[0]))

    bad = [(3, "x"), (1, "y"), (2, "z")]
    print(merge(bad, b, key=lambda x: x[0]))