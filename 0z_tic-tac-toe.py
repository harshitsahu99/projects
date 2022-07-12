#TIC TAC TOE
#First Player is x


print('\t\t\t\tFirst Player Will Be x\n\n')
board=['-','-','-',
       '-','-','-',
       '-','-','-']
currentplayer='x'
winner=None
gamerunning=True

#print board
def printboard(board):
    print("\t\t\t\t\t" + board[0] + "|" + board[1] + "|" + board[2])
    print('\t\t\t\t\t-----')
    print("\t\t\t\t\t" + board[3] + "|" + board[4] + "|" + board[5])
    print('\t\t\t\t\t-----')
    print("\t\t\t\t\t" + board[6] + "|" + board[7] + "|" + board[8] + "\n\n")   

#take player input
def playerinput(board):
    inp=int(input('\t\t\t\tEnter Value:(1-9)\n\n'))
    if board[inp-1]=="-":
        board[inp-1] = currentplayer
    else:
        print('Invalid!')
#check win or tie
def checkhor(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]!= "-":
        winner=board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!= "-":
        winner=board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!= "-":
        winner=board[6]
        return True

def checkver(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!= "-":
        winner=board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!= "-":
        winner=board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!= "-":
        winner=board[2]
        return True

def checkdig(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!= "-":
        winner=board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!= "-":
        winner=board[0]
        return True

def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print('KHICHDI PAK GYI...!!!!!')
        gamerunning = False

def checkwin(board):
    global gamerunning
    if checkhor(board):
        printboard(board)
        print(f"The Winner is {winner}!")
        gamerunning = False

    elif checkver(board):
        printboard(board)
        print(f"The Winner is {winner}!")
        gamerunning = False

    elif checkdig(board):
        printboard(board)
        print(f"The Winner is {winner}!")
        gamerunning = False
        
#switch the player
def switchplayer():
    global currentplayer
    if currentplayer=="x":
        currentplayer="o"
    else:
        currentplayer="x"

#check again
while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin(board)
    checktie(board)
    switchplayer()
    
