class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create an set to store seen numbers
        seen = set(nums)
        
        # similar to the stock problem, keep 2 counters one for current one for best
        current = 0
        best = 0

        for number in seen:
            # min number, start 
            if number - 1 not in seen:
                current = 1

                while number + 1 in seen:
                        number += 1
                        current += 1
                    
            if current > best:
                best = current
        
        return best
                
            
