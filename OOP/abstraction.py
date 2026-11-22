"""
    Abstraction foucsing on what can object do, Not how. 
    In python the superclass use `ABS` -> Abstract Base Classes

    In brif think of it as a contract with parent class and child class 
"""


from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass  

class CreditCard(Payment):

    def pay(self): 
        print("CreditCard payment process") 

class PayPal(Payment):

    def pay(self): 
        print("PayPal payment process")  

class BankTransfer(Payment):

    def pay(self): 
        print("BankTransfer payment process")  

# class CryptoTransfer(Payment):
#     pass 


payments = [ 
    CreditCard(), 
    PayPal(), 
    BankTransfer(),
    # CryptoTransfer()
]

for payment in payments: 
    payment.pay()

print(Payment.__abstractmethods__)
print(Payment.mro)

    

