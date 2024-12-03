# Exercises: Level 1
#ArewaDS 30 Days of Python Module_02
# Day 2: 30 Days of python programming
first_name = 'Lukman'
last_name = "Kabiru"
fullName ='Lukman Kabiru Bala'
country = "Nigeria"
city = 'Kebbi'
age = 21
current_year = 2024
is_married = False
is_true = True
is_light_on = True
first_name, last_name, age, is_married = 'Lukman', 'Kabiru', 21, True 

# Exercise 2
print(type(first_name))
print(type(last_name))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(current_year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))
#Compare the length of your first name and your last name
print(len(first_name) == len(last_name))
print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name)) 
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

#Output of Arithmetic Operations
print(f'total = {total}')
print(f'Difference = {diff}')
print(f'Product = {product}')
print(f'Division = {division}')
print(f'Modulus = {remainder}')
print(f'Exponential = {exp}')
print(f'Division = {floor_division}')
#Given radius as 30
radius = 30
pi = 3.142
area_of_circle = pi * (radius ** 2)
circum_of_Circle = 2 * pi * radius
print("Area of circle: ", area_of_circle)
#print("Circumference: ",  circum_of_circle)
#taking radius as input
radius_input = input('Input Radius: ')
area = pi * (int(radius_input) ** 2)
print(f'Area of Circle(radius given by user) = {area}')
#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_fname = input('Enter First Name: ')
user_lname = input('Enter Last Name: ')
user_country = input('Enter Country: ')
user_age = input("Input Age: ")

#output 
print(f'First Name: {user_fname}')
print(f'Last Name: {user_lname}')
print(f'user_country: {user_country}')
print(f'user_age: {user_age}')
#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')