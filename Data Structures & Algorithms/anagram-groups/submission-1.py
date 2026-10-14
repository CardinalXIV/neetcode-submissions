class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary to use for sorting of lists?
        seen = {}
        # results list
        res = []

        # create 

        for word in strs:
            # sort the word first
            # cause we can't use a list as a key we need to make it back into a string
            # we use "".join instead of just .join cause we wanna concat but faster than
            # looping through smth with a result += char
            group = "".join(sorted(word))

            # if group not in dict, add it in as a key
            if group not in seen:
                seen[group] = [word] # store original word in group as a list
            else: # if the seen group is inside, we need to append it to the list
                seen[group].append(word)

        # once all the words are grouped in the dict, export the results to a list
        for group in seen:
            res.append(seen[group])
        
        return res