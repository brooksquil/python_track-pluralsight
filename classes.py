students = []

class Student:
    # self refers to an instance of the class
    # refers to the class within the class
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student" + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

# HighschoolStudnet is the derived class
class HighSchoolStudent(Student):
    school_name = "Amity High"

    def get_school_name(self):
        return "This is a student"

#     using Super
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"




