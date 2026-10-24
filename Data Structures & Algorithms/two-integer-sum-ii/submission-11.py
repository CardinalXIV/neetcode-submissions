class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input is sorted in asc order
        # numbers cannot be equal
        
        for index in range(len(numbers)):
            tail = len(numbers) - 1

            while index < tail:
                # if remainder and target not the same and index of 2nd int not smaller than first
                # and the remainder is found
                if numbers[index] + numbers[tail] == target:
                    # 1-indexed
                    return [index + 1, tail + 1]

                elif numbers[index] + numbers[tail] < target:
                    index += 1

                elif numbers[index] + numbers[tail] > target:
                    tail -= 1

            
        return []

