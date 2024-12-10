print('Thirty ' + 'Days ' + 'of ' + ' Python')
print('Coding ', 'for ', 'All')
company = 'Coding for All'
print(company)
#Print the length of the company string using len() method and print().
print(len(company))
#Change all the characters to uppercase letters using upper() method.
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print('coding for all'.capitalize())
print('coding for all'.title())
print('coding for all'.swapcase())
#Cut(slice) out the first word of Coding For All string.
word = 'Coding For All'
first_word = word[1:20]
print(first_word)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(word.find('Coding'))
#Replace the word coding in the string 'Coding For All' to Python.
print(word.replace('Coding', 'python'))
#Change Python for Everyone to Python for All using the replace method or other methods.
py_word = 'Python for Everyone'
print(py_word.replace('Everyone', 'All'))
#Split the string 'Coding For All' using space as the separator (split()) .
print(word.split(' '))
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
word_split = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(word_split.split(', '))
#What is the character at index 0 in the string Coding For All.
print(word[0])
#What is the last index of the string Coding For All.
print(word[-1])
#What character is at index 10 in "Coding For All" string.
print(word[10])
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'
acronym = ''.join([abbr[0].upper() for abbr in phrase.split()])
print(acronym)
#Create an acronym or an abbreviation for the name 'Coding For All'.
acronym = ''.join([abbr[0].upper() for abbr in word.split()])
print(acronym)
#Use index to determine the position of the first occurrence of C in Coding For All.
print(word.index('C'))
#Use index to determine the position of the first occurrence of F in Coding For All.
print(word.index('F'))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
new_word = "Coding For All People"
print(new_word.rfind('l'))
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
because_position = sentence.index('because')
print(because_position)
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
because_position = sentence.rindex('because')
print(because_position)
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_because = sentence[31:54]
print(slice_because)
#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = sentence.find('because')
print(first_occurrence)
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(slice_because)
#Does ''Coding For All' start with a substring Coding?
print(word.startswith('Coding'))
#Does 'Coding For All' end with a substring coding?
print(word.endswith('All'))
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
trail_removal = '   Coding For All      '.strip()
print(trail_removal)
#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
identifier1 = '30DaysOfPython'
identifier2 = 'thirty_days_of_python'
print(identifier1.isidentifier())
print(identifier2.isidentifier())
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
py_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
py_lib_link = '# '.join(py_libraries)
print(py_lib_link)
#Use the new line escape sequence to separate the following sentences.
sentence1 = 'I am enjoying this challenge.\nI just wonder what is next.'
print(sentence1)
tab_sequence1 = 'Name\tAge\tCountry\tCity'
tab_sequence2 = 'Asabeneh\t250\tFinland\tHelsinki'
print(tab_sequence1)
print(tab_sequence2)
#Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of a circle with radius {} is {} meters square.'.format(radius, area)
print(formated_string)
#Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
num_1, num_2 = 8, 6
print('{} + {} = {}'.format(num_1, num_2, num_1 + num_2))
print('{} - {} = {}'.format(num_1, num_2, num_1 - num_2))
print('{} * {} = {}'.format(num_1, num_2, num_1 * num_2))
print('{} / {} = {}'.format(num_1, num_2, round(num_1 / num_2, 2)))
print('{} % {} = {}'.format(num_1, num_2, num_1 % num_2))
print('{} // {} = {}'.format(num_1, num_2, num_1 // num_2))
print('{} ** {} = {}'.format(num_1, num_2, num_1 ** num_2))