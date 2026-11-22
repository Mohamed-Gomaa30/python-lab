"""
    polymorphism is all about Mehtod + Overriding

    inheritance: child classes inherit attributes and behaviors form 
    a parent class

    method overriding: child classes provide their own 
    implementation of inherited methods

    same method but different logic 
"""

class Payment:

    def pay(self):
        print("payment process") 

class CreditCard(Payment):

    def pay(self): 
        print("CreditCard payment process") 

class PayPal(Payment):

    def pay(self): 
        print("PayPal payment process")  

class BankTransfer(Payment):

    def pay(self): 
        print("BankTransfer payment process")  


payments = [
    Payment(), 
    CreditCard(), 
    PayPal(), 
    BankTransfer()
]


for payment in payments: 
    payment.pay()