def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid Score'

def get_student_data():
    try:
        name = input("Enter student name: ")
        num_subjects = int(input("Enter the number of subjects: "))
        subjects = {}

        for _ in range(num_subjects):
            subject_name = input("Enter subject name: ")
            subject_score = float(input(f"Enter {subject_name} score: "))
            subjects[subject_name] = subject_score

        return name, subjects
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return None, None

def calculate_average_grade(subjects):
    total_score = sum(subjects.values())
    average_score = total_score / len(subjects)
    return calculate_grade(average_score)

def display_results(name, subjects, average_grade):
    print("\nStudent Report:")
    print(f"Name: {name}")
    
    print("\nSubject-wise Grades:")
    for subject, score in subjects.items():
        print(f"{subject}: {calculate_grade(score)}")

    print("\nAverage Grade: ", average_grade)

def main():
    name, subjects = get_student_data()

    if name and subjects:
        average_grade = calculate_average_grade(subjects)
        display_results(name, subjects, average_grade)

if __name__ == "__main__":
    main()
