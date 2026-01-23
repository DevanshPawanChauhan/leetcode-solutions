class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans=0
        vowel_count=0
        for i in range(len(s)):
            if s[i] in "aeiou":
                vowel_count+=1
            if i>=k:
                 if s[i-k] in "aeiou":
                    vowel_count-=1
            if i>=k-1:
                ans=max(ans,vowel_count)
        return ans