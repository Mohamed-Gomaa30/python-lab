"""
    Concept of inheritance comes to solve fragile code, duplication, and 
    hard scale. 
    
    For Example:
        Image buildig Employee, Devoloper, Manager, and Data Scientist
        as sperate classes you note that, those classes have a shared attributes
        name, age, email, ..etc. So without inheritance gets copied and pasted into 
        each one. In the future the system code becomes hard to maintain or scale. 

        
    Note: we can define the inheritance relation as "is a" the clasa A is a class B.          
"""

class Employee: 

    def __init__(self, name: str, age: int, email: str = None): 
        self.name = name 
        self.age = age 
        self._email = email

    def login(self): 
        print("login employee account")

    def info(self): 
        return f"name: {self.name}, age: {self.age}"

class Devoloper(Employee):
    def __init__(self, name, age, email = None, role: str = "Devoloper"):
        super().__init__(name, age, email)
        self.role = role 

    def info(self): 
        return f"Devoloper:\nNname: {self.name}\nAge: {self.age}\nrole: {self.role}"

    def login(self): 
        super().login()
        print("login devoloper account")

    def __str__(self): 
        return self.info()
    
user = Devoloper("mohamed", 24, "Software Engineer")

print(user)

print(user.login())
