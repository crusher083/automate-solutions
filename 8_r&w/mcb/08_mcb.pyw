#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve
import pyperclip
import sys
mcb_shelf = shelve.open('mcb')
# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'del':
        if sys.argv[2] and sys.argv[2] in mcb_shelf:
            del mcb_shelf[sys.argv[2]]
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[2] not in mcb_shelf:
            print('This key doesn\'t exist')
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()

mcb_shelf.close()
