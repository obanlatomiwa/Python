""" Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu,
and cats'. But your function should be able to work with any list value passed to it.
say spam = ['apples', 'bananas', 'tofu', 'cats']"""

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight, my_age + my_height + my_weight))






