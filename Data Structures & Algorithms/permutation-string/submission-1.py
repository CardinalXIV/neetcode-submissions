class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a dict for s1 with characters as key and count as value
        seens1 = dict(zip(s1, (s1.count(i) for i in s1)))
        seens2 = {}

        left = 0 

        for right in range(len(s2)):
            # If character is not in dicts, it defaults to 0, then adds 1
            seens2[s2[right]] = seens2.get(s2[right], 0) + 1

            # if current window bigger than s1 length
            if right - left + 1 > len(s1):
                seens2[s2[left]] -= 1

                # del key if count is 0
                if seens2[s2[left]] == 0:
                    del seens2[s2[left]]

                left += 1
        
            # compare frequency maps
            if seens1 == seens2:
                return True

        return False