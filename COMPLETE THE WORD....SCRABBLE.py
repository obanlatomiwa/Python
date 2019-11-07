#! python3

# gets input letters
# gets the number of letters to form your choosen word
# do the permutation
# print out the output

from pprint import pprint-
from itertools import permutations

print('Enter the Number of Letters')
n = int(input())
print('Input Your Random Letters')
inputLetters = []                                          # fix the bug that allows 2 letters for a memory box in the array
for i in range(n):
    letters = input()
    inputLetters.append(letters)
    print(inputLetters)

print('Numbers of Letters for the Word that is to be formed')
numberOfLettersCombined = int(input())

# TIME FOR THE PERMUTATIONS
pprint(list(permutations(inputLetters, numberOfLettersCombined)))


#finalResults = permutations([inputLetters], numberOfLettersCombined)
#print(finalResults)
#for [i] in list(finalResults):
#   print(i)





