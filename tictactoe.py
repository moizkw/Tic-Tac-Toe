# Single-player Tic Tac Toe (Human vs Computer) 
# Author: Moiz Kharodawala

def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('------------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

def isBoardFull(board):
    return board.count(' ') <= 1

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input("Please select a position to enter the X between 1 to 9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please type a number between 1 and 9')

        except:
            print('Please type a number')

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = [i for i in possibleMoves if i in [1 , 3 , 7 , 9]]
    if cornersOpen:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = [i for i in possibleMoves if i in [2,4,6,8]]
    if edgesOpen:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def userReference():
    print('For your reference, these are the position numbers:')
    print(' 1  |  2  | 3  ')
    print('---------------')
    print(' 4  |  5  |  6 ')
    print('---------------')
    print(' 7  |  8  |  9 \n')

def main():
    print("Welcome to the game!\n")
    userReference()
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Computer Wins\n")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('Computer placed an O on position' , move , ':')
                printBoard(board)
        else:
            print("\nYou Win!\n")
            break
    if isBoardFull(board):
        print("Tie game\n")

if __name__ == "__main__":
    while True:
        x = input("Do you want to play? (y/n): ")
        if x.lower() == 'y':
            board = [' ' for x in range(10)]
            print('--------------------')
            main()
        else:
            break
