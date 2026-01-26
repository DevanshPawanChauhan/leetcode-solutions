class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        ans=float("inf")
        window_size=0
        for right in range(len(nums)):
            window_size+=nums[right]
            while window_size>=target:
                ans=min(ans,right-left+1)
                window_size-=nums[left]
                left+=1
        return 0 if ans == float("inf") else ans