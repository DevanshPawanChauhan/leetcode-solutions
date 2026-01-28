d = {}
for right in range(len(nums)):
    if nums[right] in d:
        if abs(right - d[nums[right]]) <= k:
            return True
    d[nums[right]] = right
return False