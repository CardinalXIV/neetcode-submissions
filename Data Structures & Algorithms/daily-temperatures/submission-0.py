class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        # go in reverse order
        for temp in range(len(temperatures) -1, -1, -1):
            days = 0

            # while stack has a number and the current temp is the new highest, pop the rest of the stack
            while stack and temperatures[stack[-1]] <= temperatures[temp]:
                stack.pop()
            
            # since stack is not empty, top is warmest day
            if stack:
                result[temp] = stack[-1] - temp

            # add current temp index into stack
            stack.append(temp)
            
        return result