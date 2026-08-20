class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_sum, max_sum, current_max, current_min = float('inf'),float('-inf'),0,0
        total_sum = sum(nums)
        for num in nums:
            current_max = max(num, current_max+num)
            current_min = min(num, current_min+num)
            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)

        if max_sum < 0:
            return max_sum
        circular_max = total_sum - min_sum
        return max(abs(max_sum),abs(circular_max))
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna