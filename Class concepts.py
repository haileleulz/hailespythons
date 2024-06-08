# 1. What is a class in Python? Explain the concept of a class in Python and how it serves as a
#    blueprint for creating objects.

# Class is a blueprint of how the objects (instances) are to be built which means how it is created, modified, executed,
# and what its functions are. It is the general guide on how the instances are manipulated.
# Example :
# class Person:
#     def __init__(self, fullname,occupation,age):
#         self.fullname = fullname
#         self.occupation =occupation
#         self.age = age
#
#
# per_1 = Person("haile Leul", "Government", 30)
# per_2 = Person("ABC", "student", 25)
#
# print(per_2.__dict__)
#
# In the above example the class (Person) sets the guidelines for how the objects or instances must contain how they
# should be created. in this case Per_1 and Per_2 must contain datas fullname, occupation, and age It makes the coding
# simpler for having initialized the attributes of the instances in a constructor automatically rather than manually
# defining them all in the object are which makes the codes bulky and prone to errors and difficult to read.


# 2. What is an instance of a class? Describe what an instance is in the context of OOP and provide an example of
#    creating an instance from a class in Python.

# Instances are the objects that are created from the class, they contain at least one unique attribute from other
# instances and contain the actual data and info that are pre-given or taken as a parameter from the class constructor.

# In the previous example we have seen how per_1 and per_2 are created from the attributes from the
# classes __init__ or constructor which contains the three attributes fullname, age and occupation.


# 3. What are attributes and methods in a class? Define attributes and methods, and discuss how they differ in the
#    context of a Python class.

# Attributes are the characters or representations within the class that are defined differently within the instances.
# Methods are the behaviors or how they are to be represented when they are being called upon. In the previous example
# class(Person) we have attributes fullname, occupation and age which are the characters
# that every object should contain and as seen we have no method, so we can create one as follows

# class Person:
#     def __init__(self,  fullname, occupation, age):
#         self.fullname = fullname
#         self.occupation = occupation
#         self.age = age
#
#     def personal_info(self):
#         return f"{self.fullname} works as {self.occupation} and is {self.age} years old"
#
#
# per_1 = Person("haile Leul", "Government Officer", 30)
# per_2 = Person("ABC", "student", 25)
#
# print(per_1.personal_info())
#
# In this case we have constructed a method called (personal_info) which aim to describe the instances which we created
# as per_1 and per_2.

# 4. How do you initialize an object in Python? Explain the purpose of the __init__ method and show an example of how
#    it is used in a Python class.

# We can initialize objects in python by creating a special method called constructor, a method with contains an
# __init__ which  is used to set the attributes that are to be used while creating the objects, and then we set the
# first parameter to be (self) most preferable, but we can set other names which is also possible. this self stands as a
# representation of the instances within the init line and automatically recall the other parameters.

# class Person:
#     def __init__(self,  fullname, occupation, age):
#         self.fullname = fullname
#         self.occupation = occupation
#         self.age = age
#
# In the above example we have defined the __init__ and initialized it with the self-parameter and added
# attributes to it which are the main data points that are to be used when crating an instance.


# 5. What is inheritance in Python?
#    Describe the concept of inheritance and give an example of how one class can inherit from another in Python.

# Inheritance is a way of passing attributes, methods and constructors from a parent class to a child class unless it is
# specified within itself(method override). This means once the parent class is created all the child class can be
# created with just passing the parent class name into it. If there is a need to specify a method or add to our
# constructor we can make a modification on the child class without altering the parent or other child classes.
#
# For example:
# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#
#     def  greet(self):
#         return f"Hi, my name is {self.fname} {self.lname} and I am {self.age} years"
#
# person1 = Person("Haile","Leul",28)
# print(person1.greet())
#
# class Worker(Person):
#     def __init__(self, fname, lname,age, salary):
#         super().__init__(fname, lname, age)
#         self.salary = salary
#
# worker_1 = Worker("mesfin", "Yosef", 35,45000)
#
# class Student(Person):
#     def __init__(self, fname, lname, age, grade):
#         super().__init__(fname, lname, age)
#         self.grade = grade
#
# student_1 = Student("abc", "def", 15,"KG2")
#
# print(worker_1.greet())
# print(student_1.greet())

# 6. What is encapsulation? Why is it important in Python classes? Define encapsulation and explain its importance in
#    the design of robust and secure classes.

#  Encapsulation is the systematical way of hiding attributes of a class constructor and a method of the class to the
#  outside of the class and manipulating it through a number of other methods defined within the class. This can be
#  useful in data confidentiality and easier access to it through its method.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#
# emp1 = Employee("Haileleul", 25000)
# print(emp1.get_salary())
# print(emp1.name)

# in the above example we have encapsulated the attribute salary, so it can not be modified and to to do so we need to
# have a another method for modifying the private attribute.

# 7. What is polymorphism in OOP? How does Python support it? Explain the concept of polymorphism and provide examples
#    of how Python can implement polymorphism.

#   Polymorphism is the concept of having a similar method in more than one class and if such is the case
#   we can create one parent class and define that method in it for all other classes to share.

# example: in a company if we have the following division of workers, and they all have a method called work
# hours we would display them as follows.

# class Workers:
#     def __init__(self, fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     def work_hours(self):
#         print("working hours = 10")
#
# class Managers:
#     def __init__(self, fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     def work_hours(self):
#         print("working hours = 8")
#
# class Internship:
#     def __init__(self, fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     def work_hours(self):
#         print("working hours = 4")

# And this is where polymorphism come we can create a parent class for all and have them share its method

# class Employee:
#     def __init__(self, fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     def work_hours(self):
#         print("working hours = 10")
#
#
# class Workers(Employee):
#     def work_hours(self):
#         print("working hours = 10")
#
#
# class Managers(Employee):
#     def work_hours(self):
#         print("working hours = 8")
#
#
# class Internship(Employee):
#     def work_hours(self):
#         print("working hours = 4")
#
#
# x1 = Workers("Abc", "Def")
# x2 = Managers("Ghi", "Jkl")
# x3 = Internship("Mno", "Opq")
#
# x1.work_hours()
# x2.work_hours()
# x3.work_hours()


# 8. What does the `self` keyword represent in a class, and why is it necessary? Describe what self represents in the
# context of a Python class method and why it must be included in method definitions.

#  self is usually the first parameter passed on the method or constructor which is used to represent the instances
#  created and modify the parameter or attributes passed on.

# class Employee:
#     def __init__(self, fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#
# emp_1 = Employee("ABC","DEF")
# emp_2 = Employee("GHI","JKL")

# In the above example the (self) parameter is used to represent the instances and whenever we create a new one the
# instances take the place of the self and take on the parameters fname and lname.


# 9. What are class variables and instance variables? How do they differ? Distinguish between class variables and
# instance variables with examples illustrating their different uses.

#  class variables are variables that are defined outside, of any method and are used for all instances of the class,
#  they are accessed and modified by using the class name and dot before it.
#  instance variables are defined within the constructor and are unique to each of the instances, and they are preceded
#  and be accessed with the self parameter.
# Example
# class Employee:
#     number_of_emps = 0
#
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         Employee.number_of_emps += 1
#
#     def fullname(self):
#         print(f"Hi my name is {self.fname} {self.lname}")
#
#
# x1 = Employee("Abc", "Def")
# x2 = Employee("Ghi", "Jkl")
# x3 = Employee("Mno", "Opq")
#
# print(Employee.number_of_emps)
# x1.fullname()

# In the above example the number_of_emps is a class variable and is common for all instances while fname and lname are
# instance variables and are unique to every objects.

# 10. How do you create a private attribute or method in a Python class? Explain the notion of private members in a
# class and show how Python can simulate private attributes or methods using naming conventions.

# Private attributes and methods are encapsulation methods and are usually small or one  and does contain a number of
# other methods to gain access of them usually taking one. They are written using a double underscore(__) and the name
# of the attribute of the method.

# class Prisoner:
#     def __init__(self, fname, lname, crime, time):
#         self.fname = fname
#         self.lname = lname
#         self.__crime = crime
#         self.__time = time
#
#     def get_crime(self):
#         print(f"this person has committed a {self.__crime}")
#
#     def __prisoner_time(self):
#         return f"this is person must serve {self.__time} years."
#
#     def get_prisoner_time(self):
#         print(f"{self.__prisoner_time()}")
#
#
# c_1 = Prisoner("Haile","Leul", "Robbery",3)
# c_1.get_crime()
# c_1.get_prisoner_time()

# in the above example we have two private attributes those are crime and time, in which crime can be accessed through
# the get crime method and the time can be accessed through the get time method. For the prisoner_time method it can be
# accessed through get_prisoner_time method.


# 11. What is a constructor in Python?
#     Define what a constructor is and how it differs from other methods in a Python class.

# A constructor is a special method in a class that contains the attributes and parameters and is used as a guideline
# for creating instances within the class. It is written using the def  __init__ and (self,…) as the first line and then
# add the parameters after the comma and then define or initialize the values using the self.value. It differs from
# other methods in some ways like it carries the parameters the instances must contain, they are usually written
# without a return or a print statement.

# 12. Explain the `super()` function. When and why would you use it?
#     Discuss the purpose of the super() function in Python and provide an example of its use in
#     the context of class inheritance.

#   The super() function is used for inheriting a method from a parent class to a child class and is defined
#   in the second line and automatically pass on the attributes listed.
#  for example: in example 5 we defined the parent class Person and child classes worker and student
#  in the constructor of the worker and student we first initialize the attributes then we use the super() method
#   for taking the attributes and variable swe need to pass it to the child classes.
#
# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname = fname
#         self.lname = lname
#         self.age = age


# def __init__(self, fname, lname,age, salary):      # for worker the super(). automatically pass the fname,lname and
#        super().__init__(fname, lname, age)         # age attributes to the worker class


# def __init__(self, fname, lname, age, grade):      # for student the super(). automatically pass the fname,lname and
# super().__init__(fname, lname, age)                # age attributes to the worker class

# 13. What are magic methods in Python? Provide examples.
#     Explain what magic methods are and how they enable operator overloading in Python,
#     with examples such as __str__ and __add__.

#  they are methods that are called when the classes are called upon and are usually associated with the creation of
#  instances (constructors) or string representation (__str__) or even aritimetic operations like addition (__add__).

# class Student:
#     def __init__(self, fname,lname, grade1):
#         self.fname = fname
#         self.lname = lname
#         self.grade1 = grade1
#
#     def __str__(self):
#         print(f"My name is {self.fname} {self.lname}")
#
#     def __repr__(self):
#         return f"Student('{self.fname}', '{self.lname}', {self.grade1})"
#
#     def __add__(self, other):
#         return self.grade1 + other.grade1
#
#
# num1 = Student("Haile","Leul",3)
# num2 = Student("Zeni","Gedefaw",5)
# result = num2.grade1 + num1.grade1
# num1.__str__()
# print(num1.__repr__())
# print(result)


# 14. How does method overriding work in Python? Describe method overriding and show how a subclass can change the
#     implementation of a method defined in its superclass.

# Method overriding is when the child classes inherit a method from the parent class but then again if the child has
# another implementation or behavior that need to be specific then we can overwrite the original method with the child
# class as follows

# class Person:
#     def daily_activity(self):
#         print(f"Gets up in the morning.")
#
#
# class Parent(Person):
#     def daily_activity(self):
#         print(f"Goes to work early in the morning.")
#
#
# class Child(Person):
#     def daily_activity(self):
#         print(f"Goes to school early in the morning.")
#
#
# p1 = Person()
# par1 = Parent()
# c1 = Child()

# p1.daily_activity()
# par1.daily_activity()
# c1.daily_activity()
#
# the class Parent inherits daily activity from class Person but modified the string to "goes to work early in the
# morning" and the class  Child did the same but modified it to "goes to school early in the morning".


# 15. What is the difference between class methods and static methods? Explain the difference between a class method
# and a static method, including how to declare them and typical use cases for each.

#  A class method is a method that is associated with the class, and it initializes with a cls and can be called upon
#  with the same parameter that is cls. A static method is a method that is not associated with the class and take no
#  initialization it can take values but not initialization like cls or self.

# class Student:
#     bonus_points = 0
#
#     def __init__(self, fname, lname, grade,level):
#         self.fname = fname
#         self.lname = lname
#         self.grade = grade
#         self.level = level
#
#     @classmethod
#     def get_bonus_points(cls, grade):
#         if grade > 85:
#             return 10
#         elif grade > 75:
#             return 5
#         else:
#             return 0
#
#     @staticmethod
#     def get_school_fee(level):
#         if level < 5:
#             school_fee = 500 * 4
#         elif level <= 8:
#             school_fee = 750 * 4
#         elif level > 9:
#             school_fee = 1000 * 4
#         return school_fee
#
#
# stud1 = Student("Haile", "Wolfe", 82, 4)
# print("Bonus Points:", Student.get_bonus_points(stud1.grade))
# print("School fee:", Student.get_school_fee(stud1.level))

# 16. What is composition in OOP? How is it applied in Python?
#     Define composition and discuss how it can be used in Python to build more complex objects from simpler objects.

# composition is the idea of creating a class from another class without using the inheritance method . It is basically
# appending an initial class to a new class and sharing its attributes and methods with the newer classes.

# class Phone:
#     def __init__(self, brand, control_device):
#         self.brand = brand
#         self.control_device = control_device
#
#     def how_to_uses_of_item(self):
#         if self.control_device.lower == "smart":
#             return "Please click on the screen for use "
#         else:
#             return "Please use the buttons for use"
#
# class Radio:
#     def __init__(self, size, accessories):
#         self.size = size
#         self.accessories = accessories
#
#     def get_information(self):
#         return "Scroll between channels to update and entertain yourself"
#
# class Electronics:
#     def __init__(self, type, brand, control_device, size, accessories):
#         self.type = type
#         self.phone = Phone(brand, control_device)
#         self.radio = Radio(size, accessories)
#
#     def how_to_use_item(self):
#         return self.phone.how_to_uses_of_item()
#
#     def get_information(self):
#         return self.radio.get_information()
#
#
# p_1 = Phone("Nokia","dull")
# print(p_1.how_to_uses_of_item())
# r_1 = Radio("Pocket", "battery")
# print(r_1.get_information())
# e_1 = Electronics("device", "samsung", "smart","pocket", "chargeable")
# print(e_1.get_information())
# print(e_1.how_to_use_item())


# 17. What is the purpose of the `__del__` method in Python?
#     Explain the role of the __del__ method and how it relates to an object's lifecycle.

# __del__ is a magic method that is used for a clean-up purpose it is defined within a class and usually deletes all the
# instances used in that class.It is envoked automatically and does what is defined for it.
#
# class FileHandler:
#     def __init__(self, filename):
#         self.filename = filename
#     def __del__(self):
#         print(f"File {self.filename} closed")
#
#
# handler = FileHandler("example.txt")
# handler2 = FileHandler("EA sports.apk")

# 18. How can you restrict access to methods in a Python class? Discuss ways to make methods within a class private or
#     protected, and why such restrictions might be necessary.

# We can restrict access to a method by making them private and thus written with an underscore before the attribute
#  or method this can be useful for confidentiality and risk deduction. It was briefly explained in data encapsulation.

# class National_Bank:
#     def __init__(self, name, saving=0):
#         self.name = name
#         self.__saving = saving
#
#     def __customer_saving(self, new_saving):
#         self.__saving = new_saving
#         return self.__saving
#
#     def update_saving_amount(self, new_saving):
#         return self.__customer_saving(new_saving)
#
#     def get_saving_amount(self):
#         return self.__saving
#
#
# bank1 = National_Bank("Abyssinia")
# bank1.update_saving_amount(2500)
# print(bank1.get_saving_amount())

# In this practical example we have an attribute that shouldn't be public and access to the outside world should be
# limited, so we have to make it private and access to it should be through other methods.

# 19. What are abstract classes in Python? How do you create and use them? Define abstract classes and explain their
# role in Python with examples, including how to use the abc module to define them.

# Abstract classes are classes that does take a constructor but are the blueprints for other classes, and they contain
# an abstract method, and they are to be used by the subclasses.

# from abc import ABC, abstractmethod

# class Animal:
#
#     @abstractmethod
#     def move(self):
#         pass
#
#     @abstractmethod
#     def living_area(self):
#         pass
#
#     @abstractmethod
#     def meal(self):
#         pass
#
#
# class Dog(Animal):
#     def__init__(self, name)
#     self.name = name
#
#     def move(self):
#         print("I can walk")
#
#     def living_area(self):
#         print("I live with humans")
#
#     def meal(self):
#         print("I am a carnivore")
#
#
# class Monkey(Animal):
#     def__init__(self, name)
#     self.name = name
#
#     def move(self):
#         print("I can climb")
#
#     def living_area(self):
#         print("I live in trees")
#
#     def meal(self):
#         print("I am a herbivores")

# In the above example the class animal take no constructor and has no methods defined to do a specific task instead
# they are used to guide the child classes to contain them.

# 20. How can you use multiple inheritance in Python? What are the potential pitfalls?

# Multiple inheritance is when a child class takes methods and attributes from more than one parent class. Its potential
# drawbacks are complexity and methods are overloaded which may be difficult to manipulate.

# class Father:
#     def skills(self):
#         print("Gardening, programming")
#
# class Mother:
#     def skills(self):
#         print("cooking, Planning")
#
#
# class Child(Father,Mother):
#     def skills(self):
#         Father.skills(self)
#         Mother.skills(self)
#         print("Sports")
#
#
# c = Child()
# c.skills()
