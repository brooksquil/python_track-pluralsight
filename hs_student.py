# HighschoolStudnet is the derived class
class HighSchoolStudent(Student):
    school_name = "Amity High"

    def get_school_name(self):
        return "This is a student"

#     using Super
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"
