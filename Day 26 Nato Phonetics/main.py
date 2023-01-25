# student_scores = {'Alex': 81, 'Beth': 88, 'Caroline': 35, 'Dave': 74, 'Eleanor': 8, 'Freddie': 60}
# for scores in student_scores:
#     print(student_scores[scores])
#
# # passed_student = {student:student_scores[student] for student in student_scores if student_scores[student] > 60}
#
# passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_student)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

for data in weather_c:
    print(weather_c[data])


# Write your code 👇 below:

weather_f = {weather: (temp * 9/5 + 32) for (weather, temp) in weather_c.items()}

print(weather_f)
