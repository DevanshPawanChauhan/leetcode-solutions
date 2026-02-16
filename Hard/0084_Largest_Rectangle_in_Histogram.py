class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[0]*n
        right=[0]*n
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                stack.pop()
            if not stack:
                left[i]=i+1
            else:
                left[i]=i-stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                right[i]=n-i
            else:
                right[i]=stack[-1]-i
            stack.append(i)
        area=0
        width=0
        for i in range(n):
            width=right[i]+left[i]-1
            area=max(area,heights[i]*width)
        return area