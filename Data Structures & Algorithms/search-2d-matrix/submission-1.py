class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # create a index pointing to the middle of the list
        head_row = 0
        tail_row = len(matrix) - 1

        head_col = 0
        tail_col = len(matrix[0]) - 1

        while tail_row >= head_row:
            mid_row = (tail_row + head_row)//2

            # if target larger than mid shift right
            if target > matrix[mid_row][-1]:
                head_row = mid_row + 1
                
            # if target smaller than mid shift left
            elif target < matrix[mid_row][0]:
                tail_row = mid_row - 1

            # if target in row
            else:
                # while the head pointer hasn't passed the tail pointer
                while tail_col >= head_col:
                    mid_col = (tail_col + head_col)//2

                    # if target larger than mid shift right
                    if target > matrix[mid_row][mid_col]:
                        head_col = mid_col + 1
                        
                    # if target smaller than mid shift left
                    elif target < matrix[mid_row][mid_col]:
                        tail_col = mid_col - 1

                    # matrix[mid_row][mid_col] == target, return index
                    else:
                        return True

                return False
         
        return False