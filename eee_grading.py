#This program is a grading system for EEE department

def assign_grade(score):
    #Assign a grade based on the score.
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score <= 79:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    else:
        return 'F'

def input_course_data():
    #Take inputs for courses, student names, and scores.
    courses = []
    num_courses = int(input("Enter the number of courses: "))

    for _ in range(num_courses):
        course_name = input("Enter the course name: ")
        students = []
        num_students = int(input(f"Enter the number of students for {course_name}: "))

        for _ in range(num_students):
            student_name = input("Enter the student's name: ")
            score = int(input(f"Enter the score for {student_name}: "))
            while score < 0 or score > 100 or score :  # Check if the score is out of the valid range
                print("Invalid score. Please enter a score between 0 and 100.")
                score = int(input(f"Enter the score for {student_name}: "))
        
            grade = assign_grade(score)
            students.append({'name': student_name, 'score': score, 'grade': grade})

        courses.append({'course': course_name, 'students': students})
    
    return courses

def print_grading_report(courses):
    #Print a report of courses, student names, and their grades.
    for course in courses:
        print(f"\nCourse: {course['course']}")
        print("Student Name\tScore\tGrade")
        print("------------------------------")
        for student in course['students']:
            print(f"{student['name']}\t\t{student['score']}\t{student['grade']}")

def main():
    courses = input_course_data()
    print_grading_report(courses)

if __name__ == "__main__":
    main()
