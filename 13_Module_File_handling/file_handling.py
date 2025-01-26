#Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
def count_lines_and_words(filename):
    from pathlib import Path
    file = Path(filename)
    if file.exists():
        with open(file, 'r') as f:
            content = f.read()
            lines = content.splitlines()
            words = content.split()
            return {'lines': len(lines), 'words': len(words)}
    else:
        return 'The file does not exist'
print(count_lines_and_words('./30-days-of-python/datas/obama_speech.txt'))
print(count_lines_and_words('./30-days-of-python/datas/michelle_obama_speech.txt'))
print(count_lines_and_words('./30-days-of-python/datas/donald_speech.txt'))
print(count_lines_and_words('./30-days-of-python/datas/melina_trump_speech.txt'))
#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(filename, number):
    import json
    from collections import Counter
    with open(filename, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        languages = []
        for country in data:
            languages.extend(country['languages'])
        languages_count = Counter(languages)
        return languages_count.most_common(number)
for language in most_spoken_languages('./30-days-of-python/datas/countries_data.json', 10):
    print(language)
#print(most_spoken_languages('./30-days-of-python/datas/countries_data.json', 10))

# Your output should look like this
#print(most_spoken_languages(filename='./data/countries_data.json', 10))
#[(91, 'English'),
#(45, 'French'),
#(25, 'Arabic'),
#(24, 'Spanish'),
#(9, 'Russian'),
#(9, 'Portuguese'),
#(8, 'Dutch'),
#(7, 'German'),
#(5, 'Chinese'),
#(4, 'Swahili'),
#(4, 'Serbian')]

# Your output should look like this
#print(most_spoken_languages(filename='./data/countries_data.json', 3))
#[(91, 'English'),
#(45, 'French'),
#(25, 'Arabic')]
#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(filename, number):
    import json
    with open (filename, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        data.sort(key = lambda x: x['population'], reverse = True)
        return [{'country': country['name'], 'population': country['population']} for country in data[:number]]
for country in most_populated_countries('./30-days-of-python/datas/countries_data.json', 10):
    print(country)    
#print(most_populated_countries('./30-days-of-python/datas/countries_data.json', 10))

# Your output should look like this
#print(most_populated_countries(filename='./data/countries_data.json', 10))
'''
[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000},
{'country': 'Indonesia', 'population': 258705000},
{'country': 'Brazil', 'population': 206135893},
{'country': 'Pakistan', 'population': 194125062},
{'country': 'Nigeria', 'population': 186988000},
{'country': 'Bangladesh', 'population': 161006790},
{'country': 'Russian Federation', 'population': 146599183},
{'country': 'Japan', 'population': 126960000}
]
'''
# Your output should look like this

#print(most_populated_countries(filename='./data/countries_data.json', 3))
#[
#{'country': 'China', 'population': 1377422166},
#{'country': 'India', 'population': 1295210000},
#{'country': 'United States of America', 'population': 323947000}
#]
#Exercises: Level 2
#Extract all incoming email addresses as a list from the email_exchange_big.txt file.
def extract_emails(filename):
    import re
    with open(filename, 'r') as f:
        content = f.read()
        return re.findall(r'[\w\.-]+@[\w\.-]+', content)
#print(extract_emails('./30-days-of-python/datas/email_exchange_big.txt'))

#Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
# Your output should look like this
#    print(find_most_common_words('sample.txt', 10))
#    [(10, 'the'),
#    (8, 'be'),
#    (6, 'to'),
#    (6, 'of'),
#    (5, 'and'),
#    (4, 'a'),
#    (4, 'in'),
#    (3, 'that'),
#    (2, 'have'),
#    (2, 'I')]
def find_most_common_words(filename, number):
    import re
    from collections import Counter
    with open (filename, 'r') as f:
        content = f.read().lower()
        words = re.findall(r'\b\w+\b', content)
        stop_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
        words = [word for word in words if word not in stop_words]
        words_count = Counter(words)
        return words_count.most_common(number)
for word in find_most_common_words('./30-days-of-python/datas/donald_speech.txt', 10):
    print(word)
#    # Your output should look like this
#    print(find_most_common_words('sample.txt', 5))
#
#    [(10, 'the'),
#    (8, 'be'),
#    (6, 'to'),
#    (6, 'of'),
#    (5, 'and')]
for word in find_most_common_words('./30-days-of-python/datas/donald_speech.txt', 5):
    print(word)

#Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
def find_most_frequent_words(filename, number):
    import re
    from collections import Counter
    with open (filename, 'r') as f:
        content = f.read().lower()
        words = re.findall(r'\b\w+\b', content)
        stop_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
        words = [word for word in words if word not in stop_words]
        words_count = Counter(words)
        return words_count.most_common(number)
#Find the 10 most repeated words in the romeo_and_juliet.txt
def find_most_repeated_words(filename, number):
    import re
    from collections import Counter
    with open (filename, 'r') as f:
        content = f.read().lower()
        words = re.findall(r'\b\w+\b', content)
        stop_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
        words = [word for word in words if word not in stop_words]
        words_count = Counter(words)
        return words_count.most_common(number)
for word in find_most_repeated_words('./30-days-of-python/datas/romeo_and_juliet.txt', 10):
    print(word)
