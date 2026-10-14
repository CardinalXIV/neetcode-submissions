class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create an empty dictionary
        seen = {}

        # get target to minus number in list and then check if remainder in list
        for index, value in enumerate(nums):
            complement = target - value
            # if remainder is seen, return current item index and seen item index
            if complement in seen:
                return [seen[complement], index]
            # if complement not found
            else:
                # if value isn't in dictionary add it and the index of it in the list in
                if value not in seen:
                    seen[value] = index
