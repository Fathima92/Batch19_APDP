# -*- coding: utf-8 -*-
"""SOLID.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13sgCJvyluR1fhgD3Hczts953Kg0Fb3Vo
"""



#Single responsiblity principle
# Example 1
class ReportGenerator:
    def generate_report(self, data):
        pass

class FileSaver:
    def save_to_file(self, content, filename):
        pass

class ExcelExporter:
    def export_to_excel(self, data, filename):
        pass

# Without Single responsiblity principle
# Example 2
class Order:
    item =[]
    quantities =[]
    price =[]
    status ="open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):
        total = 0;
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total

    def pay (self, payment_type, security_code):

        if payment_type == "debit":
            print("processing debit payment")
            print(f"verifying security code: {security_code}")
            self.status= "paid"

        elif payment_type == "credit":
            print("processing credit payment")
            print(f"verifying security code: {security_code}")
            self.status = "paid"

        else:
            raise Exception(f"Unknown payment type: {payment_type}")

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
order.pay("debit", "123495")

# with Single responsiblity principle
# Example 2

class Order:
    item =[]
    quantities =[]
    price =[]
    status ="open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):
        total = 0;
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total


class PaymentProcessor:

    def pay_credit (self, order, security_code):
            print("processing credit payment")
            print(f"verifying security code: {security_code}")
            order.status = "paid"

    def pay_debit (self, order, security_code):
            print("processing credit payment")
            print(f"verifying security code: {security_code}")
            order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaymentProcessor()
processor.pay_debit(order, "123495")

# open close principle
#Example 1
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

#Example 2
from abc import ABC, abstractmethod

class Order:
    item =[]
    quantities =[]
    price =[]
    status ="open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):
        total = 0;
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("processing credit payment")
        print(f"verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("processing credit payment")
        print(f"verifying security code: {security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("processing credit payment")
        print(f"verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = DebitPaymentProcessor()
processor.pay(order, "123495")

#without liskov
class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")

# with liskov

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        return "Sparrow flying"

class Ostrich(Bird):
    def move(self):
        return "Ostrich running"

# Liskov Princple
# Example 1

from abc import ABC, abstractmethod

class Order:
    item = []
    quantities = []
    price = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):

        total = 0
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address):
        self.email_address = email_address
    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("abc@gmail.com")
pro2 =CreditPaymentProcessor(123456)
pro3 = DebitPaymentProcessor(456895)
processor.pay(order)

# Interface Seg
# Example 1
from abc import ABC, abstractmethod

class IMachine(ABC):
    @abstractmethod
    def print(self, data):
        pass

    @abstractmethod
    def scan(self, data):
        pass

class AllInOnePrinter(IMachine):
    def print(self, document):
        print(f"Printing {document}")

    def scan(self, document):
        print(f"Scanning {document}")


a = AllInOnePrinter()
a.print("hello")
a.scan("hello")

# Interface Segregation
# example 1
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class AllInOnePrinter(Printer, Scanner):
    def print(self, document):
        print(f"Printing {document}")

    def scan(self, document):
        print(f"Scanning {document}")


a = AllInOnePrinter()
a.print("hello")
a.scan("hello")

# Interface Segregation
# example 2
from abc import ABC, abstractmethod

class Order:
    item = []
    quantities = []
    price = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):

        total = 0
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def auth_sms(self, code):
        pass
    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying sms code {code}")
        self.verified = True
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authourized")
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def auth_sms(self, code):
        raise Exception("Credit Card Payment dont support SMS code authourization")
    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address):
        self.email_address = email_address

    def auth_sms(self, code):
        print(f"Verifying sms code {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authourized")
        print("processing credit payment")
        print(f"verifying security code: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("abc@gmail.com")
processor.auth_sms(123456)
processor.pay(order)

from abc import ABC, abstractmethod

class Order:
    item = []
    quantities = []
    price = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):

        total = 0
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class PaymentProcessor_SMS(PaymentProcessor):

    @abstractmethod
    def auth_sms(self, code):
        pass

class DebitPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying sms code {code}")
        self.verified = True
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authourized")
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying sms code {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authourized")
        print("processing credit payment")
        print(f"verifying security code: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentProcessor("abc@gmail.com")
processor.auth_sms(123456)
processor.pay(order)

# Depedency Inversion
# Example 1
class SMSService:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")

class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self, message_service):
        self.message_service = message_service

    def notify_email(self,message):
        self.message_service.send_email(message)

    def notify_sms(self,message):
       self.message_service.send_sms(message)


# Dependency Injection
email_service = EmailService()
sms_service = SMSService()

email_notification = Notification(email_service)
sms_notification = Notification(sms_service)

email_notification.notify_email("Your code is encrypted, Check Mail")
sms_notification.notify_sms("Your code is encrypted, Check SMS Alert")

# Depedency Inversion
# Example 2
from abc import ABC, abstractmethod

class Order:
    item = []
    quantities = []
    price = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.price.append(price)

    def total_price(self):

        total = 0
        for i in range(len(self.price)):
            total += self.quantities[i] * self.price[i]
        return total

class Authorizer(ABC):
    def is_authorized(self) -> bool:
        pass

class SMSAuth(Authorizer):

    authorizer = False

    def verify_code(self, code):
        print(f"verifying code {code}")
        self.authorizer = True

    def is_authorized(self) -> bool:
         return self.authorizer

class NotRobot(Authorizer):
    authorizer = False
    def not_robot(self):
        print("Are yot a robot?")
        self.authorizer = True

    def is_authorized(self) -> bool:
        return self.authorizer

class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authourized")
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing credit payment")
        print(f"verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authourized")
        print("processing credit payment")
        print(f"verifying security code: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = SMSAuth()
processor = DebitPaymentProcessor("123455",authorizer)
authorizer.verify_code(123456)
processor.pay(order)