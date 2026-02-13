class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        res=[-1]*n
        for i in range(n):
            while stack and nums[stack[-1]]<nums[i]:
                dele=stack.pop()
                res[dele]=nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                dele=stack.pop()
                res[dele]=nums[i]
        return res