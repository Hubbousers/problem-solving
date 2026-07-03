class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Solution 1:  Time = O(n) and space = O(2n)
        # indexes = []
        # for i in range(0, len(nums)):
        #     x = target - nums[i]
        #     remaining = nums[i+1:]
        #     if(x in remaining):
        #         indexes.append(i)
        #         r_index = remaining.index(x) + (i+1)
        #         indexes.append(r_index)
        #         break
        # return indexes
        #Solution 2
        dictionary = {}
        for i in range(len(nums)):
            search_element = target - nums[i]
            if search_element in dictionary:
                return [dictionary[search_element], i]
            dictionary[nums[i]] = i
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna