# Counts vowels in input

sentence = input('Tell me a sentence: ')
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0;
for v in vowels:
    count += sentence.count(v)
print('vowels: %s' % count)