# Counts vowels in user input

sentence = input('Give me a sentence: ')
include_y = input('Is \'y\' considered a vowel? (y/n)')
vowels = ['a', 'e', 'i', 'o', 'u']
if include_y == 'y' or include_y == 'yes':
    vowels.append('y')
count = 0;
for v in vowels:
    count += sentence.count(v)
print('There are %d vowelss.' % count)
