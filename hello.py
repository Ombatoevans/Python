import datetime
from datetime import datetime
#<--------------------PYTHON BASICS------------------>
 
#displaying output
print('hello world')
         #or
print("hello world")

#variables
age = 90
print(age)    
    #or
name = "john"
print(name)

#receiving input from the user
name = input('Enter Name: ')
print("Your Name is " +name)
       #calculating age
birth_year = int(input("Enter your year of birth: "))
age = 2023 - int(birth_year)
print("You are " +str(age))
          #or
birth_year = int(input("Enter your year of birth: "))
year = datetime.now().year
age = year - int(birth_year)
print("You are " +str(age))
            #adding two integers
x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))
sum = x+y
print("The sum of x and y is " +str(sum))

#strings
book = "Introduction to OOP"
print(book)
           #more about strings 
book = "Introduction to OOP"
print(book.upper())
print(book.lower())
print(book.find('P'))
print(book.replace('to', '2'))

#operations
                 #Arithmetic operations...........
 #add                
x = 7
y = 8
addition = x+y
print(addition)
#division
x = 45
y = 40
division = x/y
print(division)
#modulus
x = 10
y = 3
mod = x%y
print(mod)
#expornent
x = 2
y = 4
expo = x**y
print(expo)
                     #comparision and logical operators...............
x = 5 > 2
print(x)
#logical operatotors
height = 50
print(height > 25 & height < 60)
 
 #lists 
fruits = ["bananas","oranges","apples"]
print(fruits)
 
 #range
numbers = range(5)
for numbers in numbers:
    print(numbers)
                    









