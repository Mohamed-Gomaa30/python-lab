"""
    Encapsulation is all about controling access data inside an object
    
    In another word protect the object internal state by exposing only
    selected methods and properties.

        For Example: 
            using getter and setter to deal with the object's data 

    In python there are three level if access: 
        i.  private attribute self.__attribute  -> we can access it using method or getter/setter 
        ii. protected attribute self._attribute -> within class itself or inherted classes
        ii. public attribute  self.attribute    -> its publically accessible        
"""

class BankAccount: 
    idid = 200000
    def __init__(self, id, balance):
        self._id = id # protected "accessed by using the instantiated object from class object._id"
        self.__balance = balance # private accessed by methods or getter/setter properties. 

    def deposit(self, amount): 
        self.__balance+=amount

    def withdraw(self, amount): 
        if 0 < amount <= self.__balance: 
            self.__balance -= amount
            return amount 
        return "Insufficient balance" 

    def get_balance(self): 
        return self.__balance



if __name__ == "__main__": 

    account = BankAccount(1, 1000)
    account.deposit(500)
    print(account.get_balance()) 
    account.withdraw(200)
    print(account.get_balance())  
    print(account._id)

        