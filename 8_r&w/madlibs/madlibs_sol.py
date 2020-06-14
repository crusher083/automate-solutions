#! python3
import re


def words_replace(regex):
    with open('text.txt', 'r+') as f:
        text = f.read()
    while True:
        replace = regex.search(text)
        if replace is None:
            break
        print(f'Enter a substitute for {replace.group().lower()}')
        i = input()
        new_text = regex.sub(i, text, 1)
    return new_text


def re_text_save(text):
    name = input('Name new file:\n')
    re_text = open(f'{name}.txt', 'w')
    re_text.write(text)
    re_text.close()


def main():
    regex = re.compile(r'ADJECTIVE | NOUN | VERB | ADVERB')
    new_text = words_replace(regex)
    print(new_text)
    re_text_save(new_text)


if __name__ == '__main__':
    main()
