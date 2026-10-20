class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # sort the input list
        nums.sort()

        # can solve using two sum but target is the first value
        # since the list is sorted, if target > can shift pointer right
        # if target < can shift pointer left
        for number in range(len(nums)):
            # need think of how to prevent out of range
            # need think of how to remove dupe?

            # create 2 pointers: left (2nd back of list), right (end of the list)
            left = number + 1
            right = len(nums) - 1

            # once left pointer passes right, stop the search
            while left < right:
                # if triplet = 0, triplet exist
                if nums[number] + nums[left] + nums[right] == 0:
                    # add only if not in results already
                    if [nums[number], nums[left], nums[right]] not in res:
                        res.append([nums[number], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                # if triplet > 0
                elif nums[number] + nums[left] + nums[right] > 0:
                    right -= 1 

                # if triplet < 0
                elif nums[number] + nums[left] + nums[right] < 0:
                    left += 1

        return res