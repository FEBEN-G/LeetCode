class Solution:
    def minPairSum(self, nums):
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        min_pair_sum = float('-inf')
        while left < right:
            pair_sum = nums[left] + nums[right]
            min_pair_sum = max(pair_sum, min_pair_sum)
            left += 1
            right -= 1
        return min_pair_sum

        