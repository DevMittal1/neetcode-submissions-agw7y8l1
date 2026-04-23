import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cold = collections.defaultdict(set)
        rowd = collections.defaultdict(set)
        squared = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue
                if (value in cold[i] or 
                value in rowd[j] or 
                value in squared[(i//3,j//3)]):
                    return False
                else:
                    cold[i].add(value)
                    rowd[j].add(value)
                    squared[(i//3,j//3)].add(value)
        return True

