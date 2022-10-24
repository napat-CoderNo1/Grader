nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

for i in range(n):
    nums1.remove(0)
# print(nums1)

nums1.extend(nums2)
# print(nums1)

nums1.sort()
print(nums1)