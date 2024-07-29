class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = {}
        for index, value in enumerate(nums):
            if value in my_dict and index - my_dict[value] <= k:
                return True
            my_dict[value] = index
        return False

        