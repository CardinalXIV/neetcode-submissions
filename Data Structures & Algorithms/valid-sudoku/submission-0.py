class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Set of valid characters
        valid = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        
        # Use plural names to avoid confusion with loop variables
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Iterate through each row (r) and column (c)
        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                
                # Check if character is valid
                if val not in valid:
                    return False
                
                # Ignore empty cells
                if val == ".":
                    continue
                
                # Calculate the 3x3 sub-box index (0 to 8)
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check if the number already exists in the current row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False

                # Add the number into the respective sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        return True