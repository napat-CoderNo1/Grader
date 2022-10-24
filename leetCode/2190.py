def mostFrequent(nums, key):
    d={}
    for i in nums:
        d.update({i:0})

    for i in range(1, len(nums)):
        if nums[i-1]==key:
            d[nums[i]] +=1

    # print(d)

    l = []
    for i in d.values():
        l.append(i)
    
    # print(l)
    x = max(l)
    # print(x)

    for k, v in d.items():
        if v==x:
            return k

print(mostFrequent([1,100,200,1,100], 1))
