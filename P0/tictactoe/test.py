
X = "X"
O = "O"
EMPTY = None


x = [["X", EMPTY, EMPTY],
     [EMPTY, "O", EMPTY],
     [EMPTY, "O", "X"]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError
    count = 0
    for row in board:
        for element in row:
            if element is EMPTY:
                count += 1

    print(count)

    if count == 9:
        return X 
    
    if count % 2 == 0: 
        return O
    else:
        return X 

print(player(x))
