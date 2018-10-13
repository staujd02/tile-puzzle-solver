class Tile(object):

    layout = []

    def __init__(self):
        self.layout = [
            [1, 2, 3], 
            [8, 0, 4], 
            [7, 6, 5]
        ]

    @staticmethod
    def duplicate(tile):
        t = Tile()
        t.layout = [list(tile.layout[0]), list(tile.layout[1]), list(tile.layout[2])]
        return t

    @staticmethod
    def swap(tile, row, idx, sRow, sIdx):
        swap = tile.layout[row][idx]
        tile.layout[row][idx] = tile.layout[sRow][sIdx]
        tile.layout[sRow][sIdx] = swap
        return tile