class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = 0
        left = 0
        char_counts = {}
        
        # # most frequent character
        # highest_key = max(char_counts, key=char_counts.get)
        
        for char in range(len(s)):
            # If character is not in dicts, it defaults to 0, then adds 1
            char_counts[s[char]] = char_counts.get(s[char], 0) + 1

            freq = max(freq, char_counts[s[char]])

            while (char - left + 1) - freq > k:
                char_counts[s[left]] -= 1
                left += 1

            # and current counter > results, update results
            res = max(res, char - left + 1)
            
        return res
