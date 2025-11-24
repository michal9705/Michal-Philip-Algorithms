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