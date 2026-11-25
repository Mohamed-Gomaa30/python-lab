"""
    Open/Close Principle: states that software entities (classes, modules, function), 
    should be open for extension but closed for modification

    Example: 
    Payment System: An e-commerce application may initially support credit card payments and later add PayPal or UPI.
    By using a common payment abstraction, new payment methods can be introduced without modifying the existing payment-processing logic.
"""

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount): 
        pass 

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid by Credit Card:", amount)

class PayPal(Payment):
    def pay(self, amount):
        print("Paid by PayPal:", amount)

# interface method 
def process_payment(payment, amount): 
    payment.pay(amount)


card = CreditCard()
paypal = PayPal()

process_payment(card, 100)
process_payment(paypal, 200)