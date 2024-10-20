class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [] # Initialize the result list to hold all subsets

        def dfs(ind, sp):
            if ind == len(nums): # Base case: if the index is equal to the length of nums
                res.append(sp) # Add the current subset to the result
                return 
            # Recursive case 1: Include the current element in the subset
            dfs(ind + 1, sp + [nums[ind]])
            # Recursive case 2: Exclude the current element from the subset
            dfs(ind + 1, sp)
                
        dfs(0, []) # Start the DFS with the first index and an empty subset
        return res # Return the list of all subsets
        