class index:
    def car(self):
        print("Car Started")

class index_1(index):
    def bike(self):
        print("Bike Started")

obj=index_1()
obj.car()
obj.bike()