import random
import Node
import time
import tkinter
import sys

top = tkinter.Tk()
top.title("Connect Four")

gameSize = 7
difficultyLevel = 'Easy'
winner = 'None'
turn = 'max'


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

    def playerTurn(self, row, col, val):
        self.root.setValue(row, col, val)
        ##self.root.print()

# computer play function
    def gameStates(self):
        print(turn)
        global winner
        row = random.randrange(gameSize)
        col = random.randrange(gameSize)
        while self.root.array[row][col] == 0 and row < gameSize - 1:
            row += 1
        if self.root.array[row][col] != 0:
            row -= 1
        self.playerTurn(row, col, 1)
        if self.checkState() == 4:
            winner = turn

        changeTurn()
        return

# player play function
    def onButtonPress(self, i, j):
        global winner
        print(turn)
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
        changeTurn()
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
                self.button[i][j] = tkinter.Button(top, text=self.root.array[i][j], command=lambda: self.onButtonPress(i, j), width=4, height=3)
                self.colour(i, j)
                self.button[i][j].grid(row=i, column=j)

        top.mainloop()

        if winner == 'min':
            print('YOU WON!!')
            time.sleep(5)
            sys.exit()
        elif winner == 'max':
            print('YOU LOST!!')
            time.sleep(5)
            sys.exit()