marks = {
    'English': 19,
    'Web Tech': 22,
    'AIML': 26,
    'Physics': 26,
    'Maths': 29,
    'Python': None  
}
s = 0

# Logic Section
for key, value in marks.items():
    if type(value) == int:
        s += value
print("Total marks are:", s)

values = marks.values()
max_marksValue = max(values)
min_marksValue = min(values)

subject_maxMarks = []
subject_minMarks = []

for key, value in marks.items():
    if max_marksValue == value:
        subject_maxMarks.append(key)
    if min_marksValue == value:
        subject_minMarks.append(key)

print('Maximum', subject_maxMarks, max_marksValue)
print('Minimum', subject_minMarks, min_marksValue)
