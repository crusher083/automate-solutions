def tablePrinter(nestlst):
    wordlength = []
    for sub in nestlst:
        for word in sub:
            wordlength.append(len(word))
            colWidth = max(wordlength)
    for y in range(len(sub)):
        for x in range(len(nestlst)):
            print(nestlst[x][y].rjust(colWidth), end='')
        print()
