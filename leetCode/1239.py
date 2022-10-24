# not accepted by my self

arr1 = ["aa","abc","ee"]
arr2 = ["abc"]
arr3 = ["cha","r","act","ers"]
arr4 = ["abcdefghijklmnopqrstuvwxyz"]
arr5 = ["aa","bb"]
arr6 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]

def maxLength(arr):
        res = [""]
        op = 0
        
        for word in arr:
            for r in res:
                newRes = r+word
                if len(newRes)!=len(set(newRes)): continue
                res.append(newRes)
                op = max(op, len(newRes))
        return op

# def maxLength(arr):
#     res=[""]
#     output=0

#     for word in arr:
#         for j in res:
#             temp = word+j
#             if len(temp)!=len(set(temp)):
#                 continue
#             res.append(i)
#             output = max(len(temp), output)
#             print(temp)

#     return output
        
print(maxLength(arr6))

'''
x=["", arr[i]]
for loop biggest
    for in x
        arr[i]+x[i]
        check arr[i] unique
            no unique: continue
        compare with output
    x.append(arr[i])
'''