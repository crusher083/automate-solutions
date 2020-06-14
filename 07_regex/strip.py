import re


def strip(*args):
    if len(args) == 1:
        r_strip = re.compile(r'''
                     (\s*)
                     (.*\S)
                     (\s*)
                     ''', re.X)
        new_str = r_strip.search(args[0]).group(2)
        return new_str
    elif len(args) == 2:
        r_strip = re.compile(fr'(.*?)?({args[1]})(.*)?', re.S | re. I)
        s = r_strip.search(args[0])
        try:
            new_str = s.group(1) + s.group(3)
            return new_str
        except AttributeError:
            return [args[0]]
