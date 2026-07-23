class Solution:
    def isValid(self, s: str) -> bool:
        # UMPIRE
        # Match: Stack
        # Plan: Use hashmap to map the opening and closing parentheses
        # Implement: 
        stack = []
        closeToOpen = { ")" : "(",      # hashmap
                        "]" : "[",
                        "}" : "{"}
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        # Review
        ## Time: O(n) to go through every character
        ## Space: Stack is O(n)