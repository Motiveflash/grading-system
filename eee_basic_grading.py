#This program is a grading system for EEE department. 
#It takes a list of courses and student names and their scores, and the assign grades based on their scores

#This function assign grades based on the scores
def assign_grade(scores):
    if 80 <= scores <= 100:
        return 'A'
    elif 70 <= scores < 80:
        return 'B'
    elif 60 <= scores < 70:
        return 'C'
    elif 50 <= scores < 60:
        return 'D'
    else:
        return 'F'
  
def input_course_data():
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_name = input("Enter course name: ")
        students = []
        num_students = int(input(f"Enter the number of students for {course_name} "))
        for _ in range(num_students):
            student_name = input("Enter the student name: ")
            student_score = int(input("Enter the student score "))
            student_grade = assign_grade(student_score)
            students.append({'student_name' : student_name, 'student_score' : student_score, 'student_grade' : student_grade})
        courses.append({'Course' : courses, 'Students' : students})
    return courses

def print_grading_report(courses):
    for course in courses:
        print(f"\nCourse: {course['course']}")
        print("Student Name\tScore\tGrade")
        print("-------------------------------------")
        for student in course['students']:
            print(f"{student['name']}\t\t{student['score']}\t{student['grade']}")

def main():
    courses = input_course_data() 
    print_grading_report(courses)

if __name__ == "__main__":
    main()

        