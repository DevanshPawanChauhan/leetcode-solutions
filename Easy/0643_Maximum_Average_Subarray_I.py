class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Fixed-size sliding window.
        Time: O(n), Space: O(1)
        Alternate approach:
        - Build window dynamically inside the loop using i >= k-1 condition.
        - Same complexity, but this version is clearer.
        """
        window_sum = sum(nums[:k])
        max_avg = window_sum / k

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]
            max_avg = max(max_avg, window_sum / k)
        return max_avg
