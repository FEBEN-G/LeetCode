class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mydict={}
        missed=[]
        for i in range(1,len(nums)+1):
            mydict[i]=0
        for i in nums:
            mydict[i] += 1
        for key,val in mydict.items():
            if val == 0:
                missed.append(key)
        return missed

        