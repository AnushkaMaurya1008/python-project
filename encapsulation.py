# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.__salary = salary
#     def get_salary(self):
#         return self.__salary

#     def inc_salary(self, amount):
#         if amount >0:

#             self.__salary += amount
#             print("salary update")

#         else:
#             print("Invalid Amount")

# emp=Employee("Shailesh",25,50000)
# print("Salary:", emp.get_salary())

# emp.inc_salary(8000)
# print("New Balance:", emp.get_salary())




# inheritance

# single inheritance



# class Animal():
#     def property(self):
#         print("Animal has 4 legs")


# class Dog(Animal):
#     def bark(self):
#         print("dog barks")

# D=Dog()
# D.property()
# D.bark()




# class Father():
#     def skill1(self):
#         print("driving")

# class Mother():
#     def skill2(self):
#         print("cooking")

# class Child(Father,Mother):
#     def skill3(self):
#         print("Inherited skills from parent:")

# x=Child()
# x.skill1()
# x.skill2()
# x.skill3()

# Multiple Inheritance

# class Grandfather():

#     def house(self):
#         print("Grandfather's house")


# class Father(Grandfather):

#     def bike(self):
#         print("Father's bike")


# class Son(Grandfather):

#     def laptop(self):
#         print("Son's Laptop")


# class Grandson(Father, Son):
#     print("Grandson's car")
        
# s=Son()
# s.house()
# s.bike()
# s.laptop()


# g=Grandson()
# g.house()

# Hierchical inheritance


# class Institute():
#     def name(self):
#         print("NSTI w Allahabad")
# class teacher(Institute):
#     pass
# class student(Institute):
#     pass
# class Housekeeping(Institute):
#     pass

# t=teacher()
# s=student()
# h=Housekeeping()


# s.name()
# t.name()
# h.name()






# question 1

# Student Management System (Single Inheritance)

# class Fruit():
#     def fruit_name(self):
#         print("this is a fruit")

# class Apple(Fruit):
#     def Apple_color(self):
#         print("Apple color is Red")

# name=Apple()

# name.fruit_name()

# name.Apple_color()



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# class student(Person):
#     def __init__(self, name, age, roll_no, course):
#         super().__init__(name, age)
#         self.roll_no = roll_no
#         self.course = course

#     def display_student(self):
#         self.display_details()
#         print("Roll No:", self.roll_no)
#         print("Course:", self.course)

# s1 = student("Nirupama",20, 101, "Python")

# s1.display_student()

# 2. Bank Account System (Single Inheritance)
# 

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def show_balance(self):
#         print("Balance:", self.balance)

# obj = BankAccount(5000)
# obj.show_balance()

# 3. Family Assets (Multilevel Inheritance)

# class Grandfather:
#     def house(self):
#         print("Grandfather owns a house")


# class Father(Grandfather):
#     def bike(self):
#         print("Father owns a bike")


# class Son(Father):
#     def laptop(self):
#         print("Son owns a laptop")


# s = Son()
# s.house()
# s.bike()
# s.laptop()

# 4  Employee Hierarchy (Multilevel Inheritance)

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         print("Name:", self.name)


# class Employee(Person):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.emp_salary = salary

#     def salary(self):
#         print("Salary:", self.emp_salary)


# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team = team_size

#     def team_size(self):
#         print("Team Size:", self.team)


# m = Manager("Amit", 75000, 10)
# m.get_name()
# m.salary()
# m.team_size()


# 5. College Management System (Hierarchical Inheritance)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks

#     def display(self):
#         print("Student Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)


# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def display(self):
#         print("Teacher Name:", self.name)
#         print("Age:", self.age)
#         print("Subject:", self.subject)


# s = Student("Riya", 19, 88)
# t = Teacher("Sharma", 40, "Python")

# s.display()
# print()
# t.display()


# 6. Vehicle Management System (Hierarchical Inheritance

# class Vehicle:
#     def start(self):
#         print("Vehicle Started")


# class Car(Vehicle):
#     def air_condition(self):
#         print("Car has Air Conditioning")


# class Bike(Vehicle):
#     def helmet_required(self):
#         print("Helmet is Required")


# class Bus(Vehicle):
#     def passenger_capacity(self):
#         print("Bus Capacity: 50 Passengers")


# c = Car()
# b = Bike()
# bs = Bus()

# c.start()
# c.air_condition()

# b.start()
# b.helmet_required()

# bs.start()
# bs.passenger_capacity()


# 7. Smart Phone System (Multiple Inheritance)
# class Camera:
#     def take_photo(self):
#         print("Photo Captured")


# class MusicPlayer:
#     def play_music(self):
#         print("Music Playing")


# class SmartPhone(Camera, MusicPlayer):
#     def make_call(self):
#         print("Calling...")


# sp = SmartPhone()

# sp.take_photo()
# sp.play_music()
# sp.make_call()


# 8 8. Working Student (Multiple Inheritance)

# class Student:
#     def study(self):
#         print("Student is Studying")


# class Employee:
#     def work(self):
#         print("Employee is Working")


# class WorkingStudent(Student, Employee):
#     def manage_time(self):
#         print("Managing Study and Work")


# ws = WorkingStudent()

# ws.study()
# ws.work()
# ws.manage_time()


# 9 Company Structure (Hybrid Inheritance)


# class Employee:
#     def attendance(self):
#         print("Attendance Marked")


# class Developer(Employee):
#     def write_code(self):
#         print("Writing Code")


# class Tester(Employee):
#     def test_software(self):
#         print("Testing Software")


# class TeamLead(Developer, Tester):
#     def manage_team(self):
#         print("Managing Team")


# tl = TeamLead()

# tl.attendance()
# tl.write_code()
# tl.test_software()
# tl.manage_team()

# 10 Educational Institute (Hybrid Inheritance)

class Person:
    def display_name(self):
        print("Name: Rahul")


class Student(Person):
    def study(self):
        print("Student is Studying")


class Teacher(Person):
    def teach(self):
        print("Teacher is Teaching")


class Mentor(Student, Teacher):
    def guide(self):
        print("Mentor is Guiding")


m = Mentor()

m.display_name()
m.study()
m.teach()
m.guide()