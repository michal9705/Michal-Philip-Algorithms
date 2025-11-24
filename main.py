import random
import string


# ===============================================
# סעיף א: פונקציה למציאת מינימום ומקסימום
# ===============================================

def min_max_find(a, key=None):
    """
    מוצאת את האיבר המינימלי והמקסימלי ברשימה a.

    :param a: הרשימה/מערך של ערכים.
    :param key: פונקציה (key function) המופעלת על כל איבר לפני ההשוואה.
                אם key הוא None, האיברים מושווים ישירות.
    :return: Tuple המכיל את (האיבר המינימלי, האיבר המקסימלי).
    """
    if not a:
        # מחזירה None אם הרשימה ריקה
        return None, None

        # אם key הוא None, מגדירים אותו כפונקציית זהות (lambda x: x)
    if key is None:
        key = lambda x: x

    # אתחול עם האיבר הראשון
    min_item = a[0]
    max_item = a[0]

    min_key_val = key(a[0])
    max_key_val = key(a[0])

    # מעבר על שאר האיברים (O(n) זמן ריצה)
    for item in a[1:]:
        current_key_val = key(item)

        # בדיקת מינימום
        if current_key_val < min_key_val:
            min_key_val = current_key_val
            min_item = item

        # בדיקת מקסימום
        if current_key_val > max_key_val:
            max_key_val = current_key_val
            max_item = item

    return min_item, max_item


# ===============================================
# פונקציית min_find נפרדת (כנדרש בחתימה בשאלה)
# ===============================================
def min_find(a, key=None):
    """מוצאת את האיבר המינימלי ברשימה a."""
    if not a:
        return None

    if key is None:
        key = lambda x: x

    min_item = a[0]
    min_key_val = key(a[0])

    for item in a[1:]:
        current_key_val = key(item)

        if current_key_val < min_key_val:
            min_key_val = current_key_val
            min_item = item

    return min_item


# ===============================================
# סעיף ב: יצירת מערך, הפעלה והדפסה
# ===============================================

# פונקציות עזר ליצירת נתונים
def generate_random_string(length=5):
    """יוצר מחרוזת אקראית באורך נתון."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_float():
    """יוצר מספר ממשי אקראי."""
    return random.uniform(1.0, 1000.0)


def generate_random_int():
    """יוצר מספר שלם אקראי."""
    return random.randint(1, 10000)


def run_exercise_b():
    # 1. יצירת רשימה של 100 tuples
    NUM_ELEMENTS = 100
    data_array = []

    # O(n) זמן ריצה ליצירת המערך
    for _ in range(NUM_ELEMENTS):
        # Tuple עם טיפוסים [str, float, int]
        random_tuple = (
            generate_random_string(),
            generate_random_float(),
            generate_random_int()
        )
        data_array.append(random_tuple)

    # 2. מציאת המינימום והמקסימום לפי הפריט השלישי (אינדקס 2)
    # x[2] מתייחס לפריט השלישי ב-tuple, שהוא המספר השלם.
    key_function = lambda x: x[2]

    # O(n) זמן ריצה למציאת מינימום ומקסימום
    min_item, max_item = min_max_find(data_array, key=key_function)

    # 3. הדפסת הפלט הנדרש
    print("תוצאות סעיף ב':")
    print(f"min={min_item}")
    print(f"max={max_item}")


if __name__ == "__main__":
    # הפעלת התוכנית המייצרת את הנתונים ומדפיסה את התוצאות
    run_exercise_b()


    ##שאלה 5

    def insertion_sort(a, key=None):
        if key is None:
            key = lambda x: x

        n = len(a)

        for i in range(1, n):
            current_item = a[i]
            current_key = key(current_item)
            j = i - 1
            while j >= 0 and key(a[j]) > current_key:
                a[j + 1] = a[j]
                j -= 1

            a[j + 1] = current_item


    def generate_random_string(length=5):
        """יוצר מחרוזת אקראית באורך נתון."""
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))


    def generate_random_float():
        """יוצר מספר ממשי אקראי."""
        return random.uniform(1.0, 100.0)


    def generate_random_int():
        """יוצר מספר שלם אקראי."""
        return random.randint(1, 1000)


    def generate_random_tuple():
        """יוצר tuple אקראי: (str, float, int)."""
        return (
            generate_random_string(),
            generate_random_float(),
            generate_random_int()
        )


    if __name__ == "__main__":

        # יצירת רשימת בסיס של 10 tuples אקראיים
        base_list = [generate_random_tuple() for _ in range(10)]

        print("--- רשימת בסיס מקורית (10 tuples [str, float, int]) ---")
        for item in base_list:
            print(item)
        print("-" * 50)

        # 1. מיון לפי הפריט הראשון (מחרוזת, אינדקס 0)
        list1 = base_list[:]  # יצירת עותק
        key_func_str = lambda x: x[0]

        print("## 1. מיון לפי הפריט הראשון (מחרוזת)")
        insertion_sort(list1, key=key_func_str)
        for item in list1:
            print(item)
        print("-" * 50)

        # 2. מיון לפי הפריט השני (Float, אינדקס 1)
        list2 = base_list[:]  # יצירת עותק
        key_func_float = lambda x: x[1]

        print("## 2. מיון לפי הפריט השני (float)")
        insertion_sort(list2, key=key_func_float)
        for item in list2:
            print(item)
        print("-" * 50)

        # 3. מיון לפי הפריט השלישי (Integer, אינדקס 2)
        list3 = base_list[:]  # יצירת עותק
        key_func_int = lambda x: x[2]

        print("## 3. מיון לפי הפריט השלישי (integer)")
        insertion_sort(list3, key=key_func_int)
        for item in list3:
            print(item)
        print("-" * 50)