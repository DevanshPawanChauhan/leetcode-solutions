class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        left=0
        right=n-1
        mid=0
        while mid<=right:
            if nums[mid]==0:
                nums[mid],nums[left]=nums[left],nums[mid]
                mid+=1
                left+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1