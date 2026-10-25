class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # create a index pointing to the middle of the list
        head = 0
        tail = len(nums) - 1
 
        # while the head pointer hasn't passed the tail pointer
        while tail >= head:
            mid = (tail + head)//2

            # if target larger than mid shift right
            if target > nums[mid]:
                head = mid + 1
                
            # if target smaller than mid shift left
            elif target < nums[mid]:
                tail = mid - 1

            # nums[mid] == target, return index
            else:
                return mid

        return -1