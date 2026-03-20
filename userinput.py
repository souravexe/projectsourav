name = input("Enter your name:")
age = int(input("Enter your age:"))
marks1, marks2, marks3 = map(float, input("Enter marks in 3 subjects (separated by space):").split())
total = marks1 + marks2 + marks3
average = total / 3
print("\n---Student Report---")
print(f"Name: {name}")
print(f"Age: {age}")
print("Marks:", marks1, marks2, marks3, sep=",")
print("Total Marks:", total)
print("Average Marks=", round(average, 2))
print("Thank you", end=" ")
print("for using this program")