class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        if len(nums) <= 0:
            return False

        else:
            for i in range(len(nums)):
                for num in nums:
                    if num in seen:
                        return True
                    else:
                        pass
                    seen.add(num)
                return False