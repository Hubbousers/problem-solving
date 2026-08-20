class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        presum = []
        current_sum, max_prefix, min_prefix = 0,0,0
        for num in nums:
            current_sum += num
            max_prefix = max(max_prefix, current_sum)
            min_prefix = min(min_prefix, current_sum)
        
        return max_prefix - min_prefix

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna