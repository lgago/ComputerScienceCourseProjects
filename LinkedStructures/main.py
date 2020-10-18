'''Created by Luis Gago collaborated with Ryan Balog. CS2420 Summer Block1.'''
from course import Course
from courselist import CourseList

def main():
    '''main function'''
    course_list = CourseList()
    file_import = open("data.txt", "r")
    for item in file_import:
        lyst = item.split(",")
        course_no = int(lyst[0])
        course_name = lyst[1]
        course_credit_hours = float(lyst[2])
        course_grade = float(lyst[3].strip())
        course_list.insert(Course(course_no, course_name, course_credit_hours, course_grade))
    print("Current List: (" + str(course_list.size()) + ")")
    print(course_list)
    print("Cumulative GPA: " + str(round(course_list.calculate_gpa(), 3)))

if __name__ == "__main__":
    main()
