class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a dictionary for a key value pair
        seen = {}

        # for each new character in the first string, add the char
        # then the value will be the count of times it appears in s
        # if the character is in the dict, count +1
        for character in s:
            if character not in seen:
                seen[character] = 1
            else:
                seen[character] += 1

        # for character in string t, if character doesn't exist - False
        # if character exists in dict, reduce counter by 1
        for character in t:
            if character not in seen:
                return False
            else:
                seen[character] -= 1
        
        # if all values are 0, means dictionary all keys match
        if all(value == 0 for value in seen.values()):
            return True
        else:
            return False
        
         