class Student:

    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.grades = {}

    def print_(self):
        print("{} {}, {}".format(self.first_name, self.last_name, self.student_id))

    def __repr__(self):
        return "{} {}, id: {}, gpa: {}".format(self.first_name, self.last_name, self.student_id, self.get_gpa())

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_gpa(self):
        if len(self.grades) == 0:
            return 0
        sum_ = 0
        for g in self.grades.values():
            sum_ += g
        return sum_ / len(self.grades)

    def __lt__(self, other):
        return self.student_id < other.student_id


s1 = Student("00100", "Max", "Mustermann")
s2 = Student("00200", "Philipp", "Dainese")
s3 = Student("00300", "Jane", "Doe")
s4 = Student("00400", "John", "Doe")
s5 = Student("00500", "Bella", "Kadimyan")
s6 = Student("00600", "Mismo", "Aydan")
s7 = Student("00700", "Farin", "Urlaub")
s8 = Student("00800", "Jeff", "Bezos")
s9 = Student("00900", "Ben", "Falk")

students = [s1, s2, s3, s4, s5, s6, s7, s8, s9]