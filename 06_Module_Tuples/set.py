#Sets Exercises
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Sets Exercises: Level 1
#Find the length of the set it_companies
length_of_itcompanies = len(it_companies)
print('The length of the IT Companies Set is: ',length_of_itcompanies)
#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
new_itcompanies =('Instagram','Snapchat','Coursera')
it_companies.update(new_itcompanies)
print(f'Updated IT Companies: {it_companies}')
#Remove one of the companies from the set it_companies
removed_company = it_companies.pop()
print(f'Removed: {removed_company}\nNew IT Companies Set: {it_companies}')
#What is the difference between remove and discard
remove_snapchat = it_companies.remove('Snapchat')
print(it_companies)
discard_python = it_companies.discard('Python') #python does not exist in the set
print(it_companies)
#Sets Exercises: Level 2
#Join A and B
joined_sets = A.union(B)
print(f'Set A union Set B: {joined_sets}')
#Find A intersection B
a_intersect_b = A.intersection(B)
print('A intersection B: ',a_intersect_b)
#Is A subset of B
is_subset = A.issubset(B)
print('Is Set A subset of B? ',is_subset)
#Are A and B disjoint sets
is_disjoint = A.isdisjoint(B)
print(f'Are A and B disjoint? {is_disjoint}')
#Join A with B and B with A
A_with_B = A.union(B)
B_with_A = B.union(A)
print(f'A and B {A_with_B}')
print(f'B and A {B_with_A}')
#What is the symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B)
print('Symmetric Difference: ',symmetric_diff)
#Delete the sets completely
del A, B
#Sets Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print('Length of List(ages):',len(age))
print('Length of Set(ages):',len(age_st))
#Explain the difference between the following data types: string, list, tuple and set
'''
String: A sequence of characters used to represent text. e.g 'hello world'.
List: Collection of Items that is mutable(can be changed). it is defined with [].
Tuple: Immutable collection of items denoted by {}.
Set: Unordered collection of unique items defined with {} or set()
'''
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
unique_words = sentence.split()
unique_set = set(unique_words)
# Counting the number of unique words
num_unique_words = len(unique_set)
print(f'The number of unique words used in the sentence are: {num_unique_words}')
