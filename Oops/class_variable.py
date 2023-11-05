#if you have a class variable that same as all instance

class office:
    da=3.2 #class variable
    def __init__(self,emp1,salary):
        self.emp1=emp1
        self.salary=salary

    def da_netpay(self):
        self.salary=int(self.salary * self.da)

employee=office('phoenix',40000)
employee.da_netpay()
net_pay=employee.salary
print(net_pay)



