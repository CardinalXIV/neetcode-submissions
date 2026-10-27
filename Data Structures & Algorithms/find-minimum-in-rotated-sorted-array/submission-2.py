# /*
# # while the head pointer hasn't passed the tail pointer
#         while tail >= head:
#             mid = (tail + head)//2

#             # if target larger than mid shift right
#             if target > nums[mid]:
#                 head = mid + 1
                
#             # if target smaller than mid shift left
#             elif target < nums[mid]:
#                 tail = mid - 1

#             # nums[mid] == target, return index
#             else:
#                 return mid
# */
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # since is a sorted then rotated array
        # hint is the split into two arrays that are sorted then based on which array has mid inside
        # then ditch the other part
        left = 0
        right = len(nums) - 1

        # shifting both pointers so if they ever cross, means nothing left
        while left < right:
            mid = (right + left)//2

            # if there is a upward trend (mid is still a candidate)
            if nums[mid] < nums[right]:
                right = mid
                
            # if there is a downward trend, mid is no longer a candidate
            elif nums[mid] > nums[right]:
                left = mid + 1
            
        return nums[right]