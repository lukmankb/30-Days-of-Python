#Create an empty dictionary called dog
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Rocky',
    'color': 'Black',
    'breed': 'Bulldog',
    'legs': 4,
    'age': 10
}
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = { 
    'first_name': 'Lukman',
    'last_name': 'Kabiru',
    'gender' : 'Male',
    'age': 22,
    'marital_status': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country': 'Nigeria',
    'city': 'Kebbi',
    'address': 'Makerar Gandu'
}

#Get the length of the student dictionary
length_of_student = len(student)
print('The length of the student dictionary is:', length_of_student)
#Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(skills)
print(type(skills))
#Modify the skills values by adding one or two skills
student['skills'].append('HTML') #Adds HTML to the list of skills
student['skills'].append('CSS')
print(student['skills'])
#Get the dictionary keys as a list
keys = student.keys()
print('The Student dictionary Keys: ',keys)
#Get the dictionary values as a list
values = student.values()
print('The student dictionary values: ',values)
#Change the dictionary to a list of tuples using items() method
dict_tuple = student.items()
print(dict_tuple)
#Delete one of the items in the dictionary
del student['address']
print(student)
#Delete one of the dictionaries
del dog

