class Solution(object):
    def findDuplicates(self, nums):
        New_list = []

        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                New_list.append(abs(i))
            else:
                nums[index] = -nums[index]
        
        return New_list
