class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(','}': '{', ']':'['}
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif not stack or pairs[ch] != stack.pop():
                return False
        return len(stack) == 0
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna