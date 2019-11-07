#! python3

import os
import io
# os.makedirs('C:\\Users\\tomiwa obanla\\Desktop\\py\\py1\\py2') # creates new folders
readFile = open('C:\\Users\\tomiwa obanla\\Desktop\\pytexttest.txt', 'r') #open a file..its creates a file object readFile
fileRead = readFile.read() #read a file
print(fileRead)
readFile.close()

