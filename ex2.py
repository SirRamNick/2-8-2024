

student_data = {
    "Alice": {
        "age": 17,
        "grade": 12,
        "subjects": {
            "Math": 85,
            "Science": 90,
            "English": 92
        }
    },
    "Bob": {
        "age": 16,
        "grade": 11,
        "subjects": {
            "Math": 78,
            "Science": 80,
            "English": 85
        }
    },
    "Charlie": {
        "age": 18,
        "grade": 12,
        "subjects": {
            "Math": 92,
            "Science": 88,
            "English": 95
        }
    }
}

# Accessing elements from the dictionary
print("Alice's age:", student_data["Alice"]["age"])  # Output: 17
print("Alice's grade in Math:", student_data["Alice"]["subjects"]['Math'])  # Output: 85
print("Bob's English grade:", student_data["Bob"]["subjects"]["English"])  # Output: 85

# Adding a new student with their data
student_data["David"] = {
    "age": 16,
    "grade": 11,
    "subjects": {
        "Math": 80,
        "Science": 75,
        "English": 88
    }
}

# Updating data for a student
student_data["Bob"]["age"] = 17
student_data["Bob"]["subjects"]["Math"] = 80

# Iterating over the dictionary
for name, data in student_data.items():
    print(f"{name}: Age: {data['age']}, Grade: {data['grade']}")
    print("Subjects and Grades:")
    for subject, grade in data["subjects"].items():
        print(f"- {subject}: {grade}")
