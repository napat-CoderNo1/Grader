def shuffle(nums, n):
    x=[]
    y=[]
    for i in range(0, len(nums)):
        if i<n:
            x.append(nums[i])
        else:
            y.append(nums[i])

    output=[]
    for i in range(len(x)):
        output.append(x[i])
        output.append(y[i])
    
    return output

def shuffle2(nums, n):
    output=[]
    for i in range(n):
        output+=nums[i::n]
    print(output)

nums = [1,2,3,4,4,3,2,1]
n = 4
shuffle2(nums, n)