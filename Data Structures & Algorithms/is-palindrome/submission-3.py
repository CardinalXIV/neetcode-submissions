class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first strip the " " between the words
        # gotta remove all non-case sensitive and alphanumeric too
        check = "".join(filter(str.isalnum, s)).lower()

        half = (len(check))//2 

        tail = 1
        # then check first and last character and increment
        for character in range(half):
            if check[character] != check[-tail]:
                return False
            else:
                tail += 1

        # all characters match
        return True
