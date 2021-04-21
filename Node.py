import Game


class Node:
    def __init__(self):
        self.array = [[0 for i in range(Game.gameSize)] for j in range(Game.gameSize)]

    def print(self) -> object:
        for i in range(Game.gameSize):
            for j in range(Game.gameSize):
                print(self.array[i][j], end=" ")
            print()

    def setValue(self, row, col, val):
        self.array[row][col] = val
