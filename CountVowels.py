# Counts vowels in user supplied sentence
def do_count(usr_str):
    """Returns number of vowels"""
    include_y = input('Is \'y\' considered a vowel? (y/n)')
    vowels = ['a', 'e', 'i', 'o', 'u']
    if include_y == 'y' or include_y == 'yes':
        vowels.append('y')
    count = 0
    for v in vowels:
        count += usr_str.count(v)
    return count

if __name__ == "__main__":
    sentence = input('Give me a sentence: ')
    counted = do_count(sentence)
    print('There are {} vowels in "{}".'.format(counted, sentence))



