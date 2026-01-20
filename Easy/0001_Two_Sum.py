class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for v,k in enumerate(nums):
            t1=target-k
            if t1 in nums[v+1:]:
                i1=nums.index(k)
                i2=nums.index(t1)
                if i1==i2:
                    i2= nums.index(k,i1+ 1)
                return [i1,i2]