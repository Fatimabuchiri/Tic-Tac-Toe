#Fatima Anwar Ahmed
#creating a 3x3 board
board = {
    1:' ',2:' ',3:' ',
    4:' ',5:' ',6:' ',
    7:' ',8:' ',9:' '
}
#creating a board with numbered position
board_positions = {
    1:'1',2:'2',3:'3',
    4:'4',5:'5',6:'6',
    7:'7',8:'8',9:'9'
}
#printing the board
def print_board(board):
    print(board[1]+ '|' +board[2]+ '|' +board[3])
    print('-----')
    print(board[4]+ '|' +board[5]+ '|' +board[6])
    print('-----')
    print(board[7]+ '|' +board[8]+ '|' +board[9])
    print("\n")


#check if the place is free
def check_free_place(position):
    if board[position] == ' ':
        return True
    else:
        return False
#checking for a tie
def tie_check():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

#checking for the win
#we need to check for rows, columns, and diagonals wins
def win_check():
    #rows wins
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    #columns wins
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    #diagonals wins
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

# To check which player wins 'X' or 'O'
def check_which_player_won(player):
    #rows wins
    if (board[1] == board[2] and board[1] == board[3] and board[1] == player ):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == player):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == player):
        return True
    #columns wins
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == player):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == player):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == player):
        return True
    #diagonals wins
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == player):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == player):
        return True
    else:
        return False
#inserting the letter
def insert_letter(letter,position):
    if check_free_place(position):
        board[position] = letter
        print_board(board)
        if(tie_check()):
            print("Tie!")
            exit()
        if(win_check()):
            if letter == 'X':
             print("Player X wins!")
             exit()
            else:
                print("Player O wins!")
                exit()
        return

    else:
        print("position already taken!")
        position = int(input("Enter another position:"))
        insert_letter(letter,position)
        return

# Asssign the letter 'X' or 'O' to the human and computer player
Human = input("Choose between 'X' and 'O' : ")
if Human == 'X':
    bot = 'O'
else:
    bot = 'X'
Start = input("Do you want to play first ('Yes' or 'No'): ")

def print_positions(board_positions):
    print("Positions are:")
    print(board_positions[1]+ '|' +board_positions[2]+ '|' +board_positions[3])
    print('-----')
    print(board_positions[4]+ '|' +board_positions[5]+ '|' +board_positions[6])
    print('-----')
    print(board_positions[7]+ '|' +board_positions[8]+ '|' +board_positions[9])
    print("\n")
print_positions(board_positions)
def Human_player():
    position = int(input("Enter the position for " + Human + ":"))
    insert_letter(Human,position)
    return

#the function for the computer to maximize the move and take the best step
def computer_player():
    Best_score = -1000
    Best_move = 0

    for key in board.keys():
        if(board[key] == ' '):
            board[key] = bot
            score = minimax(board,False)
            board[key] = ' '
            if(score > Best_score):
                Best_score = score
                Best_move = key
    insert_letter(bot,Best_move)
    return

#minimax algorithm
def minimax(board, isMaximizing):
    if check_which_player_won(bot):
        return 1
    elif check_which_player_won(Human):
        return -1
    elif tie_check():
        return 0
    #maximize for the computer
    if isMaximizing:
        Best_score = -1000

        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, False)
                board[key] = ' '
                if (score > Best_score):
                    Best_score = score
        return Best_score
#minimize for the human
    else:
        Best_score = 1000

        for key in board.keys():
            if (board[key] == ' '):
                board[key] = Human
                score = minimax(board, True)
                board[key] = ' '
                if (score < Best_score):
                    Best_score = score
        return Best_score

#to start the game
while not win_check():
    if Start == 'No':
     computer_player()
     Human_player()
    else:
        Human_player()
        computer_player()
