class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0 
        end = len(heights) - 1
        best = 0

        while start < end:
            # end - start = width, min of both pointer heights
            area = (end - start) * min(heights[start], heights[end])

            if area > best:
                best = area

            if heights[start] < heights[end]:
                start += 1

            else:
                end -= 1

        return best