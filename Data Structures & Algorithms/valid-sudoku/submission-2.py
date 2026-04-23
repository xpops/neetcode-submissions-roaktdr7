class Solution: # NAIVE
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # row
        for i in range(9):
            empty_count = board[i].count(".")
            if len(set(board[i])) + empty_count - 1 == 9: # no duplicates
                continue
            return False
        
        # col
        for i in range(9):
            arr = []
            empty_count = 0
            for j in range(9):
                if board[j][i] == ".":
                    empty_count += 1
                arr.append(board[j][i])
            if len(set(arr)) + empty_count - 1 == 9:
                continue
            return False
        
        # box
        for i in range(9):
            arr = []
            empty_count = 0
            for j in range(3):
                for k in range(3):
                    curr = board[j + int(i / 3) * 3][k + i % 3 * 3]
                    if curr == ".":
                        empty_count += 1
                    arr.append(curr)
            if len(set(arr)) + empty_count - 1 == 9:
                continue
            return False

        
        return True
        
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
