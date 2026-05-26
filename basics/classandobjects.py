# Class = blueprint / design / template to create objects or instances 
# Object = class ka real instance
# Method = function inside class
# Attribute =  Variable inside class
# perameter = method m ane vali values
# Instance variable = Har object ka alag data
# Class variable = Sab objects ke liye same
# Encapsulation = Encapsulation ka matlab hai data aur methods ko ek class ke andar bundle karna.
# Inheritance = Inheritance ka matlab hai ek class(child) dusri class(parent) ke properties aur methods ko inherit (use) kare.
# Abstraction = Abstraction ka matlab hai important cheez dikhana aur internal details chhupa dena.(“ATM use karte ho, andar ka system nahi pata”)
# Polymorphism  = Polymorphism ka matlab hai ek hi method ka different behavior hona.
# oops pillares : Encapsulation, Inheritance, Abstraction, Polymorphism
# Inheritance types : single inheritance : Ek child class sirf 1 parent se inherit karti hai
# Multiple Inheritance : Ek child class multiple parents se inherit karti hai ( by , seperated )
# Multilevel Inheritance : (Grandparent → Parent → Child) child direct grandparent class ko access kr skta h 
# Hierarchical Inheritance: Ek parent se multiple child classes
# self = point to the current object (“jo object method call kar raha hai, uski baat ho rahi hai”)
# cls = point to the class 
# Constructor = “Constructor (init) ka use object create hote hi uske attributes initialize karne ke liye hota hai.”
# attributes = object create krte time uske prenthesis m jo values dete hai 
# “Agar object creation ke time values set nahi karni ho, to constructor optional hai aur use skip kar sakte hain.”
# “Object ke attributes ko access karne ke liye object.attribute syntax use karte hain.”
# “Jab hume multiple similar records store karne hote hain, tab hum class ka use karte hain, kyunki har record ke liye alag variables banana practical nahi hota.”
# name = perameter (bahar se aayi hui value)
# self.name = attributes (object ke andar banne wala variable)
# @ staticmethod : Static method ek independent method hota hai jo class ke andar define hota hai lekin na to object (self) par depend karta hai aur na hi class (cls) par.
# staticmethod ko directly class k through call karte hai 
# Types of Methods
# Instance Method : object k data par kam hota h 
# class method  : class ke data pe kaam karta hai 
# Static Method : independent hota hai
# @property : method ko attribute jaisa use karne deta hai


class math:
    
    @staticmethod
    def add(a , b): # method define 
        return a + b 
    # method call no dependency on object and class
print(math.add(2 , 3))




# Real world scenerion : Bank account 
# account holder name
# balance
# deposit kar sakte hain
# withdraw kar sakte hain

class bankaccount():
    def __init__(self , name , balance):
        self.name = name 
        self.balance = balance

    def deposite(self , amount):
        self.balance += amount
        print("Deposited", amount)

    def withdraw(self , amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn", amount)
        else:
            print("Insufficient balance")
        
    def showbalance(self):
        print("Current balance:", self.balance)

account1 = bankaccount("swati" , 1000)
account1.showbalance()
account1.deposite(500)
account1.showbalance()
account1.withdraw(200)
account1.showbalance()
account1.withdraw(2000)


# scenerio for all three methods 

class Student:

    school = "ABC School"   # class variable

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    #  Instance Method
    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # Class Method
    @classmethod # (decorator)
    def change_school(cls, new_name):
        cls.school = new_name # ye new_name is class ka attribute hai 
        # cls -> student 

    # Static Method
    @staticmethod
    def is_pass(marks):
        return marks >= 40
    


s1 = Student("Swati", 85)

# Instance method
s1.show_details()

# Class method
Student.change_school("XYZ School")
print(Student.school)

# Static method
print(Student.is_pass(85))

