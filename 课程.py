class Course:
    def __init__(self, courseName):
        self.__courseName = courseName
        self.__students = []

    def addStudent(self, student):
        self.__students.append(student)

    def getStudent(self):
        return self.__students

    def getNumberOfStudent(self):
        return len(self.__students)

    def getCourseName(self):
        return self.__courseName

    def dropStudent(self):
        print("Left as an exercise")
