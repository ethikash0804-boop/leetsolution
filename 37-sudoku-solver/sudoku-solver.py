class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets and empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def backtrack(index):
            # If all empty cells filled
            if index == len(empty):
                return True

            r, c = empty[index]
            box = (r // 3) * 3 + (c // 3)

            for num in "123456789":

                if num not in rows[r] and \
                   num not in cols[c] and \
                   num not in boxes[box]:

                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

                    # Move to next empty cell
                    if backtrack(index + 1):
                        return True

                    # Backtrack
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)

            return False

        backtrack(0)