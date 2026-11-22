class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest = 0

        # precomputing the left and right boundaries (hint 2)
        # left, right boundaries are positions 
        # we can extend at index i (hint 3)
        # boundaries are determined by the first smaller bars 
        # at left and right of the current bar

        # left and right to store the boundaries for each index
        left = [-1] * len(heights)
        right = [len(heights)] * len(heights)

        stack = []

        # fill out left and right arrays
        for i in range(len(heights)):
            # while left not empty and the i is the new lowest,   
            # pop the rest of the stack
            # if while loop pops everything off stack, no smaller bar 
            # rectangle can extend all the way past the edge of the histogram
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            # add current index into stack
            stack.append(i)

        stack = []

        for i in range(len(heights) - 1, -1, -1):
            # while right not empty and the i is the new lowest,   
            # pop the rest of the stack
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]

            # add current index into stack
            stack.append(i)

        # monotonic stack (Hint 4) strictly increasing nature
        # only store index and perform operations based on value
        # The top of the stack will represent the smaller bar 
        # while extending the current bar

        for index in range(len(heights)):
            # Exclude both boundary indices (left[index] and right[index])
            width = right[index] - left[index] - 1
            area = heights[index] * width
            # update if this current is the biggest
            biggest = max(area, biggest)

        return biggest