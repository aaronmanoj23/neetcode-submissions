class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for r in board:
            counter = dict()
            for num_str in r:
                if num_str != ".":
                    counter[num_str] = counter.get(num_str, 0) + 1
                    if counter[num_str] >= 2:
                        return False

        # Check each column
        for i in range(9):
            counter = dict()
            for j in range(9):
                num_str = board[j][i]
                if num_str != ".":
                    counter[num_str] = counter.get(num_str, 0) + 1
                    if counter[num_str] >= 2:
                        return False

        # Check each sub-boxes
        for i in range(3):
            for j in range(3):
                counter = dict()
                for n in range(3):
                    for k in range(3):
                        num_str = board[i * 3 + n][j * 3 + k]
                        if num_str != ".":
                            counter[num_str] = counter.get(num_str, 0) + 1
                            if counter[num_str] >= 2:
                                return False
        
        return True