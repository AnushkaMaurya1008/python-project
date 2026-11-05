print("me")
print("anushka")

name="Anushka"
age=17
salary=2500.00
is_student=True

print(type(name))
print(type(age))
print(type(salary))
print(type(is_student))

is_student=True
NSTI_collage=True



students=["Anita","Priya","Riya","Neha"]

print(students[0]) #access the emenent at 0 index
print(students[1]) #access the emenent at 1 index 

students[0]="Supriya" #modify the element of list
students[2]="Divya" #modify the element of list

print(students)
students.append("Princy")
print(students)

students.insert(1, "Princy")
print(students)

students.remove("Priya") #remove the elemet of list
print(students)

marks=(70,80,90,100)

print(marks)

marks[0]=90

print(marks)
marks[1]=90 #X

Set
name={"Shreya","Ajeet","Aditya","Shreya","Khushi","Shreya"}
print(name)

name.add("Ayush")
name.add("Ritika")


name.update(["Vishal","Rajesh","Prashant"]) #add multiple name 
print(name)


Dictionary

student=[
    {
    "name":"Ajeet",
    "age":27,
    "course":"AIPA",
    "Address":"Allahabad",
    "Mobile No":"9598925993"
},


{"name":"Aditya","age":26,"course":"AIPA","Address":"Varanasi","Mobile No":"9876543210"},




{"name":"Shreya","age":25,"course":"AIPA","Address":"Allahabad","Mobile No":"9876543210"},
]

print(student[2]["name"])

student = {"name": "Ajeet", "age": 27, "course": "AIPA"}
print(student["name"])
print(student["age"])
student["age"]=28
# student["city"]="Allahabad"
print(student)

student.items():
print(key,":",value)

get(), .keys(), .values()
print(student.get("course"))
print(student.keys())
print(student.values())

students = [
    {"name": "Aditya", "age": 26},
    {"name": "Shreya", "age": 25},
    {"name": "Ajeet", "age": 27},
]
print(students[1]["name"])
print(student["age"])
 

Arithmetic Operators
a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)


#Assignment 

# x=50

# x +=10 #x=x+10
# x -=10 #x=x-10
# x *=10 #x=x*10
# x /=10 #x=x/10
# x %=10 #x=x%10
# x //=10 #x=x//10
# x **= 10 #x=x**10

# print(x)

#Comparison Operators
# age=int(input("Enter your age :"))

# if age ==18: #control flow statement - decision
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")


#Comparison Operators Practice
#CODE 1- Greator Than
# age = 18
# required_age = 18

# print(age > required_age)
    
#CODE 2-Less Than
# marks = 35
# passing_marks = 40

# print(marks < passing_marks)

#CODE 3-Equal To
# password = 1234
# entered_password = 1234

# print(password == entered_password)

#CODE 4-Not Equal To
# a = 50
# b = 75

# print(a != b)

#CODE 5-Greator Than or Equal To
# attendance = 75
# minimum_attendance = 75

# print(attendance >= minimum_attendance)

#== For Comparison
#= For Value Assign

#Marks Comparison

# marks=35

# print(marks >=40)

# if marks >=40:  #Conditional Statement
#     print("Pass")
# else:
#     print("Fail")


# Check Even or Odd

# number = 12

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# number = 12

# if number % 7 == 0:
#     print("Even")
# else:
#     print("Odd")


# a=10
# b=14

# if a >= b:
#     print("Both are equal")
# else:
#     print("b is greator")


# n=7
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# a= int(input("Enter first no.:"))
# b= int(input("Enter secondnno.:"))

# if a > b:
#     print("First number is greator.")
# elif b >a:
#     print("Second number is greator.")
# else:
#     print("Both are equal.")

# password="Princy@1234"

# enter=input("Enter your password:")

# if password == enter:
#     print("Login successfully")
# else:
#     print("Invalid password")


# Student Marks Result

# marks = int(input("Enter student's marks: "))

# if marks >= 90 and marks <= 100:
#     print("Excellent")
# elif marks >= 75:
#     print("Very Good")
# elif marks >= 60:
#     print("Good")
# elif marks >= 40:
#     print("Pass")
# else:
#     print("Fail")


# Temperature Classification

# temperature = int(input("Enter temperature in Celsius: "))

# if temperature >= 40:
#     print("Very Hot")
# elif temperature >= 30:
#     print("Hot")
# elif temperature >= 20:
#     print("Warm")
# elif temperature >= 10:
#     print("Cool")
# else:
#     print("Cold")

# Shopping Discount Calculator
# amount = int(input("Enter shopping amount: "))

# if amount >= 5000:
#     print("20% Discount")
# elif amount >= 3000:
#     print("15% Discount")
# elif amount >= 1000:
#     print("10% Discount")
# elif amount >= 500:
#     print("5% Discount")
# else:
#     print("No Discount")

#Electricity Consumption Checker
# units = int(input("Enter electricity units consumed: "))

# if units >= 300:
#     print("High Consumption")
# elif units >= 200:
#     print("Medium-High Consumption")
# elif units >= 100:
#     print("Medium Consumption")
# elif units >= 50:
#     print("Low Consumption")
# else:
#     print("Very Low Consumption")     
 
#Control Flow
# for s in range(6):
#     print (s)

# for i in range(3,10,3):
#     print(i)

# for p in range (2,50,22):

#     print(p)

# for n in range (2,2000)
# print(p)

#Sum of numbers between 1 to 10
# total=0

# for i in range(1,101):
#     total +=i  #total = total + i

#     print(total)

#Square
# for x in range (1,11):
#     print(x**2)

#Reverse

# for i in range (10,0,-2):
#     print(i)

# count=0
# for i in range(1,101):
#    if i % 7 ==0:
#     count +=1
#     if i == 35:
#       break

# print(count)

#User input range Practice

# num = int(input("Enter the number: "))

# for i in range(1, 6):
#     print(num, "*", i, "=", num * i)

#Addition
# num = int(input("Enter the number: "))

# for i in range(1, 6):
#     print(num, "+", i, "=", num + i)

# num = int(input("Enter the number: "))

# for i in range (1,11):
#     print(num,"x",i,"=", num*i)

#Employee Salary Slip 

# employees = [15000, 18000, 20000, 22000, 25000]

# for salary in employees:
#     print("Monthly Salary:", salary)

#Attendance Register  

# attendance = ["Present", "Absent", "Present", "Present", "Absent", "Present", "Present"]

# count = 0

# for status in attendance:
#     if status == "Present":
#         count += 1

# print("Total Present:", count)

#Sales Report  

# sales = [1000, 1500, 2000, 1200, 1800, 2500, 2200]

# total = 0

# for sale in sales:
#     total += sale

# average = total / len(sales)

# print("Total Sales:", total)
# print("Average Sales:", average)

#Bonus Calculation  

# sales = [1000, 1500, 2000, 1200, 1800, 2500, 2200]

# total = 0

# for sale in sales:
#     total += sale

# average = total / len(sales)

# print("Total Sales:", total)
# print("Average Sales:", average)

#Inventory Check  

# inventory = {
#     "Pen": 5,
#     "Notebook": 15,
#     "Pencil": 8,
#     "Eraser": 20,
#     "Marker": 4
# }

# for item, quantity in inventory.items():
#     if quantity < 10:
#         print("Low Stock Alert:", item, quantity)

#Project Hours  

# hours = [5, 8, 6, 7, 4]

# total_hours = 0

# for hour in hours:
#     total_hours += hour

# print("Total Project Hours:", total_hours)


#Email List 

#

















# a=10
# b=10.5
# c="10"
# d=True 

# print(type(a))
# print(type(b))
# print(type(c))
# # print(type(d))

# Studentname ="Anushka"
# Studentage =18
# Course ="AIPA"
# Percentage=87.99
# passed="true"
# print("Studentname":Studentname)
# print("Studentage":Studentage)
# print(Course)
# print(Percentage)
# print(passed)

# employee record using 

# employee_data={
#     "Employee ID": 102,
#     "Employee Name": "Khusi",
#     "Salary": 2500.00,
#     "Department": "IT",
#     "Is Active": "True"}


# # print(employee_data)

# # list containing the names 
# students = ["Princy", "Nancy", "Ayushi", "Ayush", "Riya"]

# print("Complete list:", students)

# print("First student:", students[0])

# print("Last student:", students[-1])

# students.append("Anjali")

# students.remove("Riya")

# print("Final list:", students)


# # tuple containing the names

# months = ("January", "February", "March", "April", "May")
# print( months)
# print( months[0])
# print(len(months))

# dictionary for a student

# student={"name":"anushka",
#          "age":18,
#          "course":"AIPA",
#          "marks":"87.99",
#          "city":"mau",
#          }
# print(student["name"])
# print(student["marks"])
# student["mark"]=90
# print(student)
# print()
# print()


# # nested loop
# for i in range (1,4):
#     for j in range (1,3):
#         print("outer loop:",i,"innner loop:",j)


# for i in range (1,5):
#     for j in range (1,5):
#         print("outer loop:",i,"innner loop:",j)



# for r in range (1,5):
#     for c in range (1,6):
#         print("&",end=" ")
#     print()


#  for r in range (5,0,-1):
#     for c in range (r):
#         print("*",end="")
#     print()



# for r in range (1,5):
#     for c in range (1,r+1):
#         print(c,end="")
#     print()


# for num in range (2,11):
#     print("multiplecation of:",num)
#     for mulitiply in range (1,11):
#         print(num,"*",multiply,"=","num * multiply")
#     print()


# # Rectangle pattern


# for r in range (4):
#     for j in range (6):
#         print("*",end="")
#     print()
 

# #  Increasing triangle

# for r in range (1,8):
#     for j in range (r):
#         print("*",end="")

#     print()

# # Number square

# for r in range (4):
#     for j in range (1,5):
#         print(j, end="")
#     print()



# # 4. Multiplication tables

# for num in range (1,11):
#     print("table of",num)

#     for multiply in range (1,11):
#         print(num, "x",multiply,"=",num * multiply)
#     print()


# # Classroom seating

# for r in range(1, 6):
#     for s in range(1, 9):
#         print("r" + str(r) + "s" + str(s))
#     print()

# # Prime numbers

# for num in range (2,51):
#     is_prime = True

#     for i in range (2,num):
#         if num% i == 0:
#             is_prime=False
#             break


#     if is_prime:
#         print(num,end="")
#         print()


# # Pattern challenge


# for r in range (1,6):
#     for c in range (1, 6-r):
#         print(" ",end="")
#     for k in range (1, 2*r):
#         print("*",end="")
#     print()




# What is the function in python 
# A function is a reuseable block of code that perform a specific task. it runs when it is called.

# def add (a,b):
#     return a+b

# print(add(10,39))
# print(add(10,13))
# print(add(10,145))
# print(add(10,156))
# print(add(10,14))

# def total_bill(price,quantity):
#     total=price*quantity
#     return total


# price=int(input("Enter the price:"))
# quantity=int(input("Enter the quantity:"))


# print("Total bill:",total_bill(price, quantity))



# def multiply(x):
#     for i in range(1,11):
#         print(x,"x",i,"=",x*i)
# multiply(3)


# def add():
#     a=10
#     b=30
#     print(a+b)
# add()



# # Windsurf: Refactor | Explain | Generate Docstring | X
# def add(a,b):
#     return a+b
# # Windsurf: Refactor | Explain | Generate Docstring | X
# def sub(a,b):
#     return a-b
# # Windsurf: Refactor | Explain | Generate Docstring | X
# def multiply(a,b):
#     return a*b
# # Windsurf: Refactor | Explain | Generate Docstring | X
# def div(a,b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a/b

# print(multiply(12,10))


# print(sub(100,50))

# print(div(100,5))




# def calculate_total(marks):
#      return sum(marks)
# def calculate_average(marks):
#      return sum(marks)/len (marks)
# def result(average):
#      if average >=40:
#           return "pass"
#      else:
#          return "fail"
# student_name = input("enter student name:")

# marks = []

# for i in range(1,6):
#      mark = int(input("enter marks for subject " + str(i) + ":"))
#      marks.append(mark)
# total=calculate_total(marks)
# average=calculate_average(marks)
# result=result(average)

# print("student name:",student_name)
# print("total:",total)
# print("average:",average)
# print("result:",result)



# function in python of Questions 

# Greeting function

# def welcome_student(name):
#     print(f"Welcome, {name}! We are glad to have you here.")

# welcome_student("Anushka")

# Addition function

# def add_numbers(num1, num2):
#     return num1 + num2

# result = add_numbers(40,90)
# print(result)

# Even or odd
# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_even_odd(9))
# print(check_even_odd(8))
# print(check_even_odd(6))

# Factorial calculator
# def factorial(n):
#     result = 1

#     for i in range(1, n + 1):
#         result *= i

#     return result
# print(factorial(4))


# 5. Largest of three number

# def largest_of_three(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
        # return b/
    # else:
        # return c

# print(largest_of_three(10, 25, 15))


# Grade calculator


# def calculate_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"
# print(calculate_grade(85))


# List statistics
# def calculate_total(numbers):
#     return sum(numbers)

# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)

# def find_minimum(numbers):
#     return min(numbers)

# def find_maximum(numbers):
#     return max(numbers)

# numbers = [10, 20, 30, 40, 50]

# print("Total:", calculate_total(numbers))
# print("Average:", calculate_average(numbers))
# print("Minimum:", find_minimum(numbers))
# print("Maximum:", find_maximum(numbers))

# Banking application

# Initial balance
# balance = 0

# def deposit(amount):
#     global balance
#     balance += amount
#     print(f"Deposited: {amount}")

# def withdraw(amount):
#     global balance
#     if amount <= balance:
#         balance -= amount
#         print(f"Withdrawn: {amount}")
#     else:
#         print("Insufficient balance!")

# def display_balance():
#     print(f"Current Balance: {balance}")

# # Menu loop
# while True:
#     print("\n--- Banking Application ---")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Display Balance")
#     print("4. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         amount = float(input("Enter amount to deposit: "))
#         deposit(amount)

#     elif choice == 2:
#         amount = float(input("Enter amount to withdraw: "))
#         withdraw(amount)

#     elif choice == 3:
#         display_balance()

#     elif choice == 4:
#         print("Thank you for using the Banking Application!")
#         break

#     else:
#         print("Invalid choice. Please try again.")

# Grade calculator

# def calculate_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"

# marks = int(input("Enter marks: "))
# print("Grade:", calculate_grade(marks))

# 
# 7. List statistics

# def calculate_total(numbers):
#     return sum(numbers)

# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)

# def calculate_minimum(numbers):
#     return min(numbers)

# def calculate_maximum(numbers):
#     return max(numbers)

# # Example usage
# numbers = [12, 45, 7, 23, 56, 18]

# print("Total:", calculate_total(numbers))
# print("Average:", calculate_average(numbers))
# print("Minimum:", calculate_minimum(numbers))
# print("Maximum:", calculate_maximum(numbers))


# Student record processor
# def calculate_average(marks):
#     return sum(marks) / len(marks)

# def get_passing_students(students, pass_mark=40):
#     passing_students = []

#     for student in students:
#         average = calculate_average(student["marks"])
#         if average >= pass_mark:
#             passing_students.append(student["name"])

#     return passing_students

# # List of student dictionaries
# students = [
#     {"name": "Alice", "marks": [85, 90, 78]},
#     {"name": "Bob", "marks": [35, 40, 38]},
#     {"name": "Charlie", "marks": [60, 70, 65]},
#     {"name": "David", "marks": [25, 30, 35]}
# ]

# # Display average marks for each student
# for student in students:
#     avg = calculate_average(student["marks"])
#     print(f"{student['name']} Average: {avg:.2f}")

# # Display passing students
# print("\nPassing Students:")
# for name in get_passing_students(students):
#     print(name)


# 19/10/2006


# python in module

# import math

# print("square root:",math.sqrt(81))
# print("square of :",math.pow(5,3))
# print("factorial:",math.factorial(5))

# import random


# number=random.randint(1,10)
# print(number)

# print(random.choice(["anushka","kajal","anchal","shradha"]))

# import datetime

# today=datetime.date.today()
# print(today)

# currenttime=datetime.date.datetime.now()
# print(currenttime)



# import statistics

# marks=[50,40,20,40,80,60,70]

# print(statistics.mean(marks))
# print(statistics.median(marks))
# print(statistics.mode(marks))


# import os

# print(os.name)
# print(os.getcwd())
# os.mkdir("module_today")


# user-defind modules


# import module2
# print(module2.add(40,50))
# total=module2.x + module2.y
# print(total)

# 21/10/2026

# python file handling

# file=open("aipa5.txt","w")

# file.write("hellow aipa")
# file.close()

# with open("AIPA2.text","w") as file:
#     file.write("hellow student")



# append "a" - add a new

# with open("aipa2.text","a") as file:
#     file.write("\n praygraj UP")
#     file.write("\n India")

# import time
# with open("aipa.txt","r") as file:
#       for line in file:
#             print(line.strip())
#             time.sleep(2)
#    x=file.read()
#    print(x)


#    x=file.read(90)
#    print(x)

#    print(file.readline())
#    print(file.readline())
#    print(file.readline())     



    # print(file.readline().strip())
    # print(file.readline().strip())
    # print(file.readline().strip())

    # lines=file.readlines()

    # print(lines)

# try:
#     with open("aipa3.text","x") as file:
#          file.write("x mode")

# except:
#      print("file already exists")

# import csv

# std=[
#     ["nikita",17,"AIPA"],
#     ["anushka",18,"AIPA"],
#     ["nirupama",19,"AIPA"],
#     ["riya",16,"AIPA"]]

# with open("student.csv","w",newline="") as file: 
#     writer=csv.writer(file)
#     writer.writerows(std)

# handling dicectories & File

# import os,shutil,pathlib

# print(os.getcwd())
 
# os.mkdir("21 oct")

# print(os.listdir("."))

# shutil.rmtree("21 oct")

# os.rename("aipa.txt","copa.text")

# shutil.copy("copa.txt","")


# with open ("21oct/22oct/Aipa.txt","w") as file:
#     file.write("hello")

# from pathlib import Path 

# filename=input("enter the filename:")

# path=Path(filename)

# if path.exists():
#     print("file exists")
# else:
#     print("file does not exits")



# question 1
# Directory information

# import os,shutil,pathlib
# print(os.getcwd())
# print(os.listdir("."))

# Qest2
#  File existence
# from pathlib import Path
# filename=input("enter the filename:")
# path=Path(filename)

# if path.exists():
#     print("file exists")
# else:
#     print("file does not exits")


# QUEST 3
# Create nested folders

# import os,shutil,pathlib
# os.mkdir("college") 


# quest4
#  Find file type
# import csv
# Employee=[
#     ["riya",4500,"IT"],
#     ["nikita",50000,"IT"],
#     ["nirupam",40000,"IT"]]
# with open("Employee.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerows(Employee)

# quest 5
#  Backup a file
# import os,shutil,pathlib
# shutil.copy("student.csv","Employee.csv")

# quest 6
# Move files
# import os,shutil,pathlib
# shutil.move("MYPYTHONMODULE.py","python_practice_anushka.py")

# quest 7
#  Directory backup
from pathlib import Path

Path("test").mkdir(exist_ok=True)
with open("test/sample.txt", "w") as f:
    f.write("Hello AIPA")
    import shutil

shutil.copytree("test", "test_backup")

print("Backup created successfully!")

