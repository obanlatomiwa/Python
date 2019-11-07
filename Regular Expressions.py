# using the re module...regular expressions becomes easy to code
import re
PhoneNumRegex= re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d\d)')
num= PhoneNumRegex.search('my number is 0812-234-5432')
print('Phone Number Found:' + num.group())   # prints all the regex by passing 0 into the math object group function
print('Phone Number Found:' + num.group(1))  # prints the part 1 regex seperated  by the parentheses by passing 1 into the math object group function
print('Phone Number Found:' + num.group(2))  # prints the part 1 regex seperated  by the parentheses by passing 2 into the math object group function
print('Phone Number Found:' + num.group(3))  #prints the part 1 regex seperated  by the parentheses by passing 3 into the math object group function
# you can use the groups() method to convert the regex groups into a tuple for re-use
num.groups()
CountryCode, TraceBackNum, ReturnNum= num.groups()
print(CountryCode)
print(TraceBackNum)
print(ReturnNum)

print("\nMatchiing multiple groups with the pipe")
# matchiing multiple groups with the pipe character to match one of many expressions ,it returns the first occurence
HeroRegex=re.compile(r'Batman|Superman')  # its case-sensitive
Hero1=HeroRegex.search('Batman and Superman, who is your favourite Hero') # batman found first ,therefore it prints batman
print("Hero Found:", Hero1.group())
Hero2=HeroRegex.search('Superman and Batman, who is your favourite Hero') # superman found first ,therefore it prints batman
print("Hero Found:", Hero2.group())

# There is a badass function python offers that surpasses the search() function...the findall()function. Its searches for all
# matches not just one like the search()

PhoneNumberRegex= re.compile(r'\d{4}-\d{3}-\d{4}')
print(PhoneNumberRegex.findall('My cell is 0817-245-6450, work: 0903-459-6856 mobile:0706-945-6754'))   # how to print
# with the findall()

# 3using a character class
characteregex= re.compile(r'[^aeiouAEIOU]')
print (characteregex.findall('Robocop is A fantasy. It\'s not REAL'))

# the dot is a wildcard character matches all things apart for a new line
universeregex=re.compile(r'.at')
print(universeregex.findall('the cat messed up the mat while chasing a rat down the stairs'))

# you csn also substitute strings
NameRegex = re.compile(r'Agent \w+')
print(NameRegex.sub('CENSORED', 'Agent Navida and Agent Tommy are now classified agents'))

