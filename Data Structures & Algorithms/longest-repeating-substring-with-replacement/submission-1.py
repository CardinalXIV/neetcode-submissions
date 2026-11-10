class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = 0
        left = 0
        char_counts = {}
        
        for right in range(len(s)):
            # If character is not in dicts, it defaults to 0, then adds 1
            char_counts[s[right]] = char_counts.get(s[right], 0) + 1

            freq = max(freq, char_counts[s[right]])

            while (right - left + 1) - freq > k:
                char_counts[s[left]] -= 1
                left += 1

            # and current counter > results, update results
            res = max(res, right - left + 1)
            
        return res
