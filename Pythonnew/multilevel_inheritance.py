class showroom:
    def employees(self):
        print("Employee Id")

class sales_dept(showroom):
    def tl(self):
        print("Meet Customers")

class service_dept(sales_dept):
    def service_manager(self):
        print("Rectify customer issues on time")
        
class delivery(service_dept):
    def manager(self):
        print("Delivery on time")

obj=delivery()
obj.employees()
obj.tl()
obj.service_manager()
obj.manager()