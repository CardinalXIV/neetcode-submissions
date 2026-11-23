class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            # if the target greater than the current row
            if target > row[-1]:
                pass

            # target in row
            elif row[0] <= target <= row[-1]:
                for col in row:
                    if col == target:
                        return True
         
        return False