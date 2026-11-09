class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        right = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                # we shrink the window by incrementing the left pointer until the window no longer contains any duplicates
                # by comparing the new element s[right] to existing set and remove until no dupes
                seen.remove(s[left])
                left += 1
                
                
            # only add s[right] and calculate the current once the current window is valid
            seen.add(s[right])
            current = right - left + 1

            # and current counter > results, update results
            if res < current:
                res = current

            right += 1
            
        return res