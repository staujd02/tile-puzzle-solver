from tile import Tile 

class Mover:
    @staticmethod
    def alter_tile(tile, direction, up):
        for rowIndex, row in enumerate(tile.layout):
            for squareIndex, square in enumerate(row):
                if(square == 0):
                    if(up):
                        return Mover.move_vertically(tile, direction, rowIndex, squareIndex)
                    else:
                        return Mover.move_horizontally(tile, direction, rowIndex, squareIndex)

    @staticmethod
    def move_vertically(tile, direction, rowIndex, squareIndex):
        if(rowIndex == direction + 1):
            return None
        return Tile.swap(Tile.duplicate(tile), rowIndex + direction, squareIndex, rowIndex, squareIndex)

    @staticmethod
    def move_horizontally(tile, direction, rowIndex, squareIndex):
        if(squareIndex == direction + 1):
            return None
        return Tile.swap(Tile.duplicate(tile), rowIndex, squareIndex + direction, rowIndex, squareIndex)

    @staticmethod
    def move_down(tile):
        return Mover.alter_tile(tile, direction=1, up=True)

    @staticmethod
    def move_up(tile):
        return Mover.alter_tile(tile, direction=-1, up=True)

    @staticmethod
    def move_right(tile):
        return Mover.alter_tile(tile, direction=1, up=False)

    @staticmethod
    def move_left(tile):
        return Mover.alter_tile(tile, direction=-1, up=False)

    @staticmethod
    def possible_moves(tile):
        moves = [ 
            Mover.move_up(tile), 
            Mover.move_left(tile), 
            Mover.move_right(tile),
            Mover.move_down(tile), 
        ]
        return [item for item in moves if item != None ]