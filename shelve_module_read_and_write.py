import shelve
shelfFile=shelve.open('mydata')
cars = ['ferrari','benz','lexus','bugatti'] # use dictionaries so as enable the replace,add,delete features for flexibility.
shelfFile['cars']= cars
shelfFile.close() #necessary...you close every file your open/call.
#this program creates a .dat, .dir, .bak files.
#shelve module helps to add, save, edit and open program files. It helps to store your program's data to a file.
#the .dat, .dir, .bak files are stored in the program diretory. here its stored in the parent directory.