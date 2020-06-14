#! python3
import re
import os


def search_files(regex, dirs):
    emails = []
    for f in os.listdir(dirs):
        if f.endswith(".txt"):
            textfile = open(os.path.join(dirs, f), 'r+')
            txt = textfile.read()
            result = regex.findall(txt)
            emails.extend(result)
    return emails


def print_results(results):
    for entry in results:
        print(entry)


def main():
    reg_mail = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @                 # @ symbol
    [a-zA-Z0-9.-]+    # domain name
    \.[a-zA-Z]{2,4} # dot-something
    )''', re.X)
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    emails = search_files(reg_mail, cur_dir)
    print_results(emails)
    k = input('Close?')


if __name__ == "__main__":
    main()
