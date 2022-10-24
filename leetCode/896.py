def isMonotonic(nums):
    x=nums.copy()
    x.sort()
    y=nums.copy()
    y.sort(reverse=True)
    if nums==x or nums==y:
        return True
    return False

nums = [1,3,2]
print(isMonotonic(nums))