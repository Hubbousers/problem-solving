class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        num_set = set(nums)
        for num in num_set:
            count = 1
            if num-1 not in num_set:
                current = num
                while current+1 in num_set:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna