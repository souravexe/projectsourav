                                             #Day one                                                                                                                                                                                                                                              #                                   DAY 1
# print("Hello World")
# print("My self sourav kumar")

# print(1+2)

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print("You entered:", a, "and", b)
# sum = a + b
# Difference = a - b
# Multiply = a * b
# Division = a / b
# Modulus = a % b
# Exponent = a ** 2
# float_division = a // b
# Remainder = a % b



# print("The Value of ", a ,"+",b ,"is",sum)
# print("The Value of ", a ,"-",b ,"is",Difference)
# print("The Value of ", a ,"*",b ,"is",Multiply)
# print("The Value of ", a ,"/",b ,"is",Division)
# print("The Value of ", a ,"%",b ,"is",Modulus)
# print("The Value of ", a ,"**",b ,"is",Exponent)
# print("The Value of ", a ,"//",b ,"is",float_division)
# print("The Value of ", a ,"%",b ,"is",Remainder)



##                                      DAY 2

# #Variable Types
# # 1-flat case
# mynameclass= "xyz"
# # 1-Camel case
# myNameclass="xyz"
# # 1-snack case
# my_name_class="xyz"
# # 1-pascel case
# MyNameClass="xyz"


# # TypeCasting
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print("The value of", a, "and", b, "is :", a + b)
# print("The value of", a, "and", b, "is :", str(a) + str(b))


# # MULTIPLICATION
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# mul = a * b
# print("Multiplication of both number is : ", mul)




#rules for variable
# 1. variable strt with alpha no numeric allowed
#2. no special char except _ is allowed




            #                               DAY 3



# #while loop
# i=int(input("enter the value of i: "))
# while(i<=38):
#     i=int(input("enter the value of i: "))
#     print(i)

# if(i>=38):
#     print("enter the smaller value of i: ")
# else:
#    print("done with the loop")

#star pyramid
# rows= int(input("enter number of rows: "))
# for i in range(1, rows + 1):
#     print(" " * (rows - 1), end="")
#     print("*" * (2 * i - 1))
 
# for i in range(1, 11):
#     if i == 5:   
#         continue
#     print("9 x", i, "=", 9 * i)
# for i in range(1, 11):
#     if i == 5:   
#       break 
#     print("9 x", i, "=", 9 * i)
# Nested if-else example
# number=int(input("enter a number: "))

# if number > 0:   
#     print("Positive number")
#     if number % 2 == 0:
#         print("It's even")
#     else:
#         print("It's odd")
# else:
#     print("Non-positive number")
#functionss---



# def multiply(a1,a2):
#     print(a1*a2)

# print(multiply(8,5))


# def multiply(a1,a2):
#     return a1*a2

# print(multiply(8,5))
# print(multiply(8,"a"))

# def print_name(name):
#     print("Your name is:", name)


# print_name("hero")

# def print_age(age):
#     print("Your age is:", age)


# print_age("21")

# list[1,1,2]
# tuple (1,2,3)
# set {1,2,3}
# dict{"key":"value"}

# a={1,1,3,6,5}
# print(a)

# # Dictionary

# student = {
  
#     "name": "hero",
#     "age": 19,
#     "branch": "DS"
# }

# print(student)
# print(student["name"])
# print(student["age"])
# print(student["branch"])

#                                     DAY 4


#Qus-- write a function multiply that multiplies two number but also accept and multiply string
# def multiply (p1,p2):
#     return p1*p2
# print(multiply(8,5))
# print(multiply(8,'a'))

#pandas
#  import pandas as pd
# df = pd.DataFrame([11,22,33], columns=['col_name'])
# print(df)
# print(type(df))
# import pandas as pd
# data = {
#     'Name': ['Madhav', 'vanshika', 'lalita'],
#     'Age': [16,17,18],
#     'salary' : [90000,50000,75000]
# }

# df = pd.DataFrame(data)
# print(df)

#basic dataframe understanding

# import pandas as pd
# data = {
#     'Name': ['Madhav', 'vanshika', 'lalita'],
#     'Age': [16,17,18],
#     'salary' : [90000,50000,75000]
# }

# df = pd.DataFrame(data)
# print(df.head(2))


#import pandas as pd
# data = {
#     'Name': ['Madhav', 'vanshika', 'lalita'],
#     'Age': [16,17,18],
#     'salary' : [90000,50000,75000]
# }
#  df = pd.DataFrame(data)
# print(df.tail(2))

# #df.shape(4,3)
# #df.columns --list of column name in a dataframe 
# #df.rename -- renames column names eg-- 
# df.rename(columns={'salary': 'Monthly _salary'},inplace=True)
# print(df)
# df.to_csv('Test_data.csv', index=False)
# load_df=  pd.read_csv('Test_data.csv')
# load_df
#df(name) for single row
#select multiple columns
#df[['name', 'monthly salary']]
#select single row
#df.loc[df.name=='Madhav']
#select multiple rows
#df.loc[df.name=='madhav']
# import pandas as pd
# data = {
#     'Name': ['Madhav', 'vanshika', 'lalita','Mohan'],
#     'Age': [16,17,18,20],
#     'salary' : [90000,50000,75000,80000]
# }
# df = pd.DataFrame(data)

# df_age_filter = df[df['Age']>=18]
# print(df_age_filter)  #filter and store dataframe in new variable

# df_filtered = df[(df['Age'] >= 18) & (df['salary'] >= 50000)]
# print(df_filtered)#multiple filter condition
# df_where=df.where(df['Age']>=18)
# print(df_where)
# df_where=df.where(df['Age']>=18, other='not eligible')
# print(df_where)
# df['team']= ['ceo','HR', 'CTO','DA']
# df['bonus']= df['salary']*0.20
 # df.loc[len(df)]=['Prince',19,22000,'IT',2000]
#df.loc[df.Name=='Madhav','Salary']=95000
#df=df.drop(df[df.Name=='Prince'].index)#drop using column value filter
# df.drop('bonus', axis=1, inplace=True)
# print(df.drop)
# df=df.sort_values('salary')
# df['DOJ']=['2024-01-01','2024-01-15','2024-05-25','2024-05-27']
# print(df)