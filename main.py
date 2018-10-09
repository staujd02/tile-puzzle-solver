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

def mover(tile):
    # results = []
    # for row in tile:
    #     for square in row:
    #         if(square == 0):
    #             move_up = list(tile)
    #             move_down = list(tile)
    #             move_left = list(tile)
    #             move_right = list(tile)
    #             return [move_up, move_down, move_left, move_right]
    return [
        [[1, 0, 3], [8, 2, 4], [7, 6, 5]],
        [[1, 2, 3], [0, 8, 4], [7, 6, 5]],
        [[1, 2, 3], [8, 4, 0], [7, 6, 5]],
        [[1, 2, 3], [8, 6, 4], [7, 0, 5]]
    ]
