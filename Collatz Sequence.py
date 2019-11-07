def collatz(number):
    if number % 2 == 0:     # checks if the number is even
        print(number // 2)
    elif number % 2 == 1:   # checks if the number is odd
        print(number)
        return 3*number+1


number = int(input())
for number in range(1, 100, 2):
    collatz(number)

