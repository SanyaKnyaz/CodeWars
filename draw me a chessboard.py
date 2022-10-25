#draw me a chessboard
'''
https://www.codewars.com/kata/56242b89689c35449b000059
Task
A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

Making a digital chessboard I think is an interesting way of visualising how loops can work together.

Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two
dimensional array.

So chessBoard(6,4) should return an array like this:

[
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"]
]
And chessBoard(3,7) should return this:

[
    ["O","X","O","X","O","X","O"],
    ["X","O","X","O","X","O","X"],
    ["O","X","O","X","O","X","O"]
]
The white spaces should be represented by an: 'O'

and the black an: 'X'

The first row should always start with a white space 'O'
'''

def chess_board(rows, columns):
    res = []
    for i in range(1, rows+1):
        lst = []
        for j in range(i, columns+i):
            if j%2 != 0:
                lst.append('O')
            else:
                lst.append('X')
        res.append(lst)
    return res
