#I am using the string justification functions here: rjust(), ljust(), center()
def printpicnic (itemsdict, leftwidth, rightwidth):
    print ('PICNIC ITEMS ' .center (leftwidth + rightwidth, '-'))

    for k,v in itemsdict.items():
        print(k.ljust(leftwidth,'.') + str(v).rjust(rightwidth))

picnicitems={'sandwiches':4, 'apples':'12', 'cups': 4,'cookies':8000}
printpicnic(picnicitems,12,5)
printpicnic(picnicitems,20,6)

import pyperclip
pyperclip.copy('Hello World')
pyperclip.paste()

