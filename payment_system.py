from abc import ABC, abstractmethod

#Create an abstract class named Payment using the built-in abc module
class Payment(ABC):
    
    #Define an abstract method named makePayment()
    @abstractmethod
    def makePayment(self):
        """Abstract method that must be implemented by any child class."""
        pass


#Create a class named MobileMoneyPayment that inherits from Payment
class MobileMoneyPayment(Payment):
    
    #Implement makePayment() in MobileMoneyPayment
    def makePayment(self):
        print("Payment made using Mobile Money")


#Create another class named CardPayment that inherits from Payment
class CardPayment(Payment):
    
    #Implement makePayment() in CardPayment
    def makePayment(self):
        print("Payment made using Bank Card")


#In the main section: Create objects of both classes and call makePayment()
if __name__ == "__main__":
    print("--- Individual Object Payment Execution ---")
    
    mobile_payment = MobileMoneyPayment()
    mobile_payment.makePayment()

    card_payment = CardPayment()
    card_payment.makePayment()

    print("\n--- Polymorphic Behavior via a Unified Loop ---")
    all_payment_methods = [MobileMoneyPayment(), CardPayment()]
    
    for payment_method in all_payment_methods:

        payment_method.makePayment()
