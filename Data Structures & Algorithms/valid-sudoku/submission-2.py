from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(list)

        for row in range(len(board)):

            

            rcounter = []         

            for item in range(len(board[row])):
                
                cols[item].append(board[row][item])
                

                if row % 3 == 0 and item % 3 == 0:
                    c1 = []

                    for row2 in board[row:row +3]:
                        for k in row2[item: item +3]:
                            if k == ".":
                                continue
                            elif k not in c1:
                                c1.append(k)
                            else:
                                return False
                    



                if board[row][item]== ".":
                    continue

                if board[row][item] not in rcounter:
                    rcounter.append(board[row][item])
                else:
                    return False
                    
        for col in cols.values():
            filtered = [x for x in col if x != "."]
            if len(filtered) != len(set(filtered)):
                return False
                
        return True
                