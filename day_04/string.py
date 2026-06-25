string_1 = 'Thirty'
string_2 = 'Days'
string_3 = 'of'
string_4 = 'Python'
string = string_1 + ' ' + string_2 + ' ' + string_3 + ' ' + string_4
print(string)

str_1 = 'Coding'
str_2 = 'For'
str_3 = 'All'
string = str_1 + ' ' + str_2 + ' ' + str_3  
print(string)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
first_word = company[0:6]
print(first_word)
print(company[0])
first_word_a = company[0:2]
print(first_word_a)
print(company.find('Coding'))
company_new = company.replace('Coding', 'Python')
print(company_new)
print(company.split())

string = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(string.split(', '))

acronym_1 = 'Coding For All'
print(acronym_1[0] + acronym_1[7] + acronym_1[11])
acronym_2 = 'Python For Everyone'
print(acronym_2[0] + acronym_2[7] + acronym_2[11])

acronym_a = company.split()
print(acronym_a[0][0] + acronym_a[1][0] + acronym_a[2][0])
acronym_b = acronym_2.split()
print(acronym_b[0][0] + acronym_b[1][0] + acronym_b[2][0])

print(company.index('C'))
print(company.index('F'))

coding = 'Coding For All People'
print(coding.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rfind('because'))
print(sentence.index('because'))

phrase = 'because'
slice = sentence[sentence.find(phrase):sentence.rfind(phrase) + len(phrase)]
print(slice)

phrase = 'because because because'
slice = sentence[sentence.find(phrase):sentence.find(phrase) + len(phrase)]
print(slice)

print(company.startswith('Coding'))
print(company.endswith('Coding'))

space_string = '   Coding For All   '
print(space_string.strip())

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(', '.join(libraries))

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

print('I\nam\nenjoying\nthis\nchallenge')

line_1 = 'I am enjoying this challenge.'
line_2 = 'I just wonder what is next.'
print(line_1 + '\n' + line_2)

print('Name\t\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} square units.')
print('The area of a circle with radius {} is {} square units.'.format(radius, area))

a= 8
b= 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

print('{0} + {1} = {2}'.format(a, b, a + b))