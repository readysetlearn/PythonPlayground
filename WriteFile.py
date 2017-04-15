# Creates a file and fill with random text. Counts the vowels.
import loremipsum
import os
from CountVowels import do_count


def main():
    print("Started")
    file_name = 'rnd_txt.txt'
    text = create_file(file_name)
    print('Number of vowels: {}'.format(do_count(text)))
    os.startfile(file_name)
    delete_file(file_name)
    print("Finished")

def create_file(name):
    "creates file with random text"
    file = open(name, 'w')
    text = list(loremipsum.generate_paragraphs(1, True))[0][2]
    file.write(text)
    file.close()
    return text


def delete_file(name):
    """confirms with user before delete file"""
    input('press enter to delete file...')
    os.remove(name)


if __name__ == "__main__":
    main()
