class Solution:
    def removeDuplicates(self, nums):
        nums = list(set(nums))
        return len(nums)

nums=[0,0,1,1,1,2,3]
s1=Solution()
print(s1.removeDuplicates(nums))