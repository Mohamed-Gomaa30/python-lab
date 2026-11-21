
class User: 
    def __init__(self, name: str = None):
        self.name = name

    def __str__(self): 
        return f"Hello ya: {self.name}"



user1 = User("mohamed Gomaa")

print(user1)