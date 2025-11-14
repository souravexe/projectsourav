# print("hello world")

# x="good"

# def my_function():
#     print("python is " + x)
#     my_function()

# def my_function():
#     print("python is " + x)
# my_function()



# a="sourav"
# b="papa"
# print(a+b)



# list

# my_list=["apple","banana"]
# print(type(my_list))
# print(my_list)



# my_list=["apple","banana","cherry",1, 2, "ture"]
# print(my_list[1:5])

# my_list=["apple","banana","cherry","sjc","herohonda","tata"]
# my_list[1]="mango"
# print(my_list)


# my_list=["computer","mouse","keyboard","monitor","speaker"]
# print(my_list[-5:-2])
# print(my_list[-4:])





# sl = [1,2,3,4,5,6,7,8,9,"shiva",77]
# list2 = ["yellow","pink","orange"]
# sl[3] = "abc"
# print(sl)
# print(sl[2:4])

# print(sl[9:20:5])

# sl.insert(5,"God")
# print(sl)
# sl.append("RED")

# sl.extend(list2)
# print(sl)
# sl.remove("yellow")
# print(sl)
# sl.pop()
# print(sl)
# sl.pop()
# print(sl)       


# lst = [8,3,5,8,6,3,1,4,7,90,6]
# lst.sort()
# print(lst)

# text="hello"

# print(text.upper())
# print(text.lower())
# print(text.lower())
# print(text.replace("hello","world"))
# print(text.split())



#x=5
#y="bdcbk"

#forword starting
#print(x + y)
#x="sourav"
# y=20
# print(f"my name is {x} and my age is {y}")

#add sub mul devi..
# a=8
# a-=9
# print(a)



# d=3
# n=9

# print(d==n)
# print(d!=n)
# print(d>=n)
# print(d<=n)
# print(d>n)
# print(d<n)




# C=0
# L=C
# G=7
# #print(L)
# print(C is L)
# print(C is not L)

# name={"nitesh","panday","verma","agnihotri"}
# print(name)


# students={
#     "colour":"kala",
#     "age":16,
#     "grade":"A+"
# }
# print(students)



#if else

# age = 20

# if age >= 18:
#     print("You are adult")
# else:
#     print("You are not adult")



#if else

# age=16

# if age>18:
#     print("you are adult")

# elif age==18:
#     print("you are teenager")

# elif age==16:
#     print("you are 16")
# else:
#     print("you are not adult")


# C=69

# if C>49:
#     print("C is greater then 49")

#     if C>89:
#         print("C is greater then 89")
#     else:
#         print("C is not greater then 89")


# num = int(input("enter a number"))

# rem = num % 2

# if(rem == 0):
#    print("even")
# else:
#    print("odd")



# age=18

# if age>=18:
#     print("it is eligible for driving")

# else:
#     print("it is not eligible for driving")


# i = 1
# while i <= 50:
#     print(i)
#     i += 1



# i = 1
# while i<=10:
#     print(3*i)
#     i += 1


# i = 1
# while i <= 20:
#     print(i)
#     i -= 2
#print("end of loop")

# word="python"

# for a in word:
#     print(a)

# for i in range(1, 4):
#     print(i)

# for j in range(1, 3):
#     print(j)

#     print(f"i={i},j={j}")


# i = 1
# while i <= 5:
#     print(i)
#     if (i == 3)
#     i +=1
#print("end of loop") 


# print odd number

# i = 1
# while i <= 10:
#     if(i % 2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1



#print even number
 
# i = 1
# while i <= 10:
#     if(i % 2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1



# def greet():

#     print("Hello,Python!")


# greet() #calling the function


#Functions

# def love(pinky):
#     print(f"livay ,{pinky}")

# love("advanture")
# love("pop")


# def add(a,b):
#     return a + b 

# result=add(5,3)
# print(result) #8

# def add(a,b):
#     return a - b 

# result=add(5,3)
# print(result)



# def add(a,b):
#     return a * b 

# result=add(5,3)
# print(result)

# def add(a,b):
#     return a % b 

# result=add(5,3)
# print(result)


# x=24

# def my_function():

#     y=99

#     print(x,y)

# my_function()

# print(x)
# print(y)

# def greet():
#     print("Hello!")

# greet()


# def love(pinky):
#     print(f"livay ,{pinky}")

# love("advanture")


#local variables

# def f():
#     x = 10   # local variable
#     print("inside f, x =", x)

# f()
# print(x)  # NameError: x is not defined (x is local to f)


#global variables

# message = "hello"   # global

# def greet():
#     print(message)  # read global — OK

# greet()  # prints "hello"



#calss
# class car:
#     def __init__(self,brand,color):
#         self.brand=brand #Attribute
#         self.color=color #Attribute

#     def drive(self):
#         print(f"{self.color}{self.brand} is driving car")
        

# #object
# car1=car("BMW","Red ")
# car2=car("Audi","Black ")
# car3=car("Tata","White ")

# car1.drive()
# car2.drive()
# car3.drive()


#Array

# import array

# number=array.array('i',[1,2,3,4,5])
# print(number)


# Use Python's standard library random to avoid requiring numpy
# import random

# x = random.randint(0, 1)
# print(x)

# import random

# x = random.random()
# print(x)


#from numpy import random

# x=random.randint(100)
# print(x)

# x=random.rand()
# print(x)

# x=random.randint(100,size=(5))
# print(x)

# x=random.randint(100,size=(3,5))
# print(x)

# x=random.randint(100,size=(2,3,4,))
# print(x)

# x=random.randint(100,size=(2,3,4,5))
# print(x)


#Pandas


# import pandas as pd

# data = [10, 27, 23, 45, 38]
# s = pd.Series(data)

# print(s)

# import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [24, 27, 22, 32, 29],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# }

# df = pd.DataFrame(data)

# print(df)


#From a numpy array

import numpy as np

# arr=np.array([1,2,3,4,5])

# s=pd.Series(arr)

# print(s)


#From a dictionary

# data={"Math":90,"Science":85,"English":88}

# s=pd.Series(data)

# print(s)
      


# import tkinter as  tk
# from tkinter import messagebox

# #Functions
# def add_task():
#     task = entry.get()
#     if task!="":
#         listbox.insert(tk.END,task)
#         entry.delete(0,tk.END)
#     else:
#         messagebox.showwarning("Warning","Task cannot be empty!")

#     try:
#         selected=listbox.curselection()[0]
#         listbox.delete(selected)
#     except IndexError:
#         messagebox.showwarning("Warning","Please select a task to delete!")

# def update_task():
#     try:
#         selected=listbox.curselection()[0]
#         new_task=entry.get()
#         if new_task!="":
#             listbox.delete(selected)
#             listbox.insert(selected,new_task)
#             entry.delete(0,tk.END)
#         else:
#             messagebox.showwarning("Warning","Task cannot be empty!")
#     except IndexError:
#         messagebox.showwarning("Warning","Please select a task to update!")

# def remove_task():
#     try:
#         selected=listbox.curselection()[0]
#         listbox.delete(selected)
#     except IndexError:
#         messagebox.showwarning("Warning","Please select a task to delete!")

# #GUI setup
# root=tk.Tk()
# root.title("To-Do List App")
# root.geometry("400x400")
# root.config(bg="#f5f5f5")


# #input field
# entry=tk.Entry(root,width=30,font=("Arial",14))
# entry.pack(pady=10)

# #Buttons

# btn_frame=tk.Frame(root,bg="#f5f5f5")
# btn_frame.pack(pady=5)

# tk.Button(btn_frame,text="Add Task",width=10,command=add_task).grid(row=0,column=0,padx=5)
# tk.Button(btn_frame,text="Remove Task",width=10,command=remove_task).grid(row=0,column=1,padx=5)
# tk.Button(btn_frame,text="Update Task",width=10,command=update_task).grid(row=0,column=2,padx=5)
# tk.Button(btn_frame,text="Remove Task",width=10,command=remove_task).grid(row=2,column=1,padx=5)

    
# #Task List
# listbox=tk.Listbox(root,width=40,height=10,font=("Arial",12))
# listbox.pack(pady=10)

# root.mainloop()


# Functions to update expression in the text

# Create main window

import tkinter as tk

import tkinter as tk

#Function to update expression in the text entry
def press(key):
    entry_var.set(entry_var.get() + str(key))


#Function to evaluate the final expression
def equalpress():
    try:
        result=str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set(" Error ")

#Function to clear the text entry
def clear():
    entry_var.set("")   

#Create main window

root = tk.Tk()
root.title("Basis Calculator")
root.geometry("300x400")

#Entry widget for display

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20),bd=10,relief="sunken",justify="right")
entry.grid(columnspan=4, ipadx=8, ipady=15, pady=10)

#Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

#Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18),height=2,width=4, command=equalpress,bg="lightgreen")
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18),height=2,width=5, command=lambda t=text:press(t))
    btn.grid(row=row, column=col, padx=5,pady=5)    

#Clear

clear_btn = tk.Button(root, text='C', font=("Arial", 18), height=2, width=22, bg="yellow", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()

#Run app :
root.mainloop()