#Create students
students = []
student = {
    "id" : None,
    "name" : None,
    "DoB" : None,
    "course": None,
    "mark" : None
}

#Create courses
courses = []
course = {
    "id" : None,
    "name" : None
}

#Global variables
numCourse = 0

#Input course
def addCourse():
    numCourse = int(input("Input number of courses: "))
    for i in range(numCourse):
        course = {
            "id" : input("Input course's id: "),
            "name" : input("Input course's name: ")
        }
        courses.append(course)
    
#Input student
def addStudent():
    numStudent = int(input("Input number of students: "))
    for i in range(numStudent):
        student = {
            "id" : input("Input student's id: "),
            "name" : input("Input student's name: "),
            "DoB" : input("Input student's DoB: "),
            "course" : input("Input student's course: ").split(),
            "mark" : input("Input student's mark: ").split()
        }
        students.append(student)
        
#List courses
def listCourse():
    print("There are %s courses" %len(courses))
    for i in courses:
        print("Course info: ", i)

#List students
def listStudent():
    print("There are %s students" %len(students))
    for i in students:
        print("Student info: ", i)

#Driver
if(__name__== "__main__"):
    addCourse()
    addStudent()
    listCourse()
    listStudent()