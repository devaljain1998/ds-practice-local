from collections import defaultdict
from typing import Dict, List, Set, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols: Dict[int, Set[int]] = defaultdict(set)
        rows: Dict[int, Set[int]] = defaultdict(set)
        squares: Dict[Tuple[int, int], Set[int]] = defaultdict(set)
        
        n = len(board)
        
        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                # condition to invalidate:
                elif (
                    int(board[r][c]) in rows[r]
                    or int(board[r][c]) in cols[c]
                    or int(board[r][c]) in squares[r // 3, c // 3]
                ):
                    return False
                
                ele = int(board[r][c])
                rows[r].add(ele)
                cols[c].add(ele)
                squares[r // 3, c // 3].add(ele)

        return True