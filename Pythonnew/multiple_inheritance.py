class parent_calss_1:
    def car(self):
        print("Car Starrted")
class parent_class_2:
    def bmw(self):
        print("Performance Based")

class index(parent_calss_1,parent_class_2):
    def bike(self):
        print("Bike Started")

obj=index()
obj.car()
obj.bmw()
obj.bike()