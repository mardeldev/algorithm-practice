"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

import collections
class Sudoku:
    def __init__(self, board, size) -> None:
        self.board = board
        self.size = size


    def is_valid(self):
        board = self.board
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        square = collections.defaultdict(set)  # key -> (r // 3, c // 3)

        for r in range(self.size):
            for c in range(self.size):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                        board[r][c] in square[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        return True

    
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# board size (e.g. 9 to represent 9x9)
size = 9

# instantiate solution object
sudoku_board_1 = Sudoku(board, size)

# perform validity checker
print(sudoku_board_1.is_valid())













    
    # def partition(self, lst, size):
    #     for row in lst:
    #         for i in range(0, len(row), size):
    #             yield row[i: i+size]

    # def check_rows(self, p_list):
    #     return self.entity_checker(p_list, 3)

    # def check_blocks(self, p_list):
    #     p_blocks = self.partition_blocks(p_list)
    #     return self.entity_checker(p_blocks, 3)

    # def check_cols(self, p_list):
    #     p_blocks = self.partition_blocks(p_list)
    #     return self.partition_cols(p_blocks)

    # def partition_cols(self, p_blocks):
    #     newl = [[]]
    #     counter = 0
    #     index = 0
    #     for p in range(3):
    #         for item in p_blocks:
    #             if counter == 3:
    #                 newl.append([])
    #                 counter = 0
    #                 index += 1
    #             newl[index].append(item[p])
    #             counter += 1
    #     return self.entity_checker(newl, 3)

    # def entity_checker(self, p_entity, size):
    #     entity_set = set()
    #     idx = 0
    #     for item in p_entity:
    #         if idx < size:
    #             for val in item:
    #                 if val != '.':
    #                     if val in entity_set:
    #                         # print(False)
    #                         return False
    #                     else:
    #                         entity_set.add(val)
    #         idx += 1
    #         if idx == size:
    #             idx = 0
    #             entity_set.clear()
    #     return True

    # def partition_blocks(self, p_list):
    #     col_lst = []
    #     no_of_cols = 3
    #     for n in range(no_of_cols):
    #         for y in range(n, len(p_list), no_of_cols):
    #             col_lst.append(p_list[y])
    #     return col_lst

    # def check_validity(self, p_list):
    #     if self.check_rows(p_list) & self.check_cols(p_list) & self.check_blocks(p_list):
    #         return True
    #     else:
    #         return False


# # instantiate solution object
# solution = Valid_Sudoku()

# # size of each chunk
# n = 3
# # partition the list
# p_list = list(solution.partition(board, n))

# # perform validity checker
# print(solution.check_validity(p_list))
