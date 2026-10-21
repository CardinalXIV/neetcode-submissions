class Solution:
    def isValid(self, s: str) -> bool:
        # don't need to clean string cause only consists of '(', ')', '{', '}', '[' and ']'
        # create a dictionary so that lookup won't grow exponentially when stack increases in size
        seen = { ")" : "(", "]" : "[", "}" : "{"}
        # create an empty stack
        stack = []

        # use a stack to add a counter to each type of bracket and count as its by LIFO 
        # and order matters
        # a plain python list works as a stack
        for character in s:
            # if the stack is empty and the character is closer bracket
            if not stack and character in seen:
                return False

            # push the openers bracket into the stack
            if character not in seen:
                stack.append(character)
            
            # if hit closer brackets and stack isn't empty can pop to check
            if stack and character in seen:
                check = stack.pop()
                # print(check)
                # print(stack)
                # print(character)
                # print(seen.get(character))
                # check if closer is the same as the value of the key -> open bracket
                if check != seen.get(character):
                    return False
        
        # if stack is empty, is valid
        if not stack:
            return True
        
        return False
