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


passing_score = {student:score for (student, score) in student_scores.items() if score >= 60 }

# print(passing_score)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {
  "Monday": 12, "Tuesday": 14, "Wednesday": 15,
  "Thursday": 14, "Friday": 21, "Saturday": 22,
  "Sunday": 24
}

weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}

print(weather_f)