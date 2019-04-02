# Saves you the trouble of manually writing page numbers when printing 2-sided
# if your computer can't communicate with the printer.
# Enter number of pages, print the first array, flip pages, print second array

import easygui as eg


def printpages(a):
    first_side = []
    second_side = []
    index1 = 1
    index2 = 2
    i = a
    while i > 0:
        first_side.append(index1)
        second_side.append(index2)
        index1 += 2
        index2 += 2
        i -= 2
    if a % 2 != 0:
        second_side = second_side[0:len(second_side)-1]
    return str(first_side) + "\n" + str(second_side)


amount = eg.enterbox("How many pages?: ")
eg.msgbox(printpages(int(amount)))
