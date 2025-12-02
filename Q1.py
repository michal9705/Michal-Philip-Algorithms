from random_tuples import create_random_tuples

# יצירת רשימת טאפלים מסוגים [int, float, str]
tuples_list = create_random_tuples(10, 3, [int, float, str])

print("הרשימה המקורית:")
for t in tuples_list:
    print(t)

# מיון לפי הרכיב הראשון
sorted_by_first = sorted(tuples_list, key=lambda x: x[0])
print("\nמיון לפי הרכיב הראשון:")
for t in sorted_by_first:
    print(t)

# מיון לפי הרכיב השני
sorted_by_second = sorted(tuples_list, key=lambda x: x[1])
print("\nמיון לפי הרכיב השני:")
for t in sorted_by_second:
    print(t)

# מיון לפי הרכיב השלישי
sorted_by_third = sorted(tuples_list, key=lambda x: x[2])
print("\nמיון לפי הרכיב השלישי:")
for t in sorted_by_third:
    print(t)