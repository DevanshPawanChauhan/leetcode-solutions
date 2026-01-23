class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)
        ans=float("inf")
        n=len(cardPoints)
        min_sum=0
        for i in range(n):
            min_sum+=cardPoints[i]
            if i>=n-k:
                min_sum-=cardPoints[i-n+k]
            if i>=n-k-1:
                ans=min(ans,min_sum)
        return total-ans