student_data = {'id1':
                {'name': 'Tommy',
                 'age': 11,
                 'class': 'V',
                 'subjects': ['Math', 'Science', 'English']},
                'id2':
                {'name': 'Timmy',
                 'age': 12,
                 'class': 'V',
                 'subjects': ['Math', 'Science', 'English']},
                'id3':
                {'name': 'Jimmy',
                 'age': 11,
                 'class': 'V',
                 'subjects': ['Math', 'Science', 'English']},
                'id4':
                {'name': 'Kimmy',
                 'age': 12,
                 'class': 'V',
                 'subjects': ['Math', 'Science', 'English']},
}

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)