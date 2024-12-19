#Tuple Exercises: Level 1
#Create an empty tuple
empty_tuple = tuple()
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Sani',)
sisters = ('Kubra', 'Prof')
#Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
#How many siblings do you have?
number_of_siblings = len(siblings)
print('Number of siblings: {}'.format(number_of_siblings))
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.insert(0, 'Baba')
siblings.insert(1, 'Mama')
family_members = tuple(siblings)
print(family_members)
#Tuple Exercises: Level 2
#Unpack siblings and parents from family_members
family_members = list(family_members)
father, mother, *siblings = family_members
print('Father: ', father)
print('Mother: ', mother)
print('Siblings: ', siblings)
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Mango', 'Banana', 'Apple')
vegetables = ('Tomato', 'Onion', 'Cabbage')
animal = ('Dog', 'Cat', 'Rat')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)
#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp[4])
#Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_tp[0:3]
print('The first three items are: ',first_three)
last_three = food_stuff_tp[-3:]
print('The last three items are: ', last_three)
#Delete the food_staff_tp tuple completely
del food_stuff_tp
#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Nigeria' in nordic_countries)
#Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print('Estonia is a Nordic Country: ', is_estonia_nordic)
#Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print('Iceland is a Nordic Country: ', is_iceland_nordic)
#nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')