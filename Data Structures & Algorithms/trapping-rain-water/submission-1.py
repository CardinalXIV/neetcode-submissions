class Solution:
    def trap(self, height: List[int]) -> int:
        # for water to be trapped both sides of the 0 input has to have a number 
        # or the input both sides have to have a value higher than itself e.g. 1,2,1

        # to calculate water trapped hint 3 provides: 
        # trapped water at index i is given by: min(height[l], height[r]) - height[i]
        # tallest bar on each side of position i

        start = 0
        end = len(height) - 1
        area = 0

        # store values > 0
        prefix = [0] * len(height)
        prefix[0] = height[0]

        suffix = [0] * len(height)
        suffix[-1] = height[-1]

        # fill out prefix and suffix arrays
        for number in range(1, len(height)):
            prefix[number] = max(height[number], prefix[number - 1])

        for number in range(len(height) - 2, -1, -1):
            suffix[number] = max(height[number], suffix[number + 1])

        # calculate trapped water
        for number in range(len(height)):
            area += min(suffix[number], prefix[number]) - height[number]

        return area
        