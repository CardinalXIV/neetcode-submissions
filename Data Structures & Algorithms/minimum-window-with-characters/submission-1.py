from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        seent = Counter(t)
        seens = Counter()
        best = len(s) + 1
        result = ""

        # create pointers for sliding window
        left = 0

        # have, need, best counters
        have = 0
        need = len(seent)
        best_window = [0]*2

        # create a for loop on the 1st string s
        for right in range(len(s)):
        
            # If character is not in dicts, it defaults to 0, then adds 
            seens[s[right]] = seens.get(s[right], 0) + 1

            # add only distinct char to have
            if s[right] in seent and seens[s[right]] == seent[s[right]]:
                have += 1

            # when the entirety of t is in the current window
            while have == need:
                # start to trim to get to smallest substring possible
                if right - left + 1 < best:
                    best = right - left + 1
                    best_window = [left, right]

                seens[s[left]] -= 1

                if s[left] in seent and seens[s[left]] < seent[s[left]]:
                    have -= 1 
                
                left += 1
            
        # the best window’s position. Then slice s once at the very end.
        if best != len(s) + 1:
            result = s[best_window[0]:best_window[1] + 1]

        return result