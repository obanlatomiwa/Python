"""
 def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'
eggs = 'global'
bacon()
print(eggs) # prints 'global'
"""

# A PROGRAM FOR BASIC MATHEMATICS

 # def calculate_anything(a,b): print ("This program can add, subtract, multiply and divide any two values")

a=b = float()
         #print ("INPUT VALUE A") a= float (input())  print("INPUT VALUE B") b= float (input())

def add_anything (a,b):
    print ("The addition of %d and %d" %(a,b))
    return a + b
def subtract_anything (a,b):
    print("The subtraction of %d and  %d" % (a, b))
    return a- b
def multiply_anything (a,b):
    print("The multiplication of %d  and %d" % (a, b))
    return a * b
def divide_anything (a,b):
    print("The division of %d and %d" % (a, b))
    return a / b

add= add_anything (3,6)
subtract =subtract_anything (3,6)
multiply= multiply_anything (3,6)
divide= divide_anything (3,6)

print ("Addition=", add, "Subtraction=", subtract , "Multiplication=", multiply, "Division=", divide)




