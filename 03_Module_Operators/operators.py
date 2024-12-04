import math
age = 21
height = 5.5
complex_num = 1 + 2j
#script to calculate area of triangle using user input
base = input('Enter base of triangle: ')
height_of_triangle = input('Enter height of triangle: ')
area_of_triangle = 0.5 * int(base) * int(height_of_triangle)
print('The area of the triangle is ', area_of_triangle)
#script to calculate perimeter of triangle using user input
a = input("Enter side a:")
b = input("Enter side b: ")
c = input("Enter side c: ")
perimeter = int(a) + int(b) + int(c)
print(f"The perimeter of the triangle is {perimeter}")
#script to get length and width of rectangle and calculate area and perimeter
length = input('Enter length of rectangle: ')
width = input('Enter width of rectangle: ')
area_of_rectangle = int(length) * int(width)
perimeter_of_rectangle = 2 * (int(length) + int(width))
print(f'Area of Rectangle: {area_of_rectangle}')
print(f'Perimeter of Rectangle: {perimeter_of_rectangle}')
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and 
#circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius_of_circle = input('Input Radius: ')
area_of_circle = pi * int(radius_of_circle) * int(radius_of_circle)
circumference = 2 * pi * int(radius_of_circle)
print('Area of Circle: ', area_of_circle)
print(f'Area of circumference: {circumference}')
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2 #slope is the coefficient of x
y_intercept = -2 #y is the constant
#Calculate x-intercept
x_intercept = -y_intercept / slope  # Set y = 0 and solve for x
#Print results
print("Equation: y = 2x - 2")
print("Slope:", slope)
print("Y-intercept:", (0, y_intercept))
print("X-intercept:", (x_intercept, 0))
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, x2 = 2, 6
y1, y2 = 2, 10
m = (y2 - y1) / (x2 -x1) #Slope(m)
#Euclidean distance(d)
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#Compare the slopes in tasks 8 and 9.
print(slope == m)
print(slope > m)
print(slope < m)

#length of 'python' and 'dragon' to make a falsy comparison statement.
length_of_python = 'python'
length_of_dragon = 'dragon'
print(len(length_of_python))
print(len(length_of_dragon))
print(len(length_of_python) > len(length_of_dragon))
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in length_of_python and length_of_dragon)
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
find_jargon = 'I hope this course is not full of jargon'
print('jargon' in find_jargon)

python = len(length_of_python)
python_to_float = float(python)
python_to_string = str(python)
#Output
print(python)
print(python_to_float)
print(python_to_string)

number = int(input("Enter a number: "))
# Check if the number is even
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is not an even number.")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
num = 2.7 
print(floor_division == int(num))
#Check if type of '10' is equal to type of 10
ten = '10'
num_ten = 10
print(ten == num_ten)
#Check if int('9.8') is equal to 10
nine = 9.8
print(int(nine) == num_ten)
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input('Enter hours: ')
rate = input('Enter rate per hour: ')
weekly_earning = int(hours) * int(rate)
print('Your weekly earning is: ', weekly_earning)
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
seconds_in_year = 365 * 24 * 60 * 60  # Days * Hours * Minutes * Seconds
#Maximum lifespan in years
max_years = 100
# Prompt the user to enter the number of years
input_years = int(input("Enter the number of years you have lived (up to 100): "))
total_secs = input_years * seconds_in_year
print('You have lived for ', total_secs)

