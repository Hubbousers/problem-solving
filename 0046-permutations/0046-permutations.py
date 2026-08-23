class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        def backTrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i] != True:
                    #append 
                    used[i] = True
                    path.append(nums[i])

                    #backtrack
                    backTrack(path)

                    #undo
                    used[i] = False
                    path.pop()
        #always start with empty list so that 
        backTrack([])

        return result

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna