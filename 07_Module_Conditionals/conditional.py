#Exercises: Level 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

#Enter your age: 30
#You are old enough to learn to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.
age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print('You are old enough to drive.')
else:
    remaining_years = 18 - age  
    print(f'You need {remaining_years} more years to learn to drive.') 
#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

#Enter your age: 30
#You are 5 years older than me.
my_age = 22
your_age = int(input('Enter your age: '))
if my_age == your_age:
    print('We are age mates.')
elif your_age > my_age:
    age_diff = your_age - my_age
    print(f'You are {age_diff} years older than me.')
else:
    age_diff = my_age - your_age
    print('I am',age_diff,'years older than you.')
#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

#Enter number one: 4
#Enter number two: 3
#4 is greater than 3
num_one = int(input('Enter number one: '))
num_two = int(input('Enter number two: '))
if num_one > num_two:
    print('{} is greater than {}'.format(num_one, num_two))
elif num_one < num_two:
    print('{} is smaller than {}'.format(num_one, num_two))
else:
    print('{} is equal to {}'.format(num_one, num_two))
#Exercises: Level 2
#Write a code which gives grade to students according to theirs scores:

#80-100, A
#70-89, B
#60-69, C
#50-59, D
#0-49, F
score = int(input('Enter Score: '))
if score >= 80:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
elif score >= 50:
    print('D')
else:
    print('F')
#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
season = input('Enter Month: ')
if season == 'september' or season == 'october' or season == 'november':
    print('The season is Autumn')
elif season == 'december' or season == 'january' or season == 'february':
    print('The season is Winter')
elif season == 'march' or season == 'april' or season == 'may':
    print('The season is spring')
else:
    print('The Season is Summer') 
#The following list contains some fruits:

#```sh
#fruits = ['banana', 'orange', 'mango', 'lemon']
#```
fruits = ['banana','orange','mango','lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = input('Enter Fruit: ')
if fruit not in fruits:
    fruits.append(fruit) #Adds the fruit to the list
    print(fruits)
else:
    print('The fruit already exists in the list.')
#Exercises: Level 3
#Here we have a person dictionary. Feel free to modify it!
#        person={
 #   'first_name': 'Asabeneh',
 #   'last_name': 'Yetayeh',
 #   'age': 250,
 #   'country': 'Finland',
 #   'is_marred': True,
 #   'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 #   'address': {
  #      'street': 'Space street',
  #      'zipcode': '02210'
  #  }
  #  }
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
    'street': 'Space street',
    'zipcode': '02210'
    }
    }

 #* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(skills[middle_index])

#* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print('The person has Python skill.')
    else:
        print('The person does not have Python skill.')

#* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('unknown title')

#* If the person is married and if he lives in Finland, print the information in the following format:
#   Asabeneh Yetayeh lives in Finland. He is married.
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")