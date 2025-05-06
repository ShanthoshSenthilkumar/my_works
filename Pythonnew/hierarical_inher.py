class school:
    def staff(self):
        print("Teachers and their subjects")

class teacher_1():
    def tamil(self):
        print("Tamil teacher teaches Tamil")

class teacher_2(school,teacher_1):
    def english(self):
        print("English teacher teaches english")

class teacher_3(teacher_2):
    def maths(self):
        print("Maths teacher teaches Maths")

class teacher_4(teacher_3):
    def science(self):
        print("Science teacher teaches Science")

obj=teacher_4()
obj.staff()
obj.tamil()
obj.english()
obj.maths()
obj.science()


