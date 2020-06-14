#! python3
import re


def words_list(regex):
    with open('text.txt', 'r+') as f:
        txt = f.read()
        words = re.findall(regex, txt)
    return words, txt


def words_substitution(words):
    for i in range(len(words)):
        words[i] = input(f'Enter a substitute for {words[i].lower()}:\n')
    return words


def text_replace(regex, words, text):
    start_p = [len(text)]
    for m in re.finditer(regex, text):
        start_p.insert(-1, m.start())
    new_text = ''
    for w in range(len(words)):
        after_part = re.sub(regex, words[w],
                            text[start_p[w]:start_p[w + 1]], 1)
        new_text += after_part
    return text[:start_p[0]] + new_text


def re_text_save(txt):
    name = input('Name new file:\n')
    re_text = open(f'{name}.txt', 'w')
    re_text.write(txt)
    re_text.close()


def main():
    regex = re.compile(r'adjective|noun|verb|adverb', re.I)
    word_list, txt = words_list(regex)
    new_word_list = words_substitution(word_list)
    new_text = text_replace(regex, new_word_list, txt)
    print(new_text)
    re_text_save(new_text)


if __name__ == '__main__':
    main()
