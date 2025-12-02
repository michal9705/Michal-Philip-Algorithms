def merge_sorted_lists(lists, key):
    # מצביעים לכל רשימה
    indices = [0] * len(lists)
    result = []

    while True:
        min_value = None
        min_list_index = None

        # חיפוש הפריט הקטן הבא מתוך כל הרשימות
        for i, lst in enumerate(lists):
            idx = indices[i]

            # אם הרשימה נגמרה – מדלגים
            if idx >= len(lst):
                continue

            item = lst[idx]

            if min_value is None or key(item) < key(min_value):
                min_value = item
                min_list_index = i

        # אם לא נמצא שום פריט – סיימנו
        if min_list_index is None:
            break

        # מוסיפים את הפריט הנבחר לרשימת התוצאה
        result.append(min_value)

        # מקדמים את המצביע באותה רשימה
        indices[min_list_index] += 1

    return result
lists = [
    [1, 4, 9],
    [2, 3, 10],
    [0, 5, 6]
]

merged = merge_sorted_lists(lists, key=lambda x: x)
print(merged)
# תוצאה: [0, 1, 2, 3, 4, 5, 6, 9, 10]