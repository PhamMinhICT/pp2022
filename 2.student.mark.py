# Create courses
courses = []
course = {
    'id': None,
    'name': None
}
# Create students
students = []
student = {
    'id': None,
    'name': None,
    'DoB': None
}
# Create marks
marks = []
mark = {
    'name': None,
    'student': None,
    'mark': None
}
class Course:
    def __init__(self, n, i_d):
        self.name = n,
        self.__id = i_d,

    def get_id(self):
        return self.__id

    def set_id(self, i):
        self.__id = i

class Courses:
    def addCourse(self):
        numCourse = int(input("Enter number of courses: "))
        for i in range(numCourse):
            name = input("Enter course's name: ")
            id = input("Enter course's id: ")
            c = Course(name, id)
            c.set_id(id)
            cou = {
                'id': c.get_id(),
                'name': c.name
            }
            courses.append(cou)

    def listCourse(self):
        print("There are %s courses: " % len(courses))
        for i in courses:
            print("Course's info: ", i)

class Student:
    def __init__(self, n, i_d, dob):
        self.name = n
        self.__id = i_d
        self.DoB = dob

    def get_id(self):
        return self.__id

    def set_id(self, i):
        self.__id = i


class Students:
    def addStudent(self, numStudent):
        for i in range(numStudent):
            name = input("Enter student's name: ")
            id = input("Enter student's id: ")
            DoB = input("Enter student's DoB: ")
            s = Student(name, id, DoB)
            s.set_id(id)
            stu = {
                'id': s.get_id(),
                'name': s.name,
                'DoB': s.DoB,
            }
            students.append(stu)

    def listStudent(self):
        print("There are %s students: " % len(students))
        for i in students:
            print("Student's info: ", i)

    def addMark(self):
        id_name = input("Choose a course and enter it's name: ")
        print()
        for i in range(numStudent):
            stu_id = input("Enter student's id: ")
            mrk = input("Enter student's mark: ")
            m = {
                'name': id_name,
                'student': stu_id,
                'mark': mrk
            }
            marks.append(m)

    def listMark(self):
        for i in marks:
            print("Mark's info: ", i)


if __name__ == "__main__":
    cs = Courses()
    cs.addCourse()
    cs.listCourse()
    ss = Students()
    numStudent = int(input("Enter number of students: "))
    ss.addStudent(numStudent)
    ss.listStudent()
    ss.addMark()
    ss.listMark()

