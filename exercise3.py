#icsd16007, Antonopoulos Georgios

#arithmish pinaka

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' , '4': ' ' , '5': ' ' ,
            '6': ' ' , '7': ' ' , '8': ' ' , '9': ' ' , '10': ' ' ,
            '11': ' ' , '12': ' ' , '13': ' ' , '14': ' ' , '15': ' ' ,
            '16': ' ' , '17': ' ' , '18': ' ' , '19': ' ' , '20': ' ' ,
            '21': ' ' , '22': ' ' , '23': ' ' , '24': ' ' , '25': ' '  }

board_keys = []

for key in theBoard:
    board_keys.append(key)

#gia na kanoume print ton pinaka kathe fora meta apo kathe kinhsh me sunarthsh poy ftiaxnoyme pio katw 

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + '|' + board['4'] + '|' + board['5'])
    print('-+-+-+-+-')
    print(board['6'] + '|' + board['7'] + '|' + board['8'] + '|' + board['9'] + '|' + board['10'])
    print('-+-+-+-+-')
    print(board['11'] + '|' + board['12'] + '|' + board['13'] + '|' + board['14'] + '|' + board['15'])
    print('-+-+-+-+-')
    print(board['16'] + '|' + board['17'] + '|' + board['18'] + '|' + board['19'] + '|' + board['20'])
    print('-+-+-+-+-')
    print(board['21'] + '|' + board['22'] + '|' + board['23'] + '|' + board['24'] + '|' + board['25'])
   


def game():

    turn = 'X'
    count = 0


    for i in range(26):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Elegxos an exei nikhsei o paixths me ta X h o paixths me ta 0 me olous tous pithanous sunduasmous
        # count >=9 giati 5liza sthn kaluterh periptwsh tha mporei na ginei apo ton ena paikth meta apo 9 gurous
        if count >= 9:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] == theBoard['4'] == theBoard['5'] != ' ': # 1h grammh
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['6'] == theBoard['7'] == theBoard['8'] == theBoard['9'] == theBoard['10'] != ' ': # 2h grammh
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['11'] == theBoard['12'] == theBoard['13'] == theBoard['14'] == theBoard['15'] != ' ': # 3h grammh 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['16'] == theBoard['17'] == theBoard['18'] == theBoard['19'] == theBoard['20'] != ' ': # 4h grammh 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['21'] == theBoard['22'] == theBoard['23'] == theBoard['24'] == theBoard['25'] != ' ': # 5h grammh
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['6'] == theBoard['11'] == theBoard['16'] == theBoard['21'] != ' ': # 1h sthlh
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['2'] == theBoard['7'] == theBoard['12'] == theBoard['17'] == theBoard['22'] != ' ': # 2h sthlh 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['3'] == theBoard['8'] == theBoard['13'] == theBoard['18'] == theBoard['23'] != ' ': # 3h sthlh 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['4'] == theBoard['9'] == theBoard['14'] == theBoard['19'] == theBoard['24'] != ' ': # 4h sthlh
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['5'] == theBoard['10'] == theBoard['15'] == theBoard['20'] == theBoard['25'] != ' ': # 5h sthlh
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['1'] == theBoard['7'] == theBoard['13'] == theBoard['19'] == theBoard['25'] != ' ': # diagwnios 1
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['5'] == theBoard['9'] == theBoard['13'] == theBoard['17'] == theBoard['21'] != ' ': # diagwnios 2
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # Isopalia an kaneis paixths den exei kanei 5liza meta apo tis 25 kinhseis.
        if count == 25:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Gia thn allagh tou paixth meta apo kathe egkurh kinhsh
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    #epilogh epankkinhshs
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" :  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()