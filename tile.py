class Tile(object):

    layout = []

    def __init__(self):
        self.layout = [
            [1, 2, 3], 
            [8, 0, 4], 
            [7, 6, 5]
        ]
        self.history = []

    @staticmethod
    def duplicate(tile):
        t = Tile()
        t.layout = Tile.deepCopyLayout(tile) 
        t.history = list(tile.history)
        return t

    @staticmethod
    def deepCopyLayout(tile):
        return [list(tile.layout[0]), list(tile.layout[1]), list(tile.layout[2])]

    @staticmethod
    def swap(tile, row, idx, sRow, sIdx):
        tile.history.append(Tile.deepCopyLayout(tile))
        swap = tile.layout[row][idx]
        tile.layout[row][idx] = tile.layout[sRow][sIdx]
        tile.layout[sRow][sIdx] = swap
        return tile