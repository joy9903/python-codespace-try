
nums = [1,2,3]


first, *others = nums

print(first)
print(others)


nums1 = [1,2,3,4,5,6,7,8,9,10]
nums2 = [11,12,13,14,15,16,17,18,19,20]

nums = [*nums1, *nums2]
print(nums)