class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        horizontal = set()
        vertical = set()

        grid = [set() for _ in range(9)]

        temp = 0
        for i in range(9):
            horizontal = set()
            vertical = set()
            for j in range(9):

                if (board[i][j] in horizontal and board[i][j] != ".") or (board[j][i] in vertical and board[j][i] != "."):
                    return False
                
                horizontal.add(board[i][j])
                vertical.add(board[j][i])

                add =0
                if i>5:
                    add = 4
                elif i>2:
                    add=  2
                quad = i//3  + j//3 + add

                if board[i][j] in grid[quad] and board[i][j] !=".":
                    return False
                grid[quad].add(board[i][j])


        return True 

                # 0 1 2.    00 01 02 03 04 05 06 07 08
                # 1 2 3     10 11
                # 2 3 4.    20

                #           30 31 32
                #           40
                #           50

                #           60 61 62
                #           70
                #           80


# divide by 3 to get the grid 
#assume (6,1) = (2,0) 

 #grid = 
        #    (0,0) , (0,1) , (0,2)
        #    (1,0) , (1,1) , (1,2)
        #    (2,0) , (2,1) , (2,2)



        



            
        