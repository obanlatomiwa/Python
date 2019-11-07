while True:
    print ('Enter your age:')
    age=input()
    if age.isdecimal():
        break
    print ('Enter your age as an integer!')

while True:
    print ('Enter your password')
    password=input()
    if password.isalnum():
        break
    print('Try again, Your password must contain only alphabets and numbers')
