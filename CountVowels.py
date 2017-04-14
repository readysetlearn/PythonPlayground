# Counts vowels in user supplied sentences

def main():
    total_sentences = total_vowels = 0;
    while True:
        sentence = input('Give me a sentence or type exit to exit: ')
        if sentence == 'exit':
            break
        counted = do_count(sentence)
        print('There are {} vowels in "{}".'.format(counted, sentence))
        total_sentences += 1
        total_vowels += counted
    print('Total number of sentences processed: {}. Total vowels: {}.'.format(total_sentences, total_vowels))


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
    main()
