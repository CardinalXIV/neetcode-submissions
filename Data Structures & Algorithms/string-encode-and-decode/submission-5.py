class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ""
        # for each string in the list, add a num of the range as a delimiter
        for string in strs:
            length = len(string)
            encoded_strs += (str(length) + "#" + string)

        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        first = 0
        
        while first < len(s):
            string = ""
            number = ""
            second = first

            while s[second] != "#":
                number += s[second]
                second += 1
            
            counter = int(number) + second + 1
            increment = len(number)
            string = s[second + 1 : counter]
            decoded_strs.append(string)

            first = counter
        
        return decoded_strs

                