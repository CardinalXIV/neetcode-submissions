from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        right = 0
        res = []
        current = deque()

        while right < len(nums):
            # left most valid index of current window
            left = right - k + 1

            # while no at back < new num (pop from back)
            while current and nums[current[-1]] < nums[right]:
                current.pop()

            # add new position to back
            current.append(right)

            # if front position out of window pop from front
            if current[0] < left:
                current.popleft()

            # once right reached end of first full window, front value is window max
            if right >= k - 1:
                res.append(nums[current[0]])

            right += 1
        
        return res