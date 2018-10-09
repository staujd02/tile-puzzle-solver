def tile():
    tile = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    return tile

def duplicate(tile):
    return [list(tile[0]), list(tile[1]), list(tile[2])]

def swap(tile, row, idx, sRow, sIdx):
    swap = tile[row][idx]
    tile[row][idx] = tile[sRow][sIdx]
    tile[sRow][sIdx] = swap
    return tile

def move_vertically(tile, direction):
    for rowIndex, row in enumerate(tile):
        for squareIndex, square in enumerate(row):
            if(square == 0):
                if(rowIndex == direction + 1):
                    return None
                return swap(duplicate(tile), rowIndex + direction, squareIndex, rowIndex, squareIndex)

def move_horizontally(tile, direction):
    for rowIndex, row in enumerate(tile):
        for squareIndex, square in enumerate(row):
            if(square == 0):
                if(squareIndex == direction + 1):
                    return None
                return swap(duplicate(tile), rowIndex, squareIndex + direction, rowIndex, squareIndex)

def move_down(tile):
    return move_vertically(tile, direction=1)

def move_up(tile):
    return move_vertically(tile, direction=-1)

def move_right(tile):
    return move_horizontally(tile, direction=1)

def move_left(tile):
    return move_horizontally(tile, direction=-1)

def possible_moves(tile):
    moves = [ 
        move_up(tile), 
        move_left(tile), 
        move_right(tile),
        move_down(tile), 
    ]
    return [item for item in moves if item != None ]