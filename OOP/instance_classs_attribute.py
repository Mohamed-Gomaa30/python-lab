
"""
    class: is a blueprint for creating objects 
    object: an isntance created from a class 
    attributes: data stored inside an object 
    methods: how the object behavour 
    self: refer to the current object 


    What is the Instance/Class Attributes 

        Instance Attribute: variables unique to each individual object 
        Class Attributes: variables shared by all objects of a class
"""

class User: 

    class_name = "User Class"

    def __init__(self, name: str = None):
        """
            This is instance attribute where those attributes
            are specificed for specific user. 
        """ 
        
        self.name = name 

    def __str__(self): 
        return self.name


user1 = User("mohamed")
user2 = User("gomaa")

print("="*20)
print("Instance Attribute")
print(user1)
print(user2)

print("="*20)
print("Class Attribute")
print(User().class_name)

