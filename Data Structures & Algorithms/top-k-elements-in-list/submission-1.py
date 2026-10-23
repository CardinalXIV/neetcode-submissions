class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create an empty dictionary to store the seen values and their count
        seen = {}
        # list to store results
        result = []

        # if the element isn't in the dictionary, add it, else increase the value
        for element in nums:
            if element not in seen:
                seen[element] = 1
            else:
                seen[element] += 1
            
        result = sorted(seen.items(), key=lambda item: item[1], reverse=True)

        top_k_keys = [item[0] for item in result[:k]]

        return top_k_keys
        