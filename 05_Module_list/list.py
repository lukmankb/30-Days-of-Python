#Declare an empty list
empty_list = list()
#Declare a list with more than 5 items
school_items = ['Book','Pen','Eraser','Ruler','Protractor','Divider','Calculator']
#Find the length of your list
length_of_list = len(school_items)
print(length_of_list)
#Get the first item, the middle item and the last item of the list 
first_item = school_items[0]
middle_item = length_of_list // 2
last_item = school_items[-1]
print(first_item)
print(school_items[middle_item])
print(last_item)
#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Lukman',21,160,'Single','Makerar Gandu']
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
#Print the list using print()
print(it_companies)
#Print the number of companies in the list
number_of_companies = len(it_companies)
number = 'Number of Companies is: {}'.format(number_of_companies)
print(number)
#Print the first, middle and last company
first_middle_last = it_companies[0::3]
print(first_middle_last)
#Print the list after modifying one of the companies
it_companies[0] = 'Samsung'
print(it_companies)
#Add an IT company to it_companies
it_companies.append('Lenovo')
print(it_companies)
#Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Hp')
print(it_companies)
#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)
#Join the it_companies with a string '#;  '
join_list_string = '#; '.join(it_companies)
print(join_list_string)
#Check if a certain company exists in the it_companies list.
company_exists = 'Amazon' in it_companies
print(company_exists)
#Sort the list using sort() method
it_companies.sort()
print(it_companies)
#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
#Slice out the first 3 companies from the list
sliced_companies = it_companies[3:]
print(sliced_companies)
#Slice out the last 3 companies from the list
last_companies_sliced = it_companies[0:-3]
print(last_companies_sliced)
#Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
removed_middlie_item = it_companies[:middle_index] + it_companies[middle_index + 1:]
print(removed_middlie_item)
#Remove the first IT company from the list
it_companies.remove('Samsung')
print(it_companies)
#Remove the middle IT company or companies from the list
del it_companies[4]
print(it_companies)
#Remove the last IT company from the list
it_companies.pop()
print(it_companies)
#Remove all IT companies from the list
it_companies.clear()
print(it_companies)
#Destroy the IT companies list
del it_companies

#Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
copied_list = list(joined_list)
full_stack = copied_list
full_stack.insert(5, 'python')
full_stack.insert(6, 'SQL')
print(full_stack)
#The following is a list of 10 students ages:
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
minimum_age = min(ages)
maximum_age = max(ages)
print(f'The minimum age is: {minimum_age}\nThe maximum age is: {maximum_age}')
#Add the min age and the max age again to the list
ages.append(minimum_age)
ages.append(maximum_age)
print(ages)
#Find the median age (one middle item or two middle items divided by two)
sorted_ages = sorted(ages)
#print(sorted_ages)
length_of_ages = len(sorted_ages)
#median = (sorted_ages[5] + sorted_ages[6]) / 2
median = (sorted_ages[length_of_ages//2 - 1] + sorted_ages[length_of_ages//2]) / 2
print('The Median is: ', median)
#Find the average age (sum of all items divided by their number )
average_age = sum(ages) / length_of_ages
print('The average age is: ', average_age)
#Find the range of the ages (max minus min)
range_of_ages = maximum_age - minimum_age
print('The range is {}'.format(range_of_ages))
#Compare the value of (min - average) and (max - average), use abs() method
diff_min = abs(minimum_age - average_age)
diff_max = abs(maximum_age - average_age)
print(f'The difference  of Minimum and Average age is {diff_min}')
print(f'The value of Maximum and Average age is {diff_max}')
#Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
sorted_countries = sorted(countries)
len_of_countries = len(sorted_countries)
print('We have {} Countries in the list'.format(len_of_countries))
middle_country = len_of_countries // 2
print(f'The Middle Country is {sorted_countries[middle_country]}')
#Divide the countries list into two equal lists if it is even if not one more country for the first half.
print('Palestine' in countries)
firsthalf = len(countries) // 2
new_country = 'Palestine'
countries.insert(firsthalf, new_country)
print(countries)
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic_countries = countries2
print('Asian: ', china)
print('Transcontinental: ', russia)
print('North America: ', usa)
print('Scandinavian: ', scandic_countries)