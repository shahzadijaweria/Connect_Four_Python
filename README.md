# Connect_Four_Python

This python code implements the game connect four.
The player can play the game against an AI that makes its move based on 2 difficulty levels; Easy and Hard.
At easy diffuculty, the AI only checks one step deep on what the best move would be and then makes it's move. While on hard difficulty, it check 2-3 steps down. This was implemented using the state-space search min-max algorithm.
I also added a basic level of GUI to make the game more immersive and fun. This was done using the tkinter library. Basically, I created a nxn grid of buttons and which ever column the user clicked on, was the column where the game piece is inserted and it falls down as far as it can go just as in the game connect four.
