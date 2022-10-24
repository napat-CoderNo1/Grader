def maximum69Number(num):
    num = str(num)
    print(num)
    for i in range(len(num)):
        # print(num[i])
        if num[i]=='6':
            num = num.replace(num[i], '9', 1)
            break
    return int(num)

print(maximum69Number(9996))