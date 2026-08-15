class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0 
        maxi = float('-inf')
        for num in nums:

            if sum < 0:
                sum = 0
            sum += num
            maxi = max(maxi, sum)
        
        return maxi

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna