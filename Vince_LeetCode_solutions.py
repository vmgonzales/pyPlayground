# -*- coding: utf-8 -*-
"""
Created on Mon May  2 07:24:59 2022

@author: vmgon
"""


#%% LeetCode 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
          'M': 1000}
        
        last = s[-1]
        for t in reversed(s):
          #print(t, last)
          if t == 'C' and last in ['D', 'M']:
            total -= roman[t]
            
          elif t == 'X' and last in ['L', 'C']:
            total -= roman[t]
            
          elif t == 'I' and last in ['V', 'X']:
            total -= roman[t]
            
          else:
            total += roman[t]
          last = t
          
        return total


print(Solution().romanToInt(s = 'I'), '\n')

print(Solution().romanToInt(s = 'IV'))
print(Solution().romanToInt(s = 'V'))
print(Solution().romanToInt(s = 'VI'), '\n')

print(Solution().romanToInt(s = 'IX'))
print(Solution().romanToInt(s = 'X'))
print(Solution().romanToInt(s = 'XI'), '\n')

print(Solution().romanToInt(s = 'XL'))
print(Solution().romanToInt(s = 'LI'))
print(Solution().romanToInt(s = 'LIII'), '\n')

print(Solution().romanToInt(s = 'XCIII'))
print(Solution().romanToInt(s = 'C'))
print(Solution().romanToInt(s = 'MXCIV'))


#%% LeetCode 36: Valid Sudoku


from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        # Convert board from chars to integers
        for i in range(0, len(board)):
            for j in range(0, len(board)):
              if board[i][j] == '.':
                  board[i][j] = 0
              else:
                  board[i][j] = int(board[i][j])
    
        # Check each row for digits in the range [1, 9] w/o repetition
        for i in range(9):
      
            thisRow = board[i]
            digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            #print("Looking at row: ", i)
      
        for j in range(9):
        
            if thisRow[j] in digits:
                digits.remove(thisRow[j])
            elif thisRow[j] == 0:
                pass
            else:
                #print("Bad Row")
                return False
        
        # Check each column for digits in the range [1,9] w/o repetition
        for j in range(9):
            
            thisCol = [row[j] for row in board]
            digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
      
            for i in range(9):
            
                if thisCol[i] in digits:
                    digits.remove(thisCol[i])
                elif thisCol[i] == 0:
                    pass
                else:
                    #print("Bad column.")
                    return False
        
        #Check each 3x3 sub-box for digits [1,9] w/o repetition
        for m in range(3):
            for n in range(3):
                digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                
                # Looking at each sub-box individually:
                for i in range(3):
                    for j in range(3):
                        
                        if board[i + 3 * m][j + 3 * n] in digits:
                            digits.remove(board[i + 3 * m][j + 3 * n])
                        elif board[i + 3 * m][j + 3 * n] == 0:
                            pass
                        else:
                            print("Bad sub-box: ", m + 1, n + 1)
                            return False
        
        # If rows, columns, and 3x3 boxes are good --> puzzle is valid!
        return True

#%% LeetCode 36 test cases
# Valid sudoku test case
board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))


# Bad column test case.
board = [["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))

# Another bad column test case
board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
["6",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))


# Bad 3x3 box test case (lower right).
board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","9","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))
