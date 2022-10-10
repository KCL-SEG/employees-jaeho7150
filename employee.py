"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type = "", monthly_salary = 0, hours = 0, hourly_pay = 0, commision_bonus = 0, commision_contracts = 0, commision_hourly_pay = 0):
        self.name = name
        self.contract_type = contract_type
        self.monthly_salary = monthly_salary
        self.hours = hours
        self.hourly_pay = hourly_pay
        self.commision_bonus = commision_bonus
        self.commision_contracts = commision_contracts
        self.commision_hourly_pay = commision_hourly_pay


    def get_commision(self):
        if self.commision_bonus != 0:
            return self.commision_bonus

        elif self.commision_hourly_pay != 0:
            return self.commision_hourly_pay * self.commision_contracts

        else:
            return 0

    def get_salary(self):
        if self.contract_type == "hourly":
            return self.hours * self.hourly_pay

        elif self.contract_type == "monthly":
            return self.monthly_salary

    def get_pay(self):
        return self.get_salary() + self.get_commision()


    def __str__(self):
        if self.contract_type == "hourly":
            if self.commision_contracts > 0:
                return f"{self.name} works on a contract of {self.hours} at {self.hourly_pay}/hour and receives a commision for {self.commision_contracts} contract(s) at {self.commision_hourly_pay}/contract. Their total pay is {self.get_pay()}."
            elif self.commision_bonus > 0:
                return f"{self.name} works on a contract of {self.hours} at {self.hourly_pay}/hour and receives a bonus commision of {self.commision_bonus}. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours} at {self.hourly_pay}/hour. Their total pay is {self.get_pay()}."

        if self.contract_type == "monthly":
            if self.commision_contracts > 0:
                return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commision for {self.commision_contracts} contract(s) at {self.commision_hourly_pay}/contract. Their total pay is {self.get_pay()}."
            elif self.commision_bonus > 0:
                return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives bonus commision of {self.commision_bonus}. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.get_pay()}."

billie = Employee("Billie", contract_type = "monthly", monthly_salary = 4000)
print(str(billie))
charlie = Employee("Charlie", contract_type = "hourly", hours = 100, hourly_pay = 25)
print(str(charlie))
renee = Employee("Renee", contract_type = "monthly", monthly_salary = 3000, commision_contracts = 4, commision_hourly_pay = 200)
print(str(renee))
jan = Employee("Jan", contract_type = "hourly", hours = 150, hourly_pay = 25, commision_contracts = 3, commision_hourly_pay = 220)
print(str(jan))
robbie = Employee("Robbie", contract_type = "monthly", monthly_salary = 2000, commision_bonus = 1500)
print(str(robbie))
ariel = Employee("Ariel", contract_type = "hourly", hours = 120, hourly_pay = 30, commision_bonus = 600)
print(str(ariel))
