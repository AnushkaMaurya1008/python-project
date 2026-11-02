 21/10/2026

# python file handling

# file=open("aipa5.txt","w")

# file.write("hellow aipa")
# file.close()

# with open("AIPA2.text","w") as file:
#     file.write("hellow student")



# # append "a" - add a new

# with open("aipa2.text","a") as file:
#     file.write("\n praygraj UP")
#     file.write("\n India")

# import time
# with open("aipa.txt","r") as file:
#       for line in file:
#             print(line.strip())
#             time.sleep(2)
# x=file.read()
# print(x)


# x=file.read(90)
#    print(file.readline())
#    print(file.readline())
#    print(file.readline())     



#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline().strip())

#     lines=file.readlines()

#     print(lines)

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

# # handling dicectories & File

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



# # question 1
# # Directory information

# import os,shutil,pathlib
# print(os.getcwd())
# print(os.listdir("."))

# # Qest2
# #  File existence
# from pathlib import Path
# filename=input("enter the filename:")
# path=Path(filename)

# if path.exists():
#     print("file exists")
# else:
#     print("file does not exits")


# # QUEST 3
# # Create nested folders

# import os,shutil,pathlib
# os.mkdir("college") 


# # quest4
# #  Find file type
# import csv
# Employee=[
#     ["riya",4500,"IT"],
#     ["nikita",50000,"IT"],
#     ["nirupam",40000,"IT"]]
# with open("Employee.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerows(Employee)

# # quest 5
# #  Backup a file
# import os,shutil,pathlib
# shutil.copy("student.csv","Employee.csv")


# # quest 6
# # Move files
# import os,shutil,pathlib
# shutil.move("MYPYTHONMODULE.py","python_practice_anushka.py")

# # quest 7
# #  Directory backup
# from pathlib import Path

# Path("test").mkdir(exist_ok=True)
# with open("test/sample.txt", "w") as f:
#     f.write("Hello AIPA")
#     import shutil

# shutil.copytree("test", "test_backup")

# print("Backup created successfully!")




# try:
#     a=20
#     b=0
#     print(a/b)

# except ZeroDivisionError:
#     print("no.cannot be devided by 0")

#     a=30
#     b=15
#     print(a/b)

# x="anushka"
# y=4
# print("anushka+4)


# std={
#     "name:","anushka",
#     "age:",18
# }
# print(std("address"))







# try:
#     a=int(input("enter first no."))             
#     b=int(input("enter valid integer"))
#     print(a/b)

# except valueError:
#     print("please enter valid integers")

# except zeroDivisionError:
#     print("{cannot divide by 0.")
#     print("successful.")

# print("Successful.")





# try:
#     a=int(input("Enter first no."))
#     b=int(input("Enter second no."))

#     print(a / b)

# except (ValueError,ZeroDivisionError):
#     print("InValid entry!")

# print("Successful.")





# try:
#     num=int(input("enter number:"))

# except ValueError:
#     print("Invalid input.")
# else:
#     print("square of no.:",num ** 2)
# finally:
#     print("Run successful!")






# marks=int(input("enter your marks:"))
# if marks <0 or marks>100:
#     raise ValueError("marks cannot be less than o or more than 100.")
# print("marks accepted:",marks)
# print("successful")

# try:

#     marks=int(input("Enter your marks:"))
#     if marks <0 or marks >100:
#         raise ValueError("Marks cannot be less than 0 or more than 100.")

# except ValueError as nikita:
#     print("invalid marks",nikita)

# else:
#     print("Marks accepted:",marks)

# finally:
#     print("coding completed")






# class AIPAError(Exception):
    # pass

# try:
#     eligible=int(input("enter you qulification:"))
#     if eligible < 10 :
#         raise AIPAError("you are not qualified for AIPA admission.")
#     print("you are Eliligible.")
# except ValueError:
#     print("please enter valid number.")
# except AIPAError as ai:


#     print("Eligiblity issue: ",ai)
            
# try:
#     num=int(input("enter number:"))
#     print(100 / num)

# except Exception as e:
#     print("Error occured:",e)




# Practical 1: Safe Division Calculato

# a=50
# b=0
# print(a/b)


# try:
#     a=int(input("enter first no."))             
#     b=int(input("enter valid integer"))
#     print(a/b)

# except ValueError:
#     print("please enter valid integers")

# except ZeroDivisionError:
#     print("{cannot divide by 0.")
#     print("successful.")

# print("Successful.")


# Practical 2: Positive Number Validator


# num=int(input("enter your num:"))
# if num < 0 or num > 100:
#     raise ValueError("num cannot be negative")
# print("num accepted:",num)
# print("successful")


# Practical 3: List Index Handling

# num=[10,20,30,40,50,60]
# print(num)

# num=[10,20,30,40,50,60]
# try:
#     index=int(input("enter index (0-4):"))
#     print("num:",num[index])
# except IndexError:
#          print("Error: Invalid index! Please enter an index between 0 and 4.")
# except ValueError:
#     print("Error: Please enter a valid integer.")
