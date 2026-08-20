class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        current_min, current_max, max_sum, min_sum = 0,0,0,0
        for num in nums:
            current_min = min(num, num+current_min)
            min_sum = min(current_min, min_sum)

            current_max = max(num, num+current_max)
            max_sum = max(current_max, max_sum)

        return (max(abs(max_sum), abs(min_sum)))

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna