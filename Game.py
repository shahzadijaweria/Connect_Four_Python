import Node

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

    def __init__(self):
        self.root = Node.Node()

    def playerTurn(self, row, col, val):
        self.root.setValue(row, col, val)
        self.root.print()

    def gameStates(self, state):
        if state == 'min':
            row = int(input("Enter Row:"))
            col = int(input("Enter Col:"))
            self.playerTurn(row, col, -1)
        elif state == 'max':
            row = int(input("Enter Row:"))
            col = int(input("Enter Col:"))
            self.playerTurn(row, col, 1)

    def gamePlay(self):
        global winner
        while winner == 'None':
            self.gameStates(turn)
            if self.checkState() == 4:
                winner = turn
                if winner == 'min':
                    print('YOU WON!!')
                else:
                    print('YOU LOST!!')
            changeTurn()

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

    def checkState(self):
        count = 0
        if turn == 'max':
            ##check horizontally
            ##check horizontally
            for i in range(gameSize):
                count = 0
                for j in range(gameSize):
                    if self.root.array[i][j] == 1:
                        count += 1
                        if count == 4:
                            return count
            ##check vertically
            for i in range(gameSize):
                count = 0
                for j in range(gameSize):
                    if self.root.array[j][i] == 1:
                        count += 1
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
            for i in range(gameSize):
                count = 0
                for j in range(gameSize):
                    if self.root.array[i][j] == -1:
                        count += 1
                        if count == 4:
                            return count
            ##check vertically
            for i in range(gameSize):
                count = 0
                for j in range(gameSize):
                    if self.root.array[j][i] == -1:
                        count += 1
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

