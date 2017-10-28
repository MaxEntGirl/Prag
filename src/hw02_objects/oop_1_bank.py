"""
Exercise 1: (5 points)

a) Using the slides & the script, put together a file
    containing the complete Account class.
    Each method must have a documentation string at the
    beginning which describes what the method is doing.
    (1 points)

b) Create a main application where you create a number of accounts.
    Play around with depositing / withdrawing money.
    Change the account holder of an account using a setter method.
    (1 point)

c) Change the withdraw function such that the minimum balance
    allowed is -1000.
    (1 point)

d) Write a function apply_interest(self) which applies an interest
    rate of 1.5% to the current balance and call it on your objects.
    (1 points)

e) Draw a UML diagram representing your Account class. (1 point)

"""

import re
class Account:
    """ Diese Klasse enthält Attribute wie balance, number sowie holder und Methoden
    wie __init__, withdraw, deposit, print_info, set_holder, __str__ und apply_interest. 
    Mit der Methode withdraw  wird das Geld vom Konto abgehoben und mit 
    Methode deposit auf das Konto eingezahlt. 
    Die Methode print_info gibt den Kontostand zurück und mit set_holder wird 
    ein anderer Kontoinhaber gesetzt. 
    Mit apply_interest werden 1.5% Zinsen der Balancehinzugefügt
    Alle Kontoinformationen werden bei Aufruf als string zurückgegben
    """
    
    # CONSTRUCTOR
    def __init__(self, num, person):
        # diese  Methode wird automatisch nach Erstellen des Objekts aufgerufen.
        # Der Name und die Kontonummer werden gesetzt, die Balance initial auf 0 gesetzt
        self.balance = 0
        self.number = num
        self.holder = person
        
    # METHODS
    def withdraw(self, amount):
        # mit dieser Methode wird Geld vom Konto abgehoben. Maximal ist ein Kredit von 1000 möglich
        if self.balance - amount < -1000:
            amount = self.balance + 1000
        self.balance -= amount
        return amount
    def deposit(self, amount):
        # mti dieser Methode wird Geld auf das Konto eingezahlt (der Balance hinzugefügt).
        self.balance += amount
        return amount
    def print_info(self):
        # diese gibt den Kontostand (Balance) zurück
        print("Balance:", self.balance)

    def set_holder(self, person):
        # diese Methode setzt einen anderen Kontoinhaber (holder)
        if (not type(person) == str):
            raise TypeError
        if not re.match("\w+( \w+)*", person.strip()):
            raise ValueError
        self.holder = person
    def __str__(self):
        # Methode, die Informationen bei Aufruf als String zurückgibt
        res = "*** Account Info ***\n"
        res += "Account ID:" + str(self.number) + "\n"
        res += "Holder:" + self.holder + "\n"
        res += "Balance: " + str(self.balance) + "\n"
        return res  
    def apply_interest(self):
        # diese Methode addiert 1.5% Zinsen zur Balance .
        self.balance = self.balance + self.balance * 0.015 

if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    
    annesAcc = Account(1, "Anne")
    annesAcc.deposit(500)
    cash = annesAcc.withdraw(2000)
    print("Oh no, I only got:", cash)
    annesAcc.print_info()
    print(annesAcc)
    
    stefansAcc = Account(2, "Stefan")
    stefansAcc.deposit(1000)
    stefansAcc.print_info()
    cash = stefansAcc.withdraw(1500)
    print("Oh no, I only got:", cash)
    stefansAcc.print_info()
    stefansAcc.set_holder("Andrea")
    stefansAcc.print_info()
    
    jingsAcc = Account(3, "Jing")
    jingsAcc.deposit(1000)
    jingsAcc.print_info()
    jingsAcc.withdraw(100)
    jingsAcc.print_info()
    jingsAcc.apply_interest()
    print(jingsAcc)
    
    willsAcc = Account(4, "Will")
    willsAcc.deposit(5000)
    willsAcc.withdraw(1389)
    willsAcc.set_holder("Jing")
    print(willsAcc)
