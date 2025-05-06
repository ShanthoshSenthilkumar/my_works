class index:
    def __init__(self):
        self.__car="car moved"
        self.__car_off="car not moved"

    def car_1(self):
        self.__car="nothing moved"
        print(self.__car)

c=index()
c.car_1()


    
