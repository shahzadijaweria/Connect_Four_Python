import random
import Node
import time
import tkinter
import sys
import math
import numpy as np
from scipy.signal import savgol_filter

top = tkinter.Tk()
top.title("Connect Four")

gameSize = 7
difficultyLevel = 'Easy'
winner = 'None'
turn = 'max'
Window_length=4
empty=0

def changeTurn():
    global turn
    if turn == 'min':
        turn = 'max'
    elif turn == 'max':
        turn = 'min'


class Game:
    button = [[None] * gameSize for _ in range(gameSize)]

    def __init__(self):
        self.root = Node.Node()

    def playerTurn(self,row, col, val):

        self.root.setValue(row, col, val)
        
        ##self.root.print()



# player play function
    def onButtonPress(self, i, j):
        global winner
        if turn == 'min':
            while self.root.array[i][j] == 0 and i < gameSize - 1:
                i += 1
            if self.root.array[i][j] != 0:
                i -= 1
            self.playerTurn(i, j, -1)

        if self.checkState() == 4:
            winner = turn

        changeTurn()
        self.gameStates()
        self.createGUI()
        return

    def gamePlay(self):
        global winner
        self.gameStates()
        while winner == 'None':
            self.createGUI()

    def checkDiagonal(self, i, j, count, val):
        row = i
        col = j
        for k in range(4):
            if row < gameSize and col < gameSize:
                if self.root.array[row][col] == val:
                    count += 1
                    row += 1
                    col += 1
                if count == 4:
                    return count
        return 0

    def checkHorizontal(self, count, val):
        for i in range(gameSize):
            count = 0
            for j in range(gameSize):
                if self.root.array[i][j] == val:
                    count += 1
                    if count == 4:
                        return count
        return 0

    def checkVertical(self, count, val):
        for i in range(gameSize):
            count = 0
            for j in range(gameSize):
                if self.root.array[j][i] == val:
                    count += 1
                    if count == 4:
                        return count
        return 0

    def checkState(self):
        count = 0
        if turn == 'max':
            ##check horizontally
            count = self.checkHorizontal(count, 1)
            if count == 4:
                return count
            ##check vertically
            count = self.checkVertical(count, 1)
            if count == 4:
                return count
            ##check diagonally right
            for i in range(gameSize):
                count = 0
                for j in range(gameSize):
                    count = self.checkDiagonal(i, j, count, 1)
                    if count == 4:
                        return count
            ##check diagonally right
            for i in range(gameSize):
                count = 0
                for j in range(gameSize - 1, 0, -1):
                    count = self.checkDiagonal(i, j, count, 1)
                    if count == 4:
                        return count
        elif turn == 'min':
            ##check horizontally
            count = self.checkHorizontal(count, -1)
            if count == 4:
                return count
            ##check vertically
            count = self.checkVertical(count, -1)
            if count == 4:
                return count
            ##check diagonally right
            for i in range(gameSize):
                count = 0
                for j in range(gameSize):
                    count = self.checkDiagonal(i, j, count, -1)
                    if count == 4:
                        return count
            ##check diagonally right
            for i in range(gameSize):
                count = 0
                for j in range(gameSize - 1, 0, -1):
                    count = self.checkDiagonal(i, j, count, -1)
                    if count == 4:
                        return count
        return 0

    def colour(self, i, j):
        if self.root.array[i][j] == -1:
            self.button[i][j].config(bg='green')
        elif self.root.array[i][j] == 1:
            self.button[i][j].config(bg='red')
        else:
            self.button[i][j].config(bg='white')


    def createGUI(self):
        for i in range(gameSize):
            for j in range(gameSize):
                if winner == 'min':
                    print('YOU WON!!')
                    time.sleep(5)
                    sys.exit()
                elif winner == 'max':
                    print('YOU LOST!!')
                    time.sleep(5)
                    sys.exit()
                self.button[i][j] = tkinter.Button(top, text=self.root.array[i][j], command=lambda row=i, column=j: self.onButtonPress(row, column), width=4, height=3)
                self.colour(i, j)
                self.button[i][j].grid(row=i, column=j)

        top.mainloop()


    
    def is_valid_loc(self,col):
        return self.root.array[gameSize-1][gameSize-1]==0

    def get_next_open_row(self,col):
        i=0
        for i in range(gameSize-1):
            if self.root.array[i][col]==0:
                return i

    def get_valid_loc(self):
        valid_loc=[]
        j=0
        for j in range(gameSize-1):
            if self.is_valid_loc(j):
                valid_loc.append(j)
        return valid_loc


    def is_terminal_node(self,game_size):
        if winner=='min' or winner=='max' or len(self.get_valid_loc())==0:
            return True
        return False

     #def score_pos(self,turn):
    def score_pos(self):
        score=0
        i=0
        row_array = ["0", "1", "2"]
       
        for i in range(gameSize-1):
            y = ''.join(row_array) # converting list into string
            z = int(y)
            row_array=[int (j) for j in list(self.root.array[i:])]
        for k in range((gameSize-1)-3):
            window = row_array[k:k+ Window_length]
            if window.count(turn)==4:
                score+=100
            elif window.count(turn)==3  and window.count(empty)==1:
                score+=10

        return score





    def minMax(self, array, depth, maxPlayer):
        valid_loc= self.get_valid_loc()
        is_terminal= self.is_terminal_node(gameSize)
        if depth==0 or is_terminal:
            if is_terminal:
               if winner=='max':
                   return (None,1000000000000000)
               elif winner =='min':
                   return (None,-1000000000000000)
               else:     # game over
                   return (None,0)
            else:     #if depth is 0
                return (None,self.score_pos)
                #return (None,self.score_pos('max'))

        if maxPlayer:          # computer
            value= - math.inf     # min value set
            column= random.choice(valid_loc)        # best col
            for col in valid_loc:
                row= self.get_next_open_row(col)
                board_copy=self.root.array.copy()
                self.playerTurn(row,col,1)         # for comp
                new_score = self.minMax(board_copy,depth-1,False)[1]        # 1st index

                if new_score > value :
                    column=col
                    value = new_score

                return column,value

        else:          # human
            value=math.inf     # max value set
            column= random.choice(valid_loc)        # best col
            for col in valid_loc:
                row= self.get_next_open_row(col)
                board_copy=self.root.array.copy()
                self. playerTurn(row,col,-1)         # for human
                new_score = self.minMax (board_copy,depth-1,True)[1]     #new_score=min(value,minMax(board_copy,depth-1,True))
                
                #if new_score < value :
                column=col
                value = new_score

                

                return column,value


     # computer play function
    def gameStates(self):
        global winner
        #row = random.randrange(gameSize)
       # col = random.randrange(gameSize
        col , minimax_score = self.minMax(self.root.array,2,True)
        row=self.get_next_open_row(col)
        while self.root.array[row][col] == 0 and row < gameSize - 1:
            row += 1
        if self.root.array[row][col] != 0:
            row -= 1
        self.playerTurn(row, col, 1)
        if self.checkState() == 4:
            winner = turn

        changeTurn()
        return
      






