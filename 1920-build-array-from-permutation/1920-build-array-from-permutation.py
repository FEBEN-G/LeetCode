class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        x = len(nums)
        newarr = []
        for i in range(x):
            x = nums[nums[i]]
            newarr.append(x)
        return newarr
