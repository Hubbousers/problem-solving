class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)

        def backtrack(path):
            
            if len(path) == len(nums):
                result.append(path.copy())
                return
            # your code
            ##choice
            for i in range(0, len(nums)):

                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                if used[i] != True:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False
        backtrack([])

        return result
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna