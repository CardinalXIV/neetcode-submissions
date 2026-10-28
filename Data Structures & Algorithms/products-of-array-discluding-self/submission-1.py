class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a list the same length as nums
        output = [0] * len(nums)

        # create two lists, one to store the values from left to right the product and one from right to left
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        # init the first element for both lists
        prefix[0] = nums[0]
        suffix[-1] = nums[-1] 

        # calculate the preffix sum array
        for number in range(1, len(nums)):
            prefix[number] = prefix[number - 1] * nums[number]

        # calculate suffix sum array
        # Loop backward from the second-to-last element down to 0
        for number in range(len(nums) - 2, -1, -1):
            suffix[number] = suffix[number + 1] * nums[number]

        # calculate 
        for number in range(len(nums)):
            # first item in list
            if number - 1 < 0:
                output[number] = suffix[number + 1] 
            # last item in list
            elif number + 1 >= len(nums):
                output[number] = prefix[len(prefix) - 2]
            else:
                output[number] = prefix[number - 1] * suffix[number + 1]

        return output
        