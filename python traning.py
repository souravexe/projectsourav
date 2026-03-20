# print("hello world")
# print(35)
# #variable store data
# a='this is a my first python code'
# print(a)


# my_name='sourav kumar'
# my1name='sourav kumar'
# my_name1='souarv kumar'
# _MY_NAME='sourav kumar'  

# b= 'sourav' #string data type
# print(b)

# #c=string () it's alaways satart from quotes '',"",''' ''',
# #d=list[]
# #e= float()


# c='chandani' #string data type
# print(type(c))

# d=1010 #integer data type
# print(type(d))

# e=2.1 #float data type
# print(type(e))

# import this
# from xml.etree.ElementPath import find

# #pascal case (first letter of each word is in capital letter)
# MyNameis='sourav kumar'

# #camel case (first word is in small letter and second word is in capital letter) 
# myName="sourav kumar"

# #flat case (lower case all the alphabates are in small letter.)
# myname="sourav kumar"

# #snak case (underscore between two word)
# my_name="sourav kumar"


# #1.arithmetic operator
# a=10
# b=20
# print("Arithmetic operator:")
# print(a+b)
# print(a-b)  
# print(a*b)
# print(a/b)
# print(a//b)  #(floor division - quotient)
# print(a%b)  #(modulus - remainder)
# print(a**b) # (exponentiation - power a^b)
# print()

#2.comparison operator
# a=10
# b=20
# print("Comparison operator:")
# print(a==b) #false
# print(a!=b) #true
# print(a>b) #false
# print(a<b) #true
# print(a>=b) #false
# print(a<=b) #true
# print() 

# #3.logical operator
# a=True
# b=False
# print("Logical operator:")
# print(a and b) # false
# print(a or b) # true
# print(not a) # false
# print(not b) # true
# print()

# # 4. bitwise operator
# a=5  # in binary: 0101
# b=3  # in binary: 0011
# print("Bitwise operator:")
# print(a & b)  # 1 (bitwise AND)
# print(a | b)  # 7 (bitwise OR)
# print(a ^ b)  # 6 (bitwise XOR)
# print(~a)     # -6 (bitwise NOT)
# print(a << 1) # 10 (left shift)
# print(a >> 1) # 2 (right shift)
# print()
 
# #5. assignment operator
# a=10    
# print("Assignment operator:")
# a+=5  # a = a + 5
# print(a)
# a-=3  # a = a - 3
# print(a)
# a*=2  # a = a * 2
# print(a)
# a/=4  # a = a / 4
# print(a)
# a//=2 # a = a // 2
# print(a)
# a%=3  # a = a % 3
# print(a)

# #6. identity operator
# a=[1, 2, 3]
# b=a
# c=[1, 2, 3]
# print("Identity operator:")
# print(a is b)  # True (a and b refer to the same object)
# print(a is c)  # False (a and c are different objects with the same content)
# print(a == c)  # True (a and c have the same content)
# print(a is not c)  # True (a and c are different objects)

# #data types in python

# #1. numeric: integer, float, complex
# #2. sequence: string, list, tuple
# #3. mapping: dictionary
# #4. set: set, frozenset
# #5. boolean: bool
# #6. binary: bytes, bytearray, memoryview

# #rule for creatinng variable
# my_list=[1,2,3,4,5,"you are not performing well in python"]
# print(my_list)

# my_list.append(5)
# print(my_list)

# my_list.append("kishan")
# print(my_list)

# my_list.insert(4,55)
# print(my_list)

# #string
# b="kishan maurya"
# print(type(b)) #indexing

# #list
# b1=[1,2,"kishan maurya"]
# print(type(b1)) #indexing

# #tuple
# b2=(4,5,6,"kishan maurya")
# print(type(b2)) #indexing

# #dictionary
# my_dictionary={"name":"kishan maurya","age":19,"city":"varanasi"}
# print(type(my_dictionary)) #indexing

# #sets
# my_sets={1,2,3,4,5,"kishan maurya"}
# print(type(my_sets)) #indexing

# k={1,2,2.1,2.5,"raghav","kishan maurya"}
# print(type(k)) #indexing

# #boolean
# a=True
# b=False
# print(type(a)) #indexing
# print(type(b)) #indexing


# my_list = [1,35,65,"you are not performing well in python"]
# print(my_list)

# #removinng element from list
# my_list = [1,35,65,"you are not performing well in python"]
# my_list.remove(35) #removes the first occurrence of the specified value
# print(my_list)

# #last element remove
# my_list = [1,35,65,"you are not performing well in python"]
# my_list.pop() #removes the last element from the list
# print(my_list)

# #removing element by index
# my_list = [1,35,65,"you are not performing well in python"]
# del my_list[1] #removes the element at index 1
# print(my_list)  

# #find the length of list
# my_list = [1,35,65,"you are not performing well in python"]
# print(len(my_list)) 

# #find the minimum and maximum element in list
# my_list = [1,35,65]
# print(min(my_list)) # minimum element in the list
# print(max(my_list)) # maximum element in the list

# #age category
# age=int(input("enter your age:"))
# if age<13: 
#     print("you are a child")
# elif age<20:
#     print("you are a teen ager")
# elif age<60:
#     print("you are an adult")
# else:
#     print("you are a senior citizen")

# n=5
# for i in range(1,n+1):
#     print("*"*i)    

# n=35
# #upper part
# for i in range(1,n+1):
#     print(" "*(n-i) + "* " * i) 
#     #lower part
# for i in range(n-1,0,-1):
#     print(" "*(n-i) + "* " * i)

# #tuplle are not changeable
# #tuple are always start from paranthesis ()

# my_tuple=(1,2,3)
# print(my_tuple)

# my_tuple=(2,"sourav kumar",3)
# print(my_tuple)

# my_tuple=(2,"sourav kumar",3,4.5)
# print(my_tuple)

# #tuple operations
# a=(1,2,3)
# b=(4,5,6)
# print(a+b) #concatenation
# print(a*2) #repetition
# print(b*5) #repetition

# tuple is not changeable
# t=(1,2,3,4,5)
# t[0]=10 #tuple are not changeable
# print(t)

# t=(1,2,3,4,5)
# print(t[0]) #indexing   

# a=("it's a rainy day \nyou should take an umbrella") #\n is used for new line
# print(a)

# a=("it's a rainy day \tyou should take an umbrella") #\t is used for tab space
# print(a)

# a=("it's a rainy day     you should take an umbrella") #multiple spaces
# print(a.find("you")) #find the index of the first occurrence of the specified value

# a=("it's a rainy day you should take an umbrella")
# print(a.find("z")) #find the index of the first occurrence of the specified value 

# a=("it's a rainy day     you should take an umbrella") 
# print(a.upper() ) #convert the string to uppercase

# a=("it's a rainy day     you should take an umbrella")
# print(a.lower()) #convert the string to lowercase

# a=("it's a rainy day     you should take an umbrella")
# print(a[6:16]) #printing udder index no 6 to 16

# a=("it's a rainy day     you should take an umbrella")
# print(a.split()) #split the string into a list of words

# a=("it's a rainy day     you should take an umbrella")
# print(a.replace("rainy","sunny")) #replace the specified value with another value

# a=("it's a rainy day     you should take an umbrella")
# print(a.strip()) #remove any leading and trailing whitespace from the string

# a=("it's a rainy day     you should take an umbrella")
# print(a.startswith("it's")) #check if the string starts with the specified value

# a=("it's a rainy day you should take an umbrella")
# print(a.startswith("you")) #check if the string starts with the specified value

# a=("it's a rainy day     you should take an umbrella")
# print(a.endswith("umbrella")) #check if the string ends with the specified 

# a=("it's a rainy day you should take an umbrella")
# print(a.count("a")) #count the number of occurrences of the specified value in the string

# a=(" it's a rainy day you should take an umbrella  ")
# print(a.strip()) #remove any leading and trailing whitespace from the string

# a=(" it's a rainy day you should take an umbrella  ")
# print(a)

# a=(" it's a rainy day you should take an umbrella  ")
# print(a.title()) #convert the first character of each word to uppercase and the rest to lowercase

# a=(" it's a rainy day you should take an umbrella  ")
# print(a.lstrip("a").startswith("a")) #remove any leading whitespace from the string and check if it starts with the specified value

# a=(" it's a rainy day you should take an umbrella  ")
# print(a.lstrip().startswith("a")) #remove any leading whitespace from the string and check

# a=(" it's a rainy day you should take an umbrella  ")
# print(a.lstrip().startswith("i")) #remove any leading whitespace from the string and check if it starts with the specified value

# a=(" it's a rainy day you should take an umbrella  ")
# print(a.rstrip().endswith("a")) #remove any trailing whitespace from the string and check

# a=(" it's a rainy day you should take an umbrella  ")
# print(a.rstrip().startswith("a")) #remove any trailing whitespace from the string and check if it starts with the specified value


##time module nikalane ke liye time module ka use karte hain

# import time
# timestamp=time.strftime('%H:%M:%S')
# print(timestamp)

# import time
# timestamp=int(time.strftime('%H'))
# print(timestamp)

# import time
# timestamp = int(time.strftime('%M'))
# print(timestamp)

# import time
# timestamp = int(time.strftime('%S'))    
# print(timestamp)


# #1. if statement
# a=10
# if a>5:
#     print("a is greater than 5")

# #2. if-else statement
# age=16
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

# #3. if-elif-else statement
# marks=85
# if marks>=90:
#     print("you got A grade")
# elif marks>=80:
#     print("you got B grade")
# else:
#     print("you got C grade")


# #use of if-elif-else statement
# rupees=12000
# if rupees>=10000:
#    print("you buy a phone")
# elif rupees>=50000:
#    print("you buy a laptop")
# elif rupees>=100000:
#    print("you buy a car")
# elif rupees>=500000:
#    print("you buy a house")
# elif rupees>=1000000:
#    print("you buy a yacht")
# elif rupees>=5000000:
#    print("you buy a private jet")
# elif rupees>=10000000:
#    print("you buy a rolls royce")
# else:
#    print("you save money")


# #4.nested if (find the number is positive even or odd)
# num=16
# if num>0:
#     if num%2==0:
#         print("num is a positive even number")
#     else:
#         print("num is a positive odd number")
# else:
#     print("num is a negative number or zero")



# #5. shorthand if statement
# a=10
# if a>5:
#      print("a is greater than 5")


# #6.short-hand if-else statement(ternary operator)
# a,b=10,20
# print("a is greater than b") if a>b else print("b is greater than a")



# #crating a calculator using if-elif-else statement
# num1=float(input("enter first number:"))
# num2=float(input("enter second number:"))
# operator=input("enter operator (+, -, *, /):")

# if operator=="+":
#     print(num1+num2)
# elif operator=="-":
#     print(num1-num2)
# elif operator=="*":
#     print(num1*num2)
# elif operator=="/":
#     if num2!=0:
#         print("result:", num1/num2)
#     else:
#         print("error: division by zero is not allowed")
# else:
#     print("invalid operation!")


#  #weater suggestion
# weather= input("enter the weather (sunny, rainy, cloudy):").lower()
# if weather=="sunny":
#     print("wear sunglasses")
# elif weather=="rainy":
#     print("take an umbrella")
# elif weather=="cloudy":
#     print("wear a jacket")  
# else:
#     print("i do't know the weather type")


# #traffic light suggestion
# light= input("enter the traffic light (red, yellow, green):").lower()
# if light=="red":
#     print("stop")
# elif light=="yellow":
#     print("slow down")
# elif light=="green":
#     print("go")
# else:
#     print("i do't know the traffic light type!")

# #loops
# #1.for loop
# for i in range(5):
#     print(i)

# #2.while loop (used when we do'nt know exactly how many times we want to execute a block of code)
# count=1
# while count<=5:
#     print("hello", count)
#     count+=1

#3.loop control statement
# break and continue














# #loop inside another loop 
# for i in range(2):
#     for j in range(3):
#         print("i=", i, "j=", j)

# #summary
# #for loop = used for reating a block of code a fixed number of times
# #while loop = used for reating a block of code until a certain condition is met
  

# # what is a loop?
# #loop is a programming construct that allows us to repeat a block of code multiple times. It is used to perform repetitive tasks without having to write the same code again and again. Loops are essential for automating tasks and processing data efficiently in programming.
# #(or untill the items to be iterated are exhausted)
# #loops let you outomate repetative taks : processing every item in a list, performing a task a certain number of times, or executing a block of code until a specific condition is met. Loops are fundamental for tasks like iterating through data structures, performing calculations, and creating dynamic behavior in programs.
# #lines ina life , aggregating numbers etc.

# #python has two main loop types:
# #1.for loop--iterates over a iterable (like a list, tuple, or string) and executes a block of code for each item in the iterable.
# #2.while loop -- reates while a condition remains true.
#   #for loop -- concept & usage

# # A for loop pulls items from an iterable one -by-one and executes a block of code for each item. The syntax is:
# fruits = ["apple", "banana", "cherry"]
# for f in fruits:
#     print(f)  # prins each fruit in the list

# # iterables vs iterators(briefly)
# #iterable :an cobject you can loop over (important __iter__or sequence protocol)--e.g., lists, tuples, strings, sets, dictionaries
# #iterable: an objecct with __ next__()and __iter__(); calling next()advances it untill stopiteration is raised--e.g., file objects, generators, iterators created from iterables using iter()


# #you can manually use iterators operations
# it=iter([1,2,3])
# print(next(it)) #1
# print(next(it)) #2
# print(next(it)) #3
# #next(it) #when exhauted -- stopiteration
# #range()-- commom with for loop

# #range(stop)--range(start, stop)--range(start, stop, step)--integer sequence generator(efficient for loop ranges)
# for i in range(0, 10, 2):
#     print(i) #prints even numbers from 0 to 8.





# #Q1. print numbers from 1 to 10 using for loop and while loop.
# for i in range(1, 11):
#     print(i)

# #Q2. print numbers from 10 down to 1 using a while looop.
# n=10
# while n>0:
#     print(n)
#     n-=1

# #Q3. print the multiplication table of 5 using a for loop.
# for i in range(1, 11):
#     print("5 x", i, "=", 5*i)

# #Q4.write a program the prints only even number between 1 and 20 using a while loop.
# for i in range(1, 21):
#     if i%2==0:
#         print(i)

# #Q5.print a pattern using a nested for loop.
# for i in range(1,15):
#     for j in range(1, i+1):
#         print("*", end="") #end="" is used to print the stars in the same line
#     print()



