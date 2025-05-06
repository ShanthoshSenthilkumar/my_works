class index:
    name="Shanthosh"
    def __init__(self):
        self.tamil=int(input("Enter the tamil marks:"))
        self.english=int(input("Enter the english marks:"))
        self.maths=int(input("Enter the maths mark:"))
        self.science=int(input("Enter the science marks:"))
        self.social=int(input("Enter the social marks:"))
        # self.total=0
       
    def get_total(self):
       total= self.tamil + self.english + self.maths + self.science + self.social
       return total

    def get_percentage(self):
        total=self.get_total()
        return total/5
    

    def get_grade(self):
        percentage=self.get_percentage()

        if(percentage>=90):
            return "A+"
        elif(percentage>=80):
            return "A"
        elif(percentage>=70):
            return "B+"
        elif(percentage>=60):
            return "B"
        elif(percentage>=50):
            return "C"
        elif(percentage>=40):
            return "E"
        else:
            return "F"
            


student=index()
print(student.get_total())
print(student.get_percentage())
print(student.get_grade())



        




