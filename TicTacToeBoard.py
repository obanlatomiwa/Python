#TicTacToe Board Game a.k.a X and O
#Applying the dictionaries python data type
import pprint
theboard={'top-L':'', 'mid-L':'', 'low-L':'',
          'top-M':'', 'mid-M':'', 'low-M':'',
          'top-R':'', 'mid-R':'', 'low-R':''}

def printboard(board):
    print(board['top-L']+' | '+ board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board ['mid-L']+ ' | ' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + ' | ' + board['low-M'] + '|'+ board['low-R'])

turn='X'
for i in range(9):
    printboard (theboard)
    print("Turn for", turn, 'to move for a white space?')
    move= input()
    theboard[move]= turn
    if turn == 'X':
        turn='O'
    else:
        turn='X'

printboard(theboard)