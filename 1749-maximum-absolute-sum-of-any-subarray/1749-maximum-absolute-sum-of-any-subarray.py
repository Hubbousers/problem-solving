class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        current_sum, max_sum, min_sum = 0,0,0
        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            min_sum = min(min_sum, current_sum)

        return max_sum - min_sum

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna