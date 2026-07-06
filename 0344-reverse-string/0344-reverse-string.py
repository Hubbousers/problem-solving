class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Note: the below problem go through the recursion concepts
        # def recursive(start:int, end:int):
        #     if(start == end or start > end):
        #         return
        #     else:
        #         x=s[start] 
        #         s[start]=s[end]
        #         s[end]=x
        #         start = start+1
        #         end = end - 1
        #         recursive(start, end)
            
        # recursive(0, len(s)-1)

        left = 0
        right = len(s)-1
        while(left<right):
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna