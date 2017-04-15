# Creates a file and fills with random text
import loremipsum


def main():
    print("Started")
    rnd_str = loremipsum.generate_sentence(True)
    print(rnd_str[2])
    print("Finished")



if __name__ == "__main__":
    main()
