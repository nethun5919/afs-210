
class Employee:
    def __init__(self,firstName,lastName,employeeId,hourlyPay):
        
        self.firstName = firstName
        self.lastName = lastName 
        self.employeeId = employeeId
        self.hourlyPay = hourlyPay


    def pay(self,hours):
        print(hours)

        if hours <= 40:
            return float(self.hourlyPay * hours)

        if hours > 40: 
            balance = self.hourlyPay * 40  
            extraHours = hours - 40
            overTimePay = self.hourlyPay * 1.5
            overTimeBalance = overTimePay * extraHours
            return float(balance + overTimeBalance)

employeeId = input("Please enter the Employee's ID:")
firstName = input("Please enter the Employee's First Name: ")     
lastName = input("Please enter the Employee's Last Name: ")   
hourlyPay = input("Please enter the Employee's Hourly Pay Rate:")
hoursworked = input(f"How many hours did {firstName} work this week? ")
employee = Employee (firstName, lastName, employeeId, float(hourlyPay))
print(f"{firstName} {lastName}'s paycheck amount is:", employee.pay(int(hoursworked)))

