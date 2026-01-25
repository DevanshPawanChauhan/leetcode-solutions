class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        ans = 0
        d = {}

        for right in range(len(fruits)):
            d[fruits[right]] = d.get(fruits[right], 0) + 1

            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans
