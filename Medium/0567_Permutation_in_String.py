k = len(s1)
n = len(s2)
d1 = {}
for ch in s1:
    d1[ch] = d1.get(ch, 0) + 1
d2 = {}
for right in range(n):
    d2[s2[right]] = d2.get(s2[right], 0) + 1
    if right >= k:
        left = right - k
        d2[s2[left]] -= 1
        if d2[s2[left]] == 0:
            del d2[s2[left]]
    if right >= k - 1 and d1 == d2:
        return True
return False
