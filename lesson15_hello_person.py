# Lesson 15
def hello(name, lang):
    greetings = {
        'English': 'Hello',
        'Spanish': 'Hola',
        'French': 'Bonjour',
    }
    msg = f'{greetings[lang]} {name}'
    print(msg)


if __name__ == '__main__':
    # The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv . The argparse module also automatically generates help and usage messages.
    # https://docs.python.org/3/library/argparse.html
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalized greeting.')
    parser.add_argument('-n', '--name', metavar='name',
                        required=True, help='The name of the person to greet.')
    parser.add_argument('-l', '--lang', metavar='language',
                        required=True, choices=['English', 'Spanish', 'French'], help='The language of the greeting.')

    args = parser.parse_args()

    hello(args.name, args.lang)
    # in terminal run: py lesson15_hello_person.py -n "Art" -l "French"
