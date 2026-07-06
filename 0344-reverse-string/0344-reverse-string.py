class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursive(start:int, end:int):
            if(start == end or start > end):
                return
            else:
                x=s[start]
                s[start]=s[end]
                s[end]=x
                start = start+1
                end = end - 1
                recursive(start, end)
            
        recursive(0, len(s)-1)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna