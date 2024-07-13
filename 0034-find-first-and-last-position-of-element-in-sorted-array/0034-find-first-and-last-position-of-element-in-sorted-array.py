class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = len(nums) - 1
        numList = []

        if len(nums) == 1 and nums[0] == target:
            numList.append(0)
            numList.append(0)
            return numList

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = end = mid
                while start > 0 and nums[start - 1] == target:
                    start -= 1

             
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1

                numList.append(start)
                numList.append(end)
                return numList

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        numList.append(-1)
        numList.append(-1)
        return numList
