class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        for i in range(0, len(nums)):
            x = target - nums[i]
            remaining = nums[i+1:]
            if(x in remaining):
                indexes.append(i)
                r_index = remaining.index(x) + (i+1)
                indexes.append(r_index)
                break
        return indexes
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna