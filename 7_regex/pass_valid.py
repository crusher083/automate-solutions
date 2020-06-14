import re


def str_pass(password):
    reg_pass = re.compile(r'''
                     ^(?=.{8,})
                     (?=\D*\d)
                     (?=[^a-z]*[a-z])
                     (?=[^A-Z]*[A-Z])
                     (?=.*[@$!%*#?&])
                     .*$''', re.X | re.S)
    s = reg_pass.search(str(password))
    if s is not None:
        print('Super duper password!')
    else:
        print('Weak')
    try:
        return s.group()
    except AttributeError:
        pass
