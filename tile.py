class Tile:
    @staticmethod
    def tile():
        tile = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
        return tile

    @staticmethod
    def duplicate(tile):
        return [list(tile[0]), list(tile[1]), list(tile[2])]

    @staticmethod
    def swap(tile, row, idx, sRow, sIdx):
        swap = tile[row][idx]
        tile[row][idx] = tile[sRow][sIdx]
        tile[sRow][sIdx] = swap
        return tile