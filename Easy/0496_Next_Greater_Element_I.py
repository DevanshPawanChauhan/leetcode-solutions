class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        result=[]
        stack=[]
        for currentele in range(len(nums2)):
            while stack and stack[-1]<nums2[currentele]:
                popped=stack.pop()
                hashmap[popped]=nums2[currentele]
            stack.append(nums2[currentele])
        for eachele in stack:
            hashmap[eachele]=-1
        for i in nums1:
            if i in hashmap:
                result.append(hashmap[i])
        return result