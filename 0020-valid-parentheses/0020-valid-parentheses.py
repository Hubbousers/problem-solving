class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(','}': '{', ']':'['}
        stack = []
        for ch in s:
            if len(stack) != 0 and ch in pairs:
                ele = stack.pop()
                if ele != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna