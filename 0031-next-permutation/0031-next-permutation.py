class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)
        for i in range (n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            return nums.sort()
        
        for i in range(n-1,index,-1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        nums[index+1:n] = nums[index+1:n][::-1]
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna