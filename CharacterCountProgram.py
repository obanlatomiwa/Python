import pprint
message = 'It is a bright, sunny and dry day, on the 2nd of Janauary, the Harmattan- I really hate it'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    pprint. pprint(count)
# pprint.pformat(count)
# If you want to obtain the prettified text as a
# string value instead of displaying it on the screen,
# call pprint.pformat() instead
