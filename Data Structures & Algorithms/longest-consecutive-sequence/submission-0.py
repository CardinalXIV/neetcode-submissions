class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create an empty set to store seen numbers
        seen = set()
        
        # similar to the stock problem, keep 2 counters one for current one for best
        current = 0
        best = 0

        # one pass the nums list
        for number in nums:
            # add all distinct numbers into the set
            if number not in seen:
                seen.add(number)

        for number in seen:
            # min number, start 
            if number - 1 not in seen:
                current = 1
                start = True
                while start is True:
                    # next number exists, increment
                    if number + 1 in seen:
                        number += 1
                        current += 1
                    else:
                        start = False
                        if current > best:
                            best = current
        
        return best
                
            
