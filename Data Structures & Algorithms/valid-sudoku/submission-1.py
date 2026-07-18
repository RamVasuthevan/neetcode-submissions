from collections import Counter
from itertools import chain
from pprint import pprint

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pprint(board)

        BOARD_SIZE_ROWS = 9
        BOARD_COLUMNS_ROWS = 9

        BOARD_SIZE_CELLS_ROWS = 3
        BOARD_SIZE_CELLS_COLUMNS = 3

        for row in board:
            C = Counter(row)
            del C["."]
            if max(C.values(),default=0) not in {0,1}:
                return False

        for columnInd in range(BOARD_COLUMNS_ROWS):
            C = Counter((board[rowInd][columnInd] for rowInd in range(BOARD_COLUMNS_ROWS)))
            del C["."]
            if max(C.values(),default=0) not in {0,1}:
                return False
        
        for rowInd in range(0,BOARD_SIZE_ROWS,BOARD_SIZE_CELLS_ROWS):
            for columnInd in range(0,BOARD_SIZE_ROWS,BOARD_SIZE_CELLS_COLUMNS):
                C = Counter(chain.from_iterable(board[rowInd+cellRowInd][columnInd:columnInd+BOARD_SIZE_CELLS_COLUMNS] for cellRowInd in range(BOARD_SIZE_CELLS_ROWS)))
                del C["."]
                if max(C.values(),default=0) not in {0,1}:
                    return False
        return True