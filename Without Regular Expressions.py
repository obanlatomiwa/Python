# Finding patterns without regular expressions
# creating a function to check if a string matches this pattern, returning either true or false

def isphonenumber(text):
    if len(text)!=13:
        return False
    for i in range(0,3):
        if not text[i].isdecimal:
            return False
    if text[4]!= '-':
        return False
    for i in range (5,7):
        if not text[i].isdecimal:
            return False
    if text[8]!= '-':
        return False
    for i in range(9, 12):
        if not text[i].isdecimal:
            return False
    return True

#print("is 0817-827-3457 a phone number:")
#print(isphonenumber('0817-827-3457'))

#For a larger string
message="call me at 0817-234-9678 or through my office cell at 0812-995-9687"
print(len(message))
for i in range(len(message)):
    chunk = message[i:i+12]
    if isphonenumber(chunk):
        print('phone number found:'+ chunk)
print('Done')