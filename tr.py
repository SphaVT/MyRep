__author__ = '215000129'

def pascalRow(previousRow):
    x = 0
    nextRow = []
    for i in previousRow:
        y = x+i
        nextRow.append(y)
        x = i
    nextRow.append(1)
    return nextRow

def newList():
    numRow = int(input("Enter number of rows:\n"))
    while numRow < 1:
         numRow = int(input("Enter number of rows:\n"))

    newlist = []
    finelist = []
    for i in range(numRow):
        finelist.append(pascalRow(newlist))
        newlist = pascalRow(newlist)
    return finelist


print(newList())