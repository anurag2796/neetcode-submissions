class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        
        horizontal = defaultdict(set)
        vertical = defaultdict(set)
        grid = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in horizontal[i] or board[i][j] in vertical[j] or board[i][j] in grid[(i//3,j//3)]): 
                    return False

                horizontal[i].add(board[i][j])
                vertical[j].add(board[i][j])
                grid[(i//3,j//3)].add(board[i][j])  

        return True
            
        