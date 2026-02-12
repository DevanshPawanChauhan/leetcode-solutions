class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if not stack:
                left[i] = i + 1
            else:
                left[i] = i - stack[-1]
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if not stack:
                right[i] = n - i
            else:
                right[i] = stack[-1] - i
            stack.append(i)

        min_sum = 0
        for i in range(n):
            min_sum += nums[i] * left[i] * right[i]

        left = [0] * n
        right = [0] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if not stack:
                left[i] = i + 1
            else:
                left[i] = i - stack[-1]
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if not stack:
                right[i] = n - i
            else:
                right[i] = stack[-1] - i
            stack.append(i)

        max_sum = 0
        for i in range(n):
            max_sum += nums[i] * left[i] * right[i]

        return max_sum - min_sum