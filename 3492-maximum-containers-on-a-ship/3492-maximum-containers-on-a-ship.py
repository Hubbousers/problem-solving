class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        total_containers = n*n
        # how_many_containers_with_weight_w_it_can_hold
        max_possible_containers = total_containers * w
        # maximum_containers_with_weight_w_it_can_hold 
        maxi_con = int(maxWeight/w)
        minimum_containers = min(maxi_con, total_containers)

        return minimum_containers
        # if maxi_con < total_containers:
        #     return maxi_con
        # else:
        #     return total_containers

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna