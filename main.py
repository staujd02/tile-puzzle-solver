def tile():
    tile = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    return tile

def move_up(tile):
    if(tile[0][1] == 0):
        return None
    return [
            [1, 0, 3], 
            [8, 2, 4], 
            [7, 6, 5]
        ]


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
