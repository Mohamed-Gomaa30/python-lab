"""
    that that each class should have only one primary responsibity

    Example: In a restaurant, a chef prepares food, a waiter serves customers, and a cashier handles payments.
    Each person has a separate responsibility.

    Without SRP: a class that handles several unrelated tasks becomes 
    difficult to modify and maintain
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary


class SalaryCalculator:

    def calculate_salary(self, employee):
        return employee.get_salary()


class EmployeeRepository:

    def save(self, employee):
        print("Employee saved to database")


class EmployeeReport:

    def generate(self, employee):
        print(f"Generating report for {employee.get_name()}")


class EmailService:

    def send_email(self, employee):
        print(f"Email sent to {employee.get_name()}")


employee = Employee("Mohamed", 50000)

salary_calculator = SalaryCalculator()
repository = EmployeeRepository()
report = EmployeeReport()
email_service = EmailService()

print(
    f"Salary: {salary_calculator.calculate_salary(employee)}"
)

repository.save(employee)
report.generate(employee)
email_service.send_email(employee)