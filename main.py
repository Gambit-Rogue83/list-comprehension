# numbers = [1, 2, 3, 4, 5]
# new_numbers = [num + 1 for num in numbers]
# print(new_numbers)

# string = "Shak"
# new_string = [letter for letter in string]
# print(new_string)

# double_list = [num * 2 for num in range(1, 5)]
# print(double_list)

import random

names = ["Alex", "Beth", "Dave", "Elizabeth", "Frank", "Jeff", "Kenneth", "Liam"]

# short_names = [name for name in names if len(name) == 4]

# cap_names = [name.upper() for name in names if len(name) > 4]

# print(cap_names)

student_scores = {student:random.randint(45, 100) for student in names}

print(student_scores)